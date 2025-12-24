def calculate_elevation_penalty(graph, route_nodes):
    """
    Calculates penalty for uphill segments.
    Returns 0 if elevation data is unavailable.
    """
    penalty = 0.0

    for u, v in zip(route_nodes[:-1], route_nodes[1:]):
        u_ele = graph.nodes[u].get("elevation")
        v_ele = graph.nodes[v].get("elevation")

        if u_ele is not None and v_ele is not None:
            diff = v_ele - u_ele
            if diff > 0:
                penalty += diff * 0.5  # tunable weight

    return penalty
