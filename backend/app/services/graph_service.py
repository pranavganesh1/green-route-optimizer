import osmnx as ox
from functools import lru_cache

# Cache graph so it loads only once
@lru_cache(maxsize=1)
def load_graph(city_name: str = "Bengaluru, India"):
    """
    Load road network graph for a given city using OpenStreetMap.
    Cached to avoid reloading on every request.
    """
    print(f"Loading road network for {city_name}...")

    graph = ox.graph_from_place(
        city_name,
        network_type="drive",
        simplify=True
    )

    # Add edge length (meters)
    graph = ox.distance.add_edge_lengths(graph)

    print("Graph loaded successfully.")
    return graph


def get_nearest_node(graph, latitude: float, longitude: float):
    """
    Find nearest node in the graph for given coordinates.
    """
    return ox.distance.nearest_nodes(graph, longitude, latitude)
