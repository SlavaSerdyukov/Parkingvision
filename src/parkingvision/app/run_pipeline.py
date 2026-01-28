from parkingvision.app.api.mock import MockParkingAPI
from parkingvision.app.predictor import predict_parking_with_ci
from parkingvision.app.visualization import plot_prediction


def run_pipeline(
    city: str,
    parking_name: str,
    minutes_ahead: int = 30,
    use_mock: bool = False,
    show_plot: bool = True,
):
    """
    Main orchestration pipeline.
    """

    if use_mock:
        api = MockParkingAPI(city)
    else:
        raise NotImplementedError(
            "Real API integration is not enabled yet. Use --use-mock."
        )

    history = api.fetch_parking_data()

    if history.empty:
        print("No parking data available.")
        return

    pred, lower, upper = predict_parking_with_ci(
        city=city,
        parking_name=parking_name,
        minutes_ahead=minutes_ahead,
    )

    if pred is None:
        print("Not enough historical data for prediction.")
        return

    print(
        f"Prediction for '{parking_name}' in {minutes_ahead} min: "
        f"{pred:.1f} (CI {lower:.1f} – {upper:.1f})"
    )

    if show_plot:
        plot_prediction(history, pred, lower, upper, parking_name)
