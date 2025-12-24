import osmnx as ox


def get_stations_near_route(
    route_coordinates,
    station_type: str = "fuel",
    radius_m: int = 2500
):
    """
    Detect fuel or EV charging stations near the route.
    Reliable implementation using OSMnx features API.
    """

    if not route_coordinates:
        return []

    # Sample fewer points for performance
    sampled_points = route_coordinates[::3]

    stations = {}

    # Tag definitions (IMPORTANT)
    if station_type == "fuel":
        tags = {
            "amenity": "fuel"
        }
    elif station_type == "charging":
        tags = {
            "amenity": "charging_station"
        }
    else:
        return []

    for lat, lon in sampled_points:
        try:
            gdf = ox.features_from_point(
                (lat, lon),
                tags=tags,
                dist=radius_m
            )

            if gdf.empty:
                continue

            for _, row in gdf.iterrows():
                geom = row.geometry
                if geom is None:
                    continue

                name = row.get("name", "Unknown Station")

                # Handle Point or Polygon
                if geom.geom_type == "Point":
                    s_lat, s_lon = geom.y, geom.x
                else:
                    centroid = geom.centroid
                    s_lat, s_lon = centroid.y, centroid.x

                stations[(s_lat, s_lon)] = {
                    "name": name,
                    "lat": s_lat,
                    "lon": s_lon,
                    "type": station_type
                }

        except Exception:
            continue

    return list(stations.values())
