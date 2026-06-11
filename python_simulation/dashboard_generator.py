import os
import pandas as pd

import plotly.express as px


class DashboardGenerator:

    def __init__(
        self,
        csv_file
    ):
        self.csv_file = csv_file

    def generate_chart(self):

        if not os.path.exists(
            self.csv_file
        ):
            print(
                "No log file found."
            )
            return

        df = pd.read_csv(
            self.csv_file
        )

        if df.empty:
            print(
                "CSV empty."
            )
            return

        os.makedirs(
            "outputs",
            exist_ok=True
        )

        fig = px.line(
            df,
            x="timestamp",
            y="fill_percentage",
            title=(
                "Waste Bin Fill Level"
            )
        )

        fig.write_html(
            "outputs/dashboard.html"
        )

        print(
            "Dashboard generated."
        )