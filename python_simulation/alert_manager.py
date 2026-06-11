class AlertManager:

    def __init__(self):

        self.alert_threshold = 80

    def get_alert(self, fill_percentage):

        if fill_percentage >= self.alert_threshold:

            return {
                "alert": True,
                "message": "BIN FULL - COLLECTION REQUIRED"
            }

        return {
            "alert": False,
            "message": "Normal"
        }