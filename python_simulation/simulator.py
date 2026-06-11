import random
from datetime import datetime

from python_simulation.bin_monitor import BinMonitor
from python_simulation.alert_manager import AlertManager

class WasteBinSimulator:

    def __init__(self):

        self.monitor = BinMonitor()

        self.alert_manager = AlertManager()

    def generate_distance(self):

        return round(
            random.uniform(2, 40),
            2
        )

    def generate_record(self):

        distance = self.generate_distance()

        fill_percentage = (
            self.monitor
            .calculate_fill_percentage(
                distance
            )
        )

        status = (
            self.monitor
            .get_status(
                fill_percentage
            )
        )

        alert_data = (
            self.alert_manager
            .get_alert(
                fill_percentage
            )
        )

        return {

            "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "distance_cm":
            distance,

            "fill_percentage":
            fill_percentage,

            "status":
            status,

            "alert":
            alert_data["message"]
        }

    def simulate_empty_bin(self):

        distance = 38

        fill = (
            self.monitor
            .calculate_fill_percentage(
                distance
            )
        )

        return {
            "distance": distance,
            "fill": fill
        }

    def simulate_half_bin(self):

        distance = 20

        fill = (
            self.monitor
            .calculate_fill_percentage(
                distance
            )
        )

        return {
            "distance": distance,
            "fill": fill
        }

    def simulate_nearly_full(self):

        distance = 8

        fill = (
            self.monitor
            .calculate_fill_percentage(
                distance
            )
        )

        return {
            "distance": distance,
            "fill": fill
        }

    def simulate_full_bin(self):

        distance = 2

        fill = (
            self.monitor
            .calculate_fill_percentage(
                distance
            )
        )

        return {
            "distance": distance,
            "fill": fill
        }


if __name__ == "__main__":

    simulator = WasteBinSimulator()

    record = simulator.generate_record()

    print(record)