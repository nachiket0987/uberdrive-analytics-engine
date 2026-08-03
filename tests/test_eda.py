import os
import pytest
from uberdrive_analytics.data_loader import UberDataLoader
from uberdrive_analytics.eda_engine import UberEDAEngine

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "Uber Drives.csv")

def test_data_loader():
    loader = UberDataLoader(DATA_PATH)
    df = loader.load_clean_data()
    assert not df.empty
    assert "DURATION_MIN" in df.columns
    assert "HOUR" in df.columns

def test_eda_metrics():
    loader = UberDataLoader(DATA_PATH)
    df = loader.load_clean_data()
    engine = UberEDAEngine(df)
    metrics = engine.summary_metrics()
    assert metrics["total_trips"] > 0
    assert metrics["total_miles"] > 0
