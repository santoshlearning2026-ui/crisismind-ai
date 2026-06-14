"""Database models."""

from sqlalchemy import Column, DateTime, Integer, String, Float, Boolean, JSON, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

Base = declarative_base()


class WeatherFeatures(Base):
    """Weather features table."""

    __tablename__ = "weather_features"
    __table_args__ = (Index("idx_city_timestamp", "city", "timestamp"),)

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    city = Column(String(100), nullable=False, index=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    precipitation = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    uv_index = Column(Float, nullable=True)
    visibility = Column(Float, nullable=True)
    cloud_cover = Column(Float, nullable=True)
    data_source = Column(String(50), nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class InfrastructureFeatures(Base):
    """Infrastructure features table."""

    __tablename__ = "infrastructure_features"
    __table_args__ = (Index("idx_city_infrastructure", "city"),)

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    city = Column(String(100), nullable=False, index=True)
    drainage_quality = Column(Float, nullable=False)
    power_grid_resilience = Column(Float, nullable=False)
    hospital_count = Column(Integer, nullable=False)
    emergency_services_coverage = Column(Float, nullable=False)
    critical_infrastructure_count = Column(Integer, nullable=False)
    population_density = Column(Float, nullable=False)
    road_network_quality = Column(Float, nullable=False)
    water_supply_reliability = Column(Float, nullable=False)
    metadata = Column(JSON, nullable=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class NewsFeatures(Base):
    """News and events table."""

    __tablename__ = "news_features"
    __table_args__ = (Index("idx_city_date", "city", "published_date"),)

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    city = Column(String(100), nullable=False, index=True)
    title = Column(String(500), nullable=False)
    content = Column(String(5000), nullable=False)
    source = Column(String(100), nullable=False)
    url = Column(String(2000), nullable=True)
    sentiment = Column(Float, nullable=False)
    relevance_score = Column(Float, nullable=False)
    tags = Column(JSON, nullable=True)
    published_date = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class RiskScores(Base):
    """Risk scores table."""

    __tablename__ = "risk_scores"
    __table_args__ = (Index("idx_city_risk_type", "city", "risk_type"),)

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    city = Column(String(100), nullable=False, index=True)
    risk_type = Column(String(50), nullable=False, index=True)
    score = Column(Float, nullable=False)
    level = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False)
    factors = Column(JSON, nullable=False)
    model_version = Column(String(50), nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SimulationResults(Base):
    """Simulation results table."""

    __tablename__ = "simulation_results"
    __table_args__ = (Index("idx_city_scenario", "city", "scenario"),)

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    city = Column(String(100), nullable=False, index=True)
    scenario = Column(String(200), nullable=False, index=True)
    parameters = Column(JSON, nullable=False)
    results = Column(JSON, nullable=False)
    risk_changes = Column(JSON, nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AuditLogs(Base):
    """Audit logs table."""

    __tablename__ = "audit_logs"
    __table_args__ = (Index("idx_timestamp_action", "timestamp", "action"),)

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    action = Column(String(100), nullable=False, index=True)
    resource_type = Column(String(50), nullable=False)
    resource_id = Column(String(36), nullable=False)
    user_id = Column(String(36), nullable=True)
    details = Column(JSON, nullable=True)
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(String(500), nullable=True)
    timestamp = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
