from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class RoutePoint(BaseModel):
    """Single point in a route"""
    lat: float
    lon: float
    elevation: Optional[float] = None

class RouteMetrics(BaseModel):
    """Metrics for a route"""
    distance_km: float = Field(..., description="Total distance in kilometers")
    estimated_time_min: float = Field(..., description="Estimated time in minutes")
    fuel_consumption: Optional[float] = Field(None, description="Fuel consumed (liters or kWh)")
    cost_estimate: Optional[float] = Field(None, description="Estimated cost in INR")
    carbon_emission_kg: Optional[float] = Field(None, description="CO2 emissions in kg")
    elevation_gain_m: Optional[float] = Field(None, description="Total elevation gain in meters")
    idle_time_min: Optional[float] = Field(None, description="Expected idle time in minutes")

class SingleRoute(BaseModel):
    """Single route option"""
    route_type: str = Field(..., description="fastest or green")
    polyline: List[RoutePoint] = Field(..., description="Route coordinates")
    metrics: RouteMetrics

class StationInfo(BaseModel):
    """Fuel or charging station info"""
    name: str
    lat: float
    lon: float
    distance_from_route_km: float
    station_type: str  # "fuel" or "charging"

class AlertInfo(BaseModel):
    """Alert information"""
    alert_type: str  # "low_fuel", "charging_needed", "traffic", etc.
    message: str
    severity: str  # "info", "warning", "critical"
    trigger_at_km: Optional[float] = None

class RouteResponse(BaseModel):
    """Complete response for route optimization"""
    
    # Request echo
    vehicle_type: str
    route_mode: str
    
    # Routes
    fastest_route: Optional[SingleRoute] = None
    green_route: Optional[SingleRoute] = None
    
    # Comparison (only if both routes returned)
    savings: Optional[Dict[str, Any]] = None
    
    # Additional info
    nearby_stations: List[StationInfo] = Field(default_factory=list)
    alerts: List[AlertInfo] = Field(default_factory=list)
    
    # Metadata
    timestamp: datetime = Field(default_factory=datetime.now)
    computation_time_ms: Optional[float] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "vehicle_type": "bike",
                "route_mode": "both",
                "fastest_route": {
                    "route_type": "fastest",
                    "polyline": [
                        {"lat": 12.9716, "lon": 77.5946},
                        {"lat": 12.9700, "lon": 77.5930}
                    ],
                    "metrics": {
                        "distance_km": 85.5,
                        "estimated_time_min": 120.0,
                        "fuel_consumption": 2.1,
                        "cost_estimate": 220.0,
                        "carbon_emission_kg": 5.2
                    }
                },
                "savings": {
                    "fuel_saved_liters": 0.3,
                    "cost_saved_inr": 30.0,
                    "co2_reduced_kg": 0.8,
                    "time_difference_min": 15.0
                }
            }
        }