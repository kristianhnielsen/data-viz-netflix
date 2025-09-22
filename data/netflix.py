from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import requests
from urllib.parse import urljoin, quote_plus


@dataclass
class NetflixDataConfig:
    netflix_titles_path: Path | str
    omdb_path: Path | str | None = None

    def __post_init__(self):
        if isinstance(self.netflix_titles_path, str):
            self.netflix_titles_path = Path(self.netflix_titles_path)
        if isinstance(self.omdb_path, str):
            self.omdb_path = Path(self.omdb_path)
        self.has_omdb = self.omdb_path is not None and self.omdb_path.exists()


class Preprocessor(ABC):
    @abstractmethod
    def process_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass


class NetflixDataPreprocessor(Preprocessor):
    def process_data(self, data: pd.DataFrame):
        self.data = data
        self._handle_missing_values()
        self._handle_datetime()
        return data

    def _handle_datetime(self):
        self.data["date_added"] = pd.to_datetime(self.data["date_added"].str.strip())
        self.data["month_added"] = self.data["date_added"].dt.month
        self.data["month_name_added"] = self.data["date_added"].dt.month_name()
        self.data["year_added"] = self.data["date_added"].dt.year

    def _handle_missing_values(self):
        self.data["cast"] = self.data["cast"].fillna("No Data")
        self.data["director"] = self.data["director"].fillna("No Data")

    def _pick_a_country(self, countries: str):
        if pd.isna(countries) or countries.strip() == "":
            return "No Data"
        return countries.split(",")[0].strip()


class NetflixData:
    def __init__(self, config: NetflixDataConfig, preprocessor: Preprocessor):
        self.config = config
        self.data = preprocessor.process_data(self._load_data())

    def to_csv(self, path: str):
        self.data.to_csv(path, index=False)
        return

    def _load_data(self):
        self.data = pd.read_csv(self.config.netflix_titles_path)
        if self.config.has_omdb and self.config.omdb_path:
            omdb_data = pd.read_csv(self.config.omdb_path)
            self._merge_omdb_data(omdb_data=omdb_data)
        return self.data

    def _merge_omdb_data(self, omdb_data: pd.DataFrame):
        self.data = self.data.merge(
            omdb_data, left_on="title", right_on="Title", how="left"
        )
        return self.data


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


if __name__ == "__main__":
    config = NetflixDataConfig(
        netflix_titles_path="data/netflix_titles.csv", omdb_path="data/omdb_data.csv"
    )
    preprocessor = NetflixDataPreprocessor()

    netflix_data = NetflixData(config=config, preprocessor=preprocessor)
    data = netflix_data.data
    print(data.columns)
    print(data.head())
