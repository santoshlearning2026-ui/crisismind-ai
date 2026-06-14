# CRISISMIND AI - Autonomous Infrastructure Risk Prediction Agent

[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black.svg)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

CRISISMIND AI is an autonomous infrastructure risk prediction system that leverages AI agents, machine learning models, and real-time intelligence to predict flood risk, heatwave risk, and power outage risk for cities.

**Key Features:**
- Real-time weather intelligence integration
- Infrastructure vulnerability assessment
- News and event monitoring
- AI-powered risk prediction using XGBoost and LightGBM
- Explainable AI for risk factors
- LangGraph-based agentic workflow
- Gemini API integration for natural language analysis
- Production-ready REST API with OpenAPI documentation
- Comprehensive monitoring and logging

## Architecture

```
CRISISMIND AI
├── Backend (FastAPI + Python 3.12)
├── Frontend (Next.js 15 + React + TypeScript)
├── AI Agents (LangGraph + LangChain)
├── ML Models (XGBoost, LightGBM)
├── Data Pipeline (PostgreSQL + ChromaDB)
└── DevOps (Docker + GitHub Actions)
```

## Tech Stack

### Backend
- **Framework:** FastAPI 0.104.1
- **Runtime:** Python 3.12
- **Graph Intelligence:** LangGraph
- **Language Model Chain:** LangChain
- **Database:** PostgreSQL 15
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic
- **Vector DB:** ChromaDB
- **Validation:** Pydantic v2
- **API Documentation:** OpenAPI 3.1.0

### Frontend
- **Framework:** Next.js 15
- **UI Library:** React 19
- **Language:** TypeScript 5.3
- **Styling:** TailwindCSS 3.3
- **Charts:** Recharts 2.10
- **HTTP Client:** Axios

### ML/Data Science
- **Gradient Boosting:** XGBoost, LightGBM
- **ML Framework:** Scikit-Learn
- **Data Processing:** Pandas, Polars
- **Numerical Computing:** NumPy
- **Visualization:** Matplotlib, Seaborn

### DevOps & Infrastructure
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Environment Management:** Python-dotenv
- **Logging:** Structlog, Python Logging

## Project Structure

```
crisismind-ai/
├── backend/                          # FastAPI backend service
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI app entry point
│   │   ├── config.py                # Configuration management
│   │   ├── dependencies.py          # Dependency injection
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── v1/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── router.py        # API routes v1
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── health.py
│   │   │   │   │   ├── risk.py
│   │   │   │   │   ├── weather.py
│   │   │   │   │   ├── simulation.py
│   │   │   │   │   └── explanations.py
│   │   │   │   └── schemas/
│   │   │   │       ├── __init__.py
│   │   │   │       ├── request.py
│   │   │   │       └── response.py
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   ├── base.py              # Base agent class
│   │   │   ├── weather_agent.py
│   │   │   ├── infrastructure_agent.py
│   │   │   ├── news_agent.py
│   │   │   ├── prediction_agent.py
│   │   │   ├── recommendation_agent.py
│   │   │   ├── orchestrator_agent.py
│   │   │   └── graph.py             # LangGraph workflow
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── database/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   ├── weather.py
│   │   │   │   ├── infrastructure.py
│   │   │   │   ├── news.py
│   │   │   │   ├── risk.py
│   │   │   │   ├── simulation.py
│   │   │   │   └── audit.py
│   │   │   └── ml/
│   │   │       ├── __init__.py
│   │   │       ├── flood_risk_model.py
│   │   │       ├── heatwave_risk_model.py
│   │   │       └── outage_risk_model.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── weather_service.py
│   │   │   ├── infrastructure_service.py
│   │   │   ├── news_service.py
│   │   │   ├── risk_service.py
│   │   │   ├── simulation_service.py
│   │   │   └── gemini_service.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── logging.py           # Structured logging
│   │   │   ├── security.py
│   │   │   ├── exceptions.py
│   │   │   └── constants.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── validators.py
│   │       ├── formatters.py
│   │       └── helpers.py
│   ├── migrations/                  # Alembic database migrations
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   └── versions/
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── unit/
│   │   │   ├── __init__.py
│   │   │   ├── test_config.py
│   │   │   ├── test_services/
│   │   │   ├── test_models/
│   │   │   └── test_agents/
│   │   ├── integration/
│   │   │   ├── __init__.py
│   │   │   ├── test_database.py
│   │   │   ├── test_api_endpoints.py
│   │   │   └── test_workflows.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── test_health.py
│   │   │   ├── test_risk.py
│   │   │   ├── test_weather.py
│   │   │   └── test_explanations.py
│   │   └── performance/
│   │       ├── __init__.py
│   │       └── test_load.py
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── Dockerfile
├── frontend/                         # Next.js frontend application
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── dashboard/
│   │   ├── risk/
│   │   ├── simulation/
│   │   └── api/
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── Navigation.tsx
│   │   ├── RiskCard.tsx
│   │   ├── charts/
│   │   │   ├── RiskChart.tsx
│   │   │   └── TrendChart.tsx
│   │   └── common/
│   ├── lib/
│   │   ├── api-client.ts
│   │   ├── constants.ts
│   │   └── types.ts
│   ├── styles/
│   │   └── globals.css
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   ├── next.config.ts
│   └── Dockerfile
├── agents/                           # Agent definitions and workflows
│   └── README.md
├── models/                           # ML model artifacts
│   ├── README.md
│   └── .gitkeep
├── datasets/                         # Training and reference datasets
│   ├── README.md
│   └── .gitkeep
├── notebooks/                        # Jupyter notebooks for analysis
│   ├── README.md
│   ├── 01_eda.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation.ipynb
├── docs/                             # Comprehensive documentation
│   ├── 01_PRD.md
│   ├── 02_ARCHITECTURE.md
│   ├── 03_DATA_STRATEGY.md
│   ├── 04_AGENT_DESIGN.md
│   ├── 05_API_DOCUMENTATION.md
│   ├── 06_TEST_STRATEGY.md
│   ├── 07_DEPLOYMENT_GUIDE.md
│   ├── 08_USER_GUIDE.md
│   └── 09_KAGGLE_SUBMISSION.md
├── deployment/                       # Deployment configurations
│   ├── docker-compose.yml
│   ├── docker-compose.prod.yml
│   ├── nginx.conf
│   └── kubernetes/
│       └── .gitkeep
├── tests/                            # Root level test scripts
│   ├── e2e/
│   └── load/
├── scripts/                          # Utility scripts
│   ├── setup.sh
│   ├── migrate.sh
│   ├── seed.sh
│   └── load_models.sh
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── cd.yml
│       ├── security.yml
│       └── performance.yml
├── .dockerignore
├── .gitignore
├── .env.example
├── docker-compose.yml
├── Makefile
├── LICENSE
└── CONTRIBUTING.md
```

## Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 15
- Git

### Local Development Setup

#### 1. Clone Repository
```bash
git clone https://github.com/santoshlearning2026-ui/crisismind-ai.git
cd crisismind-ai
```

#### 2. Setup Backend
```bash
cd backend
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

#### 3. Setup Frontend
```bash
cd ../frontend
npm install
cp .env.example .env.local
```

#### 4. Start Services with Docker Compose
```bash
cd ..
docker-compose up -d
```

#### 5. Run Migrations
```bash
cd backend
alembic upgrade head
```

#### 6. Start Backend
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### 7. Start Frontend (in new terminal)
```bash
cd frontend
npm run dev
```

### Access Points
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs
- **Frontend:** http://localhost:3000
- **Database:** localhost:5432 (PostgreSQL)
- **Vector DB:** localhost:8000 (ChromaDB)

## API Endpoints

### Health Check
```bash
GET /health
```

### Risk Assessment
```bash
GET /api/v1/risk/{city}
POST /api/v1/simulate
GET /api/v1/weather/{city}
GET /api/v1/explanations/{city}
```

## Database Schema

### Core Tables
- `weather_features` - Real-time and historical weather data
- `infrastructure_features` - Critical infrastructure inventory
- `news_features` - News and event monitoring data
- `risk_scores` - AI-predicted risk assessments
- `simulation_results` - Scenario simulation outputs
- `audit_logs` - System audit trail

## AI Agents

### Agent Architecture
1. **Weather Agent** - Collects and processes weather data
2. **Infrastructure Agent** - Analyzes infrastructure vulnerability
3. **News Agent** - Monitors relevant news and events
4. **Prediction Agent** - Generates risk predictions
5. **Recommendation Agent** - Creates actionable recommendations
6. **Orchestrator Agent** - Coordinates all agents using LangGraph

## Testing

### Run All Tests
```bash
cd backend
pytest
```

### Run Specific Test Suite
```bash
pytest tests/unit/
pytest tests/integration/
pytest tests/api/
pytest tests/performance/
```

### Run with Coverage
```bash
pytest --cov=app tests/
```

## Docker Commands

### Build Images
```bash
docker-compose build
```

### Start Services
```bash
docker-compose up
```

### Stop Services
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Production Deployment
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## Environment Variables

Copy `.env.example` to `.env` and configure:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/crisismind

# API Keys
GEMINI_API_KEY=your_gemini_key
OPENWEATHER_API_KEY=your_openweather_key

# Application
APP_ENV=development
DEBUG=True
SECRET_KEY=your_secret_key

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Documentation

Comprehensive documentation available in `/docs`:

- **01_PRD.md** - Product Requirements Document
- **02_ARCHITECTURE.md** - System architecture and design
- **03_DATA_STRATEGY.md** - Data collection and processing strategy
- **04_AGENT_DESIGN.md** - AI agent design and LangGraph workflow
- **05_API_DOCUMENTATION.md** - Complete API reference
- **06_TEST_STRATEGY.md** - Testing strategy and coverage
- **07_DEPLOYMENT_GUIDE.md** - Deployment and DevOps
- **08_USER_GUIDE.md** - End-user documentation
- **09_KAGGLE_SUBMISSION.md** - Kaggle competition guidelines

## Development Workflow

### Branch Strategy
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/*` - Feature development
- `bugfix/*` - Bug fixes
- `hotfix/*` - Production hotfixes

### Pre-commit Checks
```bash
pip install pre-commit
pre-commit install
```

### Code Quality
- **Linting:** pylint, black
- **Type Checking:** mypy
- **Testing:** pytest with 80%+ coverage
- **Documentation:** docstrings for all functions

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Performance Characteristics

- **Risk Prediction Latency:** < 500ms
- **API Response Time:** < 200ms (p95)
- **Database Query Performance:** < 100ms (p95)
- **Concurrent Users:** 1000+
- **Data Pipeline:** Real-time ingestion

## Monitoring & Logging

- **Structured Logging:** JSON format with context
- **Health Checks:** Liveness and readiness probes
- **Metrics:** Prometheus-compatible endpoints
- **Tracing:** OpenTelemetry integration ready

## Security

- CORS properly configured
- Request validation with Pydantic
- Rate limiting on API endpoints
- Environment-based secrets management
- Database connection pooling
- SQL injection prevention via SQLAlchemy

## Troubleshooting

### Database Connection Issues
```bash
# Check PostgreSQL container
docker-compose logs postgres

# Reset database
alembic downgrade base
alembic upgrade head
```

### Port Already in Use
```bash
# Kill process on port
lsof -ti:8000 | xargs kill -9
```

### Dependencies Issues
```bash
# Clear cache and reinstall
pip cache purge
pip install -r requirements.txt --force-reinstall
```

## License

MIT License - See [LICENSE](LICENSE) for details

## Support

For issues and questions:
1. Check existing [GitHub Issues](https://github.com/santoshlearning2026-ui/crisismind-ai/issues)
2. Create a new issue with detailed information
3. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

## Roadmap

- [ ] GraphQL API support
- [ ] Real-time WebSocket notifications
- [ ] Mobile app (React Native)
- [ ] Advanced ML model ensemble
- [ ] Kubernetes deployment automation
- [ ] Multi-language support
- [ ] Advanced visualization dashboard

## Authors

- **Principal Architect:** Santosh Learning
- **Project:** CRISISMIND AI

## Acknowledgments

- FastAPI community
- LangChain and LangGraph teams
- OpenWeather API
- Kaggle community
