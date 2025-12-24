from pydantic import BaseModel, Field
from typing import Literal, Optional
from enum import Enum

class VehicleType(str, Enum):
    """Vehicle types supported"""
    BIKE = "bike"
    VAN = "van"
    TRUCK = "truck"
    EV_BIKE = "ev_bike"
    EV_VAN = "ev_van"
    EV_TRUCK = "ev_truck"

class RouteMode(str, Enum):
    """Routing mode"""
    FASTEST = "fastest"
    GREEN = "green"
    BOTH = "both"

class RouteRequest(BaseModel):
    """Request model for route optimization"""
    
    # Location data
    start_lat: float = Field(..., ge=-90, le=90, description="Starting latitude")
    start_lon: float = Field(..., ge=-180, le=180, description="Starting longitude")
    end_lat: float = Field(..., ge=-90, le=90, description="Destination latitude")
    end_lon: float = Field(..., ge=-180, le=180, description="Destination longitude")
    
    # Vehicle configuration
    vehicle_type: VehicleType = Field(..., description="Type of vehicle")
    
    # Route preferences
    route_mode: RouteMode = Field(default=RouteMode.BOTH, description="Routing mode")
    
    # Optional parameters
    current_fuel_level: Optional[float] = Field(None, ge=0, le=100, description="Current fuel/battery %")
    traffic_factor: Optional[float] = Field(1.0, ge=0.5, le=2.0, description="Traffic multiplier")
    
    class Config:
        json_schema_extra = {
            "example": {
                "start_lat": 12.9716,
                "start_lon": 77.5946,
                "end_lat": 12.2958,
                "end_lon": 76.6394,
                "vehicle_type": "bike",
                "route_mode": "both",
                "current_fuel_level": 75.0,
                "traffic_factor": 1.2
            }
        }