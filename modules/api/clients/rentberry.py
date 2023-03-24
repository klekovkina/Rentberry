import requests


class Rentberry:
    def search_location(self, location):
        r = requests.post(
            "https://api.rentberry.com/v4/search_seo_url",
            data={"formattedAddress": location},
        )
        body = r.json()

        return body
