import networkx as nx
from app.services.graph_service import load_graph, get_nearest_node


def get_fastest_route(
    start_lat: float,
    start_lon: float,
    end_lat: float,
    end_lon: float,
    city_name: str = "Bengaluru, India"
):
    """
    Compute fastest route using Dijkstra algorithm.

    Returns:
    - route: list of (lat, lon)
    - distance_meters
    - distance_km
    """

    # 1️⃣ Load cached city graph
    G = load_graph(city_name)

    # 2️⃣ Find nearest graph nodes
    start_node = get_nearest_node(G, start_lat, start_lon)
    end_node = get_nearest_node(G, end_lat, end_lon)

    # 3️⃣ Dijkstra shortest path (weight = length)
    route_nodes = nx.shortest_path(
        G,
        source=start_node,
        target=end_node,
        weight="length"
    )

    # 4️⃣ Convert nodes to polyline (lat, lon)
    route_coordinates = [
        (G.nodes[node]["y"], G.nodes[node]["x"])
        for node in route_nodes
    ]

    # 5️⃣ Compute total distance (meters)
    total_distance_m = 0.0

    for u, v in zip(route_nodes[:-1], route_nodes[1:]):
        edge_data = G.get_edge_data(u, v)

        # Handle MultiDiGraph (multiple edges)
        if isinstance(edge_data, dict):
            edge_length = min(
                data.get("length", 0)
                for data in edge_data.values()
            )
        else:
            edge_length = edge_data.get("length", 0)

        total_distance_m += edge_length

    # 6️⃣ Convert to kilometers
    total_distance_km = round(total_distance_m / 1000, 2)

    return {
        "route": route_coordinates,
        "distance_meters": round(total_distance_m, 2),
        "distance_km": total_distance_km
    }
