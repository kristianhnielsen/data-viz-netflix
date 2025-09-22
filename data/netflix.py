from dataclasses import dataclass
import pandas as pd
import requests
from urllib.parse import urljoin, quote_plus
import os


class NetflixDataPreprocessor:
    def __init__(self, data: pd.DataFrame, has_omdb_data=False) -> None:
        self.data = data
        self._has_omdb_data = has_omdb_data
        self.process_data()

    def process_data(self):
        self._handle_missing_values()
        self._handle_datetime()

    def get_processed_data(self):
        return self.data

    def _handle_datetime(self):
        self.data["date_added"] = pd.to_datetime(self.data["date_added"].str.strip())
        self.data["month_added"] = self.data["date_added"].dt.month
        self.data["month_name_added"] = self.data["date_added"].dt.month_name()
        self.data["year_added"] = self.data["date_added"].dt.year

    def _handle_missing_values(self):
        self.data["cast"] = self.data["cast"].fillna("No Data")
        self.data["director"] = self.data["director"].fillna("No Data")


class NetflixData:
    def __init__(self, path="data/netflix_titles.csv"):
        self.path = path
        self.omdb_data_path = "data/omdb_data.csv"
        self._has_omdb_data = False
        self.preprocessor = NetflixDataPreprocessor(self.load_data())
        self.data = self.preprocessor.get_processed_data()

    def _merge_omdb_data(self):
        if os.path.exists(self.omdb_data_path):
            omdb_df = pd.read_csv(self.omdb_data_path)
            self.data = self.data.merge(
                omdb_df, left_on="title", right_on="Title", how="left"
            )
            self._has_omdb_data = True
        return self.data

    def load_data(self):
        self.data = pd.read_csv(self.path)
        self._merge_omdb_data()
        return self.data

    def get_data(self):
        return self.data

    def _add_omdb_data(self):
        omdb = OMDB()
        titles = self.data["title"].tolist()
        omdb_data = omdb.fetch_data_from_dataset(titles)
        omdb_df = pd.DataFrame(omdb_data)
        omdb_df.to_csv("data/omdb_data.csv", index=False)
        self.data = self.data.merge(
            omdb_df, left_on="title", right_on="Title", how="left"
        )
        return self.data

    def to_csv(self, path: str):
        self.data.to_csv(path, index=False)
        return


class OMDB:
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


if __name__ == "__main__":
    netflix_data = NetflixData()
    print("Data preprocessing complete and saved to CSV.")
