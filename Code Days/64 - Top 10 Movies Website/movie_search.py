import requests
from werkzeug.wrappers import response

class MovieSearch:
    def __init__(self) -> None:
        self.apiKey = "API KEY"
        self.searchEndpoint = "https://api.themoviedb.org/3/search/movie"
        self.params = {
            "api_key": self.apiKey,
            "language": "en-US",
            "query": "",
            "include_adult": "false"
        }
        self.movieID = ""
        self.detailsEndpoint = f"https://api.themoviedb.org/3/movie/{self.movieID}"

    def searchMovie(self, movieTitle):
        self.params["query"] = movieTitle
        response = requests.get(url=self.searchEndpoint, params=self.params)
        data = response.json()
        if data["results"] != []:
            movieData = data["results"]
            return movieData

    def getMovieDetails(self, movieID):
        self.movieID = movieID
        params = {
            "api_key": self.apiKey,
            "language": "en-US",
        }
        response = requests.get(url=self.detailsEndpoint, params=params)
        data = response.json()
        print(data)
