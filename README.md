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
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── utils/          # Helper functions
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── routes/         # API endpoints
│   │   ├── models/         # Data models
│   │   ├── services/       # Business logic
│   │   └── utils/          # Helper functions
│   ├── tests/              # Unit tests
│   └── requirements.txt
├── docs/
│   ├── API.md              # API documentation
│   └── DEVELOPMENT.md      # Development guide
└── README.md

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