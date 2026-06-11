import requests


class ThingSpeakUploader:

    def __init__(
        self,
        api_key,
        url
    ):
        self.api_key = api_key
        self.url = url

    def upload(
        self,
        distance,
        fill_percentage,
        status,
        alert
    ):

        payload = {

            "api_key":
            self.api_key,

            "field1":
            distance,

            "field2":
            fill_percentage,

            "field3":
            status,

            "field4":
            alert
        }

        try:

            response = requests.get(
                self.url,
                params=payload,
                timeout=10
            )

            print(
                "ThingSpeak Response:",
                response.text
            )

        except Exception as e:

            print(
                "Upload Failed:",
                e
            )