import os
import pandas as pd

from fpdf import FPDF


class WasteReportGenerator:

    def __init__(
        self,
        csv_file,
        pdf_file
    ):
        self.csv_file = csv_file
        self.pdf_file = pdf_file

    def generate_pdf(self):

        if not os.path.exists(
            self.csv_file
        ):
            print(
                "CSV file not found."
            )
            return

        df = pd.read_csv(
            self.csv_file
        )

        if df.empty:
            print(
                "No data available."
            )
            return

        os.makedirs(
            os.path.dirname(
                self.pdf_file
            ),
            exist_ok=True
        )

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            "B",
            16
        )

        pdf.cell(
            200,
            10,
            "Smart Waste Management Report",
            ln=True,
            align="C"
        )

        pdf.ln(5)

        pdf.set_font(
            "Arial",
            "",
            10
        )

        headers = [
            "Time",
            "Distance",
            "Fill %",
            "Status",
            "Alert"
        ]

        widths = [
            50,
            25,
            25,
            40,
            40
        ]

        for i, header in enumerate(
            headers
        ):
            pdf.cell(
                widths[i],
                10,
                header,
                border=1
            )

        pdf.ln()

        for _, row in df.iterrows():

            pdf.cell(
                widths[0],
                8,
                str(
                    row["timestamp"]
                )[:19],
                border=1
            )

            pdf.cell(
                widths[1],
                8,
                str(
                    row["distance_cm"]
                ),
                border=1
            )

            pdf.cell(
                widths[2],
                8,
                str(
                    row["fill_percentage"]
                ),
                border=1
            )

            pdf.cell(
                widths[3],
                8,
                str(
                    row["status"]
                ),
                border=1
            )

            pdf.cell(
                widths[4],
                8,
                str(
                    row["alert"]
                ),
                border=1
            )

            pdf.ln()

        pdf.output(
            self.pdf_file
        )

        print(
            f"PDF Report Generated: "
            f"{self.pdf_file}"
        )