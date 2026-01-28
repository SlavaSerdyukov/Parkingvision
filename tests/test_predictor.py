import pandas as pd
from parkingvision.app.predictor import predict_parking_with_ci
import os


def setup_module():
    os.makedirs("data/processed", exist_ok=True)

    df = pd.DataFrame(
        {
            "timestamp": pd.date_range("2024-01-01", periods=10, freq="5min"),
            "name": ["Test Parking"] * 10,
            "available": [50, 48, 47, 46, 45, 44, 43, 42, 41, 40],
            "total": [100] * 10,
        }
    )

    df.to_csv(
        "data/processed/testcity_parking_history.csv",
        index=False,
        header=False,
    )


def test_predictor_returns_prediction_and_ci():
    pred, lower, upper = predict_parking_with_ci(
        city="testcity",
        parking_name="Test Parking",
        minutes_ahead=30,
    )

    assert pred is not None
    assert lower is not None
    assert upper is not None
    assert lower <= pred <= upper
