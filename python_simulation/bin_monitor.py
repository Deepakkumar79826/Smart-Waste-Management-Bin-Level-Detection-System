from python_simulation.config import BIN_HEIGHT_CM


class BinMonitor:

    def __init__(self):

        self.bin_height = BIN_HEIGHT_CM

    def calculate_fill_percentage(
        self,
        distance
    ):

        fill = (
            (
                self.bin_height - distance
            )
            / self.bin_height
        ) * 100

        fill = max(0, min(fill, 100))

        return round(fill, 2)

    def get_status(
        self,
        fill_percentage
    ):

        if fill_percentage < 40:
            return "EMPTY"

        if fill_percentage < 80:
            return "HALF FULL"

        return "FULL"