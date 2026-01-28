import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.utils import resample


def predict_parking_with_ci(
    city,
    parking_name,
    minutes_ahead=30,
    n_bootstrap=1000,
    alpha=0.05,
):
    file_name = f"data/processed/{city}_parking_history.csv"

    try:
        df = pd.read_csv(
            file_name,
            names=["timestamp", "name", "available", "total"],
        )
    except FileNotFoundError:
        return None, None, None

    df = df[df["name"] == parking_name]
    if df.empty:
        return None, None, None

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    df["time_sec"] = df["timestamp"].astype("int64") // 10**9

    X = df[["time_sec"]].values
    y = df["available"].values

    model = LinearRegression()
    model.fit(X, y)

    future_time = np.array(
        [[df["time_sec"].max() + minutes_ahead * 60]]
    )
    pred = model.predict(future_time)[0]

    preds_bootstrap = []
    for _ in range(n_bootstrap):
        X_res, y_res = resample(X, y)
        model.fit(X_res, y_res)
        preds_bootstrap.append(model.predict(future_time)[0])

    lower = np.percentile(preds_bootstrap, 100 * alpha / 2)
    upper = np.percentile(preds_bootstrap, 100 * (1 - alpha / 2))

    return pred, lower, upper
