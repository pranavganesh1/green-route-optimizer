import math
import networkx as nx

from app.services.graph_service import load_graph, get_nearest_node


# =====================================================
# FASTEST ROUTE (DIJKSTRA) — YOUR EXISTING LOGIC
# =====================================================
def get_fastest_route(
    start_lat: float,
    start_lon: float,
    end_lat: float,
    end_lon: float,
    city_name: str = "Bengaluru, India"
):
    """
    Compute fastest route using Dijkstra algorithm.
    """

    G = load_graph(city_name)

    start_node = get_nearest_node(G, start_lat, start_lon)
    end_node = get_nearest_node(G, end_lat, end_lon)

    route_nodes = nx.shortest_path(
        G,
        source=start_node,
        target=end_node,
        weight="length"
    )

    route_coordinates = [
        (G.nodes[node]["y"], G.nodes[node]["x"])
        for node in route_nodes
    ]

    total_distance_m = 0.0
    for u, v in zip(route_nodes[:-1], route_nodes[1:]):
        edge_data = G.get_edge_data(u, v)
        edge_length = min(
            data.get("length", 0) for data in edge_data.values()
        )
        total_distance_m += edge_length

    return {
        "route": route_coordinates,
        "distance_meters": round(total_distance_m, 2),
        "distance_km": round(total_distance_m / 1000, 2),
    }


# =====================================================
# HELPER: A* HEURISTIC (STRAIGHT LINE DISTANCE)
# =====================================================
def _heuristic(u, v, graph):
    x1, y1 = graph.nodes[u]["x"], graph.nodes[u]["y"]
    x2, y2 = graph.nodes[v]["x"], graph.nodes[v]["y"]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# =====================================================
# HELPER: ELEVATION PENALTY
# =====================================================
def _elevation_penalty(graph, route_nodes):
    penalty = 0.0
    for u, v in zip(route_nodes[:-1], route_nodes[1:]):
        u_ele = graph.nodes[u].get("elevation")
        v_ele = graph.nodes[v].get("elevation")
        if u_ele is not None and v_ele is not None:
            diff = v_ele - u_ele
            if diff > 0:  # uphill
                penalty += diff * 0.5
    return penalty


# =====================================================
# GREEN ROUTE (A* + PENALTIES)
# =====================================================
def get_green_route(
    start_lat: float,
    start_lon: float,
    end_lat: float,
    end_lon: float,
    city_name: str = "Bengaluru, India"
):
    """
    Compute eco-friendly route using A* with elevation & idle penalties.
    """

    G = load_graph(city_name)

    start_node = get_nearest_node(G, start_lat, start_lon)
    end_node = get_nearest_node(G, end_lat, end_lon)

    route_nodes = nx.astar_path(
        G,
        start_node,
        end_node,
        heuristic=lambda u, v: _heuristic(u, v, G),
        weight="length"
    )

    route_coordinates = [
        (G.nodes[node]["y"], G.nodes[node]["x"])
        for node in route_nodes
    ]

    distance_m = 0.0
    for u, v in zip(route_nodes[:-1], route_nodes[1:]):
        edge_data = G.get_edge_data(u, v)
        edge_length = min(
            data.get("length", 0) for data in edge_data.values()
        )
        distance_m += edge_length

    elevation_penalty = _elevation_penalty(G, route_nodes)
    idle_penalty = len(route_nodes) * 2.0  # simple idle model

    green_cost = distance_m + elevation_penalty + idle_penalty

    return {
        "route": route_coordinates,
        "distance_km": round(distance_m / 1000, 2),
        "elevation_penalty": round(elevation_penalty, 2),
        "idle_penalty": round(idle_penalty, 2),
        "green_cost": round(green_cost, 2),
    }


# =====================================================
# ROUTE COMPARISON
# =====================================================
def compare_routes(fastest, green):
    """
    Compare fastest vs green route.
    """

    return {
        "fastest_distance_km": fastest["distance_km"],
        "green_distance_km": green["distance_km"],
        "green_cost": green["green_cost"],
        "eco_friendly": green["green_cost"] < (fastest["distance_km"] * 1000),
    }
