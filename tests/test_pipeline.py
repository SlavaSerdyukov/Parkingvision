from parkingvision.app.run_pipeline import run_pipeline


def test_pipeline_runs_with_mock_and_handles_no_data(capsys):
    """
    Pipeline should run without crashing even if there is
    not enough historical data for prediction.
    """
    run_pipeline(
        city="testcity",
        parking_name="Mock Parking",
        minutes_ahead=15,
        use_mock=True,
        show_plot=False,
    )

    captured = capsys.readouterr()

    assert "Not enough historical data" in captured.out
