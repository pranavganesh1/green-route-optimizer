# 🌱 Green Route Optimizer

**Dual-Mode (Fuel + EV) Smart Routing System**

A intelligent routing platform designed for both fuel-based and electric delivery vehicles that optimizes routes based on fuel/energy consumption, idle time, elevation, and vehicle type.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![React](https://img.shields.io/badge/react-18+-61dafb.svg)

## 🎯 Problem Statement

Traditional navigation systems optimize only for the fastest routes, leading to:
- High fuel costs and battery drain
- Traffic idling losses
- Increased stress for delivery partners
- Lack of carbon emission tracking
- ESG compliance challenges for logistics companies

## 💡 Solution

A single platform with two intelligent modes:
- **Fuel Mode**: Optimizes for bikes, vans, and trucks
- **EV Mode**: Optimizes for electric bikes, vans, and trucks

Both modes compare fastest routes with green routes optimized for cost, energy efficiency, and sustainability.

## ✨ Key Features

- 🔄 **Dual-Mode Routing**: Seamless switching between Fuel and EV modes
- ⛽ **Station Awareness**: Real-time fuel/charging station display with voice alerts
- 🌍 **Carbon Tracking**: Calculate and display emission scores
- 💰 **Cost Projection**: Daily, monthly, and yearly savings estimates
- 📊 **Route Difficulty Index**: Evaluate route complexity before departure
- 🎤 **Voice Alerts**: Hands-free safety notifications
- ⚡ **Regenerative Braking**: EV energy recovery calculations
- 🗺️ **Elevation-Aware**: Optimize routes based on terrain

## 🛠️ Technology Stack

### Frontend
- React.js
- Leaflet.js (mapping)
- Chart.js (visualizations)
- Tailwind CSS (styling)
- Web Speech API (voice alerts)

### Backend
- Python 3.9+
- FastAPI
- OSMnx (OpenStreetMap network analysis)
- NetworkX (graph algorithms)

### Data Sources
- OpenStreetMap
- Elevation data APIs

## 📋 Prerequisites

- **Node.js** 18+ and npm/yarn
- **Python** 3.9+
- **Git**
- OpenStreetMap API access

## 🚀 Quick Start

### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

Backend will be available at `http://localhost:8000`

### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at `http://localhost:3000`

## 📁 Project Structure
green-route-optimizer/
│
├── README.md                     # Project overview (already created)
├── .gitignore
├── .env.example                  # Environment variables template
│
├── docs/                         # Documentation (shared understanding)
│   ├── API.md                    # Backend API contracts
│   ├── ARCHITECTURE.md           # System design & flow
│   ├── DEMO.md                   # Demo steps (what to show)
│   └── DEVELOPMENT.md            # Dev guidelines for both members
│
├── backend/                      # 👨‍💻 BACKEND (YOU)
│   ├── app/
│   │   ├── main.py               # FastAPI entry point
│   │   │
│   │   ├── core/                 # App-level configs
│   │   │   ├── config.py         # Constants, city name, thresholds
│   │   │   └── logger.py
│   │   │
│   │   ├── routes/               # API endpoints
│   │   │   ├── __init__.py
│   │   │   └── route_optimizer.py  # POST /route/optimize
│   │   │
│   │   ├── models/               # Request & response schemas
│   │   │   ├── __init__.py
│   │   │   ├── request.py        # Input payload
│   │   │   ├── response.py       # Output payload
│   │   │   └── vehicle.py        # Vehicle models
│   │   │
│   │   ├── services/             # ⭐ CORE LOGIC (MOST IMPORTANT)
│   │   │   ├── __init__.py
│   │   │   ├── graph_service.py      # Load OSM graph
│   │   │   ├── routing_service.py    # Dijkstra + A*
│   │   │   ├── cost_service.py       # Fuel / EV energy calc
│   │   │   ├── station_service.py    # Fuel & charging stations
│   │   │   ├── carbon_service.py     # CO₂ calculations
│   │   │   └── alert_service.py      # Alert trigger logic
│   │   │
│   │   ├── utils/                # Helper functions
│   │   │   ├── __init__.py
│   │   │   ├── geo.py             # Distance, polyline helpers
│   │   │   └── elevation.py       # Elevation helpers
│   │   │
│   │   └── constants/             # Fixed values (shared logic)
│   │       ├── __init__.py
│   │       ├── vehicles.py        # Mileage, energy rates
│   │       └── emissions.py       # CO₂ factors
│   │
│   ├── tests/
│   │   └── test_routes.py
│   │
│   ├── requirements.txt
│   └── README.md
│
├── frontend/                     # 👨‍🎨 FRONTEND (YOUR FRIEND)
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── app/                  # App-level setup
│   │   │   ├── App.jsx
│   │   │   └── router.jsx
│   │   │
│   │   ├── pages/                # Screens (mobile-first)
│   │   │   ├── Home.jsx          # Input screen
│   │   │   └── Result.jsx        # Map + dashboard
│   │   │
│   │   ├── components/           # Reusable UI blocks
│   │   │   ├── MapView.jsx       # Leaflet map
│   │   │   ├── RouteLayer.jsx    # Fastest vs Green routes
│   │   │   ├── StationLayer.jsx  # Fuel / charging icons
│   │   │   ├── Dashboard.jsx     # Metrics panel
│   │   │   └── VoiceAlert.jsx    # Voice alert handler
│   │   │
│   │   ├── services/             # API calls (matches backend)
│   │   │   └── routeService.js   # Calls /route/optimize
│   │   │
│   │   ├── utils/                # Frontend helpers
│   │   │   ├── constants.js      # Same logic as backend
│   │   │   └── formatters.js
│   │   │
│   │   ├── styles/
│   │   │   └── tailwind.css
│   │   │
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── README.md
│
└── mobile/ (OPTIONAL)
    ├── README.md                 # PWA / mobile notes
    └── manifest.json             # Add-to-home-screen support


## 🗓️ Development Roadmap (14 Days)

- **Days 1-2**: Planning & setup
- **Days 3-4**: Map & road data integration
- **Days 5-6**: Fastest route algorithm
- **Days 7-8**: Green route optimization
- **Days 9-10**: Fuel/EV logic + stations
- **Days 11-12**: Dashboard + voice alerts
- **Days 13-14**: Testing, documentation, demo

## 👥 Team

**2-Member Team Structure:**
- **Member 1**: Backend & Algorithms (routing logic, fuel/energy models, APIs)
- **Member 2**: Frontend & Visualization (UI, maps, charts, voice alerts)

## 📊 Impact

- **Delivery Partners**: Save fuel, reduce stress, increase earnings
- **Logistics Companies**: Reduce fleet costs, ensure EV range safety, meet ESG goals
- **Environment**: Lower carbon emissions through optimized routing

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

---

**Built with ❤️ for sustainable logistics**
