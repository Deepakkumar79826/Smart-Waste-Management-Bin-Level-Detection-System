import time

from python_simulation.config import (
    CSV_FILE,
    PDF_REPORT,
    SIMULATION_INTERVAL,
    THINGSPEAK_API_KEY,
    THINGSPEAK_URL
)

from python_simulation.simulator import (
    WasteBinSimulator
)

from python_simulation.data_logger import (
    DataLogger
)

from python_simulation.report_generator import (
    WasteReportGenerator
)

from python_simulation.dashboard_generator import (
    DashboardGenerator
)

from dashboard.thingspeak_uploader import (
    ThingSpeakUploader
)


def main():

    simulator = (
        WasteBinSimulator()
    )

    logger = (
        DataLogger(
            CSV_FILE
        )
    )

    uploader = (
        ThingSpeakUploader(
            THINGSPEAK_API_KEY,
            THINGSPEAK_URL
        )
    )

    print(
        "\nSmart Waste "
        "Management System\n"
    )

    while True:

        record = (
            simulator
            .generate_record()
        )

        logger.log(
            record
        )

        print(
            record
        )

        uploader.upload(
            record[
                "distance_cm"
            ],
            record[
                "fill_percentage"
            ],
            record[
                "status"
            ],
            record[
                "alert"
            ]
        )

        dashboard = (
            DashboardGenerator(
                CSV_FILE
            )
        )

        dashboard.generate_chart()

        report = (
            WasteReportGenerator(
                CSV_FILE,
                PDF_REPORT
            )
        )

        report.generate_pdf()

        time.sleep(
            SIMULATION_INTERVAL
        )


if __name__ == "__main__":
    main()