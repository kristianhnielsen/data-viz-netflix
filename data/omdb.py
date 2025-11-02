from urllib.parse import quote_plus, urljoin

import requests


class OMDB_API:
    def __init__(self):
        self.base_url = "http://www.omdbapi.com/"
        self.api_keys = [
            "f51ea6c7",
            "e3039e27",
            "274f3ed2",
            "2b7ddacc",
            "ca7ca816",
            "1ecc4fba",
            "f4f9d9",
            "3ef28501",
            "59a95e5",
            "d04899ee",
        ]
        self.api_key_counter = 0

    def fetch_data(self, title: str):
        """Fetch data from OMDB API for a given title."""
        formatted_title = quote_plus(title.lower())
        api_key = self.api_keys[self.api_key_counter]

        url = urljoin(
            self.base_url,
            f"?t={formatted_title}&apikey={api_key}",
        )
        print(url)

        response = requests.get(url)

        if not response.status_code == 200:
            self.api_key_counter += 1
            return self.fetch_data(title)

        return response.json()

    def fetch_data_from_dataset(self, titles: list[str]):
        """Fetch data for a list of titles."""
        results = []
        for title in titles:
            data = self.fetch_data(title)
            if not data:
                print(f"Failed to fetch data for title: {title}")
                continue
            results.append(data)

        return results
