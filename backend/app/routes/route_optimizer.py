from fastapi import APIRouter, HTTPException, status
from app.models.request import RouteRequest
from app.models.response import RouteResponse, SingleRoute, RoutePoint, RouteMetrics
import time

router = APIRouter(prefix="/route", tags=["Route Optimization"])

@router.post("/optimize", response_model=RouteResponse, status_code=status.HTTP_200_OK)
async def optimize_route(request: RouteRequest):
    """
    Optimize route based on vehicle type and preferences
    
    - **start_lat/lon**: Starting coordinates
    - **end_lat/lon**: Destination coordinates
    - **vehicle_type**: Type of vehicle (bike, van, truck, ev_bike, ev_van, ev_truck)
    - **route_mode**: fastest, green, or both
    - **current_fuel_level**: Optional current fuel/battery percentage
    """
    
    start_time = time.time()
    
    try:
        # TODO: Member 1 will provide graph service
        # For now, return mock data to test API structure
        
        # Mock fastest route
        fastest_route = SingleRoute(
            route_type="fastest",
            polyline=[
                RoutePoint(lat=request.start_lat, lon=request.start_lon),
                RoutePoint(lat=request.end_lat, lon=request.end_lon)
            ],
            metrics=RouteMetrics(
                distance_km=10.0,
                estimated_time_min=15.0,
                fuel_consumption=0.5,
                cost_estimate=50.0,
                carbon_emission_kg=1.2
            )
        )
        
        # Mock green route
        green_route = SingleRoute(
            route_type="green",
            polyline=[
                RoutePoint(lat=request.start_lat, lon=request.start_lon),
                RoutePoint(lat=request.end_lat, lon=request.end_lon)
            ],
            metrics=RouteMetrics(
                distance_km=11.0,
                estimated_time_min=18.0,
                fuel_consumption=0.4,
                cost_estimate=42.0,
                carbon_emission_kg=1.0
            )
        )
        
        computation_time = (time.time() - start_time) * 1000  # Convert to ms
        
        response = RouteResponse(
            vehicle_type=request.vehicle_type.value,
            route_mode=request.route_mode.value,
            fastest_route=fastest_route if request.route_mode != "green" else None,
            green_route=green_route if request.route_mode != "fastest" else None,
            savings={
                "fuel_saved_liters": 0.1,
                "cost_saved_inr": 8.0,
                "co2_reduced_kg": 0.2,
                "time_difference_min": 3.0
            } if request.route_mode == "both" else None,
            computation_time_ms=computation_time
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Route optimization failed: {str(e)}"
        )

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "route-optimizer"}