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
        self._drop_cols()
        self._rename_cols()

        self._handle_datetime()
        self._handle_missing_values()
        self._cast_types()
        return self.data

    def _rename_cols(self):
        self.data.rename(
            columns={
                "Poster": "poster",
                "imdbVotes": "imdb_votes",
                "imdbRating": "imdb_rating",
                "imdbID": "imdb_id",
                "Metascore": "metascore",
                "Metascore": "metascore",
                "Actors": "cast",
                "Awards": "awards",
                "Language": "language",
                "Genre": "genre",
                "country": "country_secondary",
                "Country": "country_primary",
                "totalSeasons": "seasons",
                "Released": "release_date",
                "Runtime": "runtime",
            },
            inplace=True,
        )

    def _drop_cols(self):
        self.data.drop(
            columns=[
                "Response",
                "Error",
                "DVD",
                "BoxOffice",
                "Production",
                "Website",
                "Title",
                "Rated",
                "Director",
                "Writer",
                "cast",
                "Type",
                "Plot",
                "Ratings",
                "date_added",
                "show_id",
                "duration",
            ],
            inplace=True,
        )

    def _handle_datetime(self):
        self.data["release_date"] = pd.to_datetime(self.data["release_date"])
        self.data["release_year"] = self.data["release_date"].dt.year
        self.data["release_month"] = self.data["release_date"].dt.month

    def _handle_missing_values(self):
        self.data["cast"] = self.data["cast"].fillna("No Data")
        self.data["director"] = self.data["director"].fillna("No Data")

    def _cast_types(self):
        self.data["release_year"] = self.data["release_year"].fillna(0)
        self.data["release_month"] = self.data["release_month"].fillna(0)
        self.data["release_year"] = self.data["release_year"].astype(int)
        self.data["release_month"] = self.data["release_month"].astype(int)
        # Check if has OMDB data by checking if data has the column "imdbVotes"
        has_omdb = "imdbVotes" in self.data.columns

        if has_omdb:
            # imdbVotes
            self.data["imdbVotes"] = self.data["imdbVotes"].str.split(",").str.join("")
            self.data["imdbVotes"] = self.data["imdbVotes"].fillna(0)
            self.data["imdbVotes"] = self.data["imdbVotes"].astype(int, errors="ignore")

            # Metascore
            self.data["Metascore"] = self.data["Metascore"].astype(int, errors="ignore")


class NetflixData:
    def __init__(self, config: NetflixDataConfig, preprocessor: Preprocessor):
        self.config = config

        self.data = self._load_data()
        self.data = preprocessor.process_data(self.data)

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
