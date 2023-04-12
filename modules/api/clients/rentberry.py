import requests


class Rentberry:
    # Send the POST request for searching field
    def search_location(self, location):
        r = requests.post(
            "https://api.rentberry.com/v4/search_seo_url",
            data={"formattedAddress": location},
        )
        body = r.json()

        return body

    # Send the POST request for login
    def login(self, username, userpassword):
        # Send the login request
        # if the login is successful, the site will return token
        r = requests.post(
            "https://api.rentberry.com/v4/auth/token",
            data={
                "username": username,
                "plainPassword": userpassword,
                "formName": "signinForm",
            },
        )
        if r.status_code == 200:
            # extracting the value "auth_token" from the JSON response
            token = r.json().get("body", {}).get("auth_token")
            return token

        else:
            return None
