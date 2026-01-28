import matplotlib.pyplot as plt
import pandas as pd


def plot_prediction(
    city: str,
    parking_name: str,
    prediction: float,
    lower: float,
    upper: float,
):
    df = pd.read_csv(
        f"data/processed/{city}_parking_history.csv",
        names=["timestamp", "name", "available", "total"],
    )

    df = df[df["name"] == parking_name]
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["available"], label="Historical")

    plt.axhline(prediction, linestyle="--", label="Prediction")
    plt.fill_between(
        df["timestamp"],
        lower,
        upper,
        alpha=0.2,
        label="Confidence Interval",
    )

    plt.legend()
    plt.title(f"{parking_name} availability forecast")
    plt.show()
