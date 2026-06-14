.PHONY: help install dev test lint format clean docker-build docker-up docker-down db-migrate db-seed

help:
	@echo "CRISISMIND AI - Available Commands"
	@echo "================================="
	@echo ""
	@echo "Setup:"
	@echo "  make install              Install all dependencies"
	@echo "  make setup                Complete local setup"
	@echo ""
	@echo "Development:"
	@echo "  make dev                  Run development server"
	@echo "  make dev-backend          Run backend only"
	@echo "  make dev-frontend         Run frontend only"
	@echo ""
	@echo "Testing:"
	@echo "  make test                 Run all tests"
	@echo "  make test-unit            Run unit tests"
	@echo "  make test-integration     Run integration tests"
	@echo "  make test-api             Run API tests"
	@echo "  make test-coverage        Run tests with coverage report"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint                 Run linters"
	@echo "  make format               Format code"
	@echo "  make type-check           Run type checking"
	@echo ""
	@echo "Database:"
	@echo "  make db-migrate           Run database migrations"
	@echo "  make db-seed              Seed database with sample data"
	@echo "  make db-reset             Reset database"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build         Build Docker images"
	@echo "  make docker-up            Start Docker containers"
	@echo "  make docker-down          Stop Docker containers"
	@echo "  make docker-logs          View Docker logs"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean                Clean up generated files"
	@echo "  make clean-all            Complete cleanup including cache"

.PHONY: install
install:
	@echo "Installing dependencies..."
	cd backend && pip install -r requirements.txt
	cd ../frontend && npm install
	@echo "Dependencies installed!"

.PHONY: setup
setup:
	@echo "Setting up CRISISMIND AI..."
	if [ ! -f .env ]; then cp .env.example .env; fi
	cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
	cd ../frontend && npm install
	@echo "Setup complete! Run 'make docker-up' to start services."

.PHONY: dev
dev: docker-up dev-backend

.PHONY: dev-backend
dev-backend:
	cd backend && source venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

.PHONY: dev-frontend
dev-frontend:
	cd frontend && npm run dev

.PHONY: test
test:
	cd backend && pytest

.PHONY: test-unit
test-unit:
	cd backend && pytest tests/unit/ -v

.PHONY: test-integration
test-integration:
	cd backend && pytest tests/integration/ -v

.PHONY: test-api
test-api:
	cd backend && pytest tests/api/ -v

.PHONY: test-coverage
test-coverage:
	cd backend && pytest --cov=app --cov-report=html tests/
	@echo "Coverage report generated in htmlcov/index.html"

.PHONY: lint
lint:
	cd backend && pylint app/ || true
	cd backend && mypy app/

.PHONY: format
format:
	cd backend && black app/ tests/
	cd backend && isort app/ tests/
	cd frontend && npx prettier --write .

.PHONY: type-check
type-check:
	cd backend && mypy app/

db-migrate:
	cd backend && alembic upgrade head

.PHONY: db-seed
db-seed:
	cd backend && python scripts/seed_database.py

.PHONY: db-reset
db-reset:
	cd backend && alembic downgrade base && alembic upgrade head

.PHONY: docker-build
docker-build:
	docker-compose build

.PHONY: docker-up
docker-up:
	docker-compose up -d
	@echo "Services started! Check logs with 'make docker-logs'"

.PHONY: docker-down
docker-down:
	docker-compose down
	@echo "Services stopped!"

.PHONY: docker-logs
docker-logs:
	docker-compose logs -f

.PHONY: clean
clean:
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -r {} + 2>/dev/null || true
	cd frontend && rm -rf .next out node_modules/.cache || true

.PHONY: clean-all
clean-all: clean
	cd backend && rm -rf venv/
	cd frontend && rm -rf node_modules/
	@echo "Deep cleanup complete!"
