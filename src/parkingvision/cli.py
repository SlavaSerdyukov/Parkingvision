import argparse

from parkingvision.app.run_pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="parkingvision",
        description="Parking occupancy prediction pipeline",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser(
        "run",
        help="Run parking prediction pipeline",
    )

    run_parser.add_argument("--city", required=True, help="City name")
    run_parser.add_argument("--parking", required=True, help="Parking name")
    run_parser.add_argument(
        "--minutes-ahead",
        type=int,
        default=30,
        help="Prediction horizon in minutes",
    )
    run_parser.add_argument(
        "--use-mock",
        action="store_true",
        help="Use mock data source",
    )
    run_parser.add_argument(
        "--show-plot",
        action="store_true",
        help="Show prediction plot",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run":
        run_pipeline(
            city=args.city,
            parking_name=args.parking,
            minutes_ahead=args.minutes_ahead,
            use_mock=args.use_mock,
            show_plot=args.show_plot,
        )


if __name__ == "__main__":
    main()
