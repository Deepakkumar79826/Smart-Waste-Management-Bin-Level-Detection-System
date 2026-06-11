import os
import pandas as pd


class DataLogger:

    def __init__(self, csv_file):
        self.csv_file = csv_file

        os.makedirs(
            os.path.dirname(csv_file),
            exist_ok=True
        )

        if not os.path.exists(csv_file):

            columns = [
                "timestamp",
                "distance_cm",
                "fill_percentage",
                "status",
                "alert"
            ]

            pd.DataFrame(columns=columns).to_csv(
                csv_file,
                index=False
            )

    def log(self, record):

        df = pd.DataFrame([record])

        df.to_csv(
            self.csv_file,
            mode="a",
            header=False,
            index=False
        )

    def read_logs(self):

        return pd.read_csv(self.csv_file)