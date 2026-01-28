from parkingvision.app.api.mock import MockParkingAPI
import pandas as pd


def test_mock_api_returns_dataframe():
    api = MockParkingAPI(city="test_city")
    df = api.fetch_parking_data()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert {"timestamp", "name", "available", "total"}.issubset(df.columns)
