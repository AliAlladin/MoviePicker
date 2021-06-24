import http.client
import json

class apiCommunicator:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("imdb-api.com", 443)
        self.payload = ''
        self.headers = {}
        self.apiKey = 'k_57a3yf8o'

    # Function returns the json of the top 250 movies in the database by connecting to the API.
    def getTop250(self):
        self.conn.request("GET", "/en/API/Top250Movies/" + self.apiKey, self.payload, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        top250 = json.loads(data.decode("utf-8"))
        return top250['items']

    # Function returns the json of the most popular movies in the database by connecting to the API.
    def getPopular(self):
        self.conn.request("GET", "/en/API/MostPopularMovies/" + self.apiKey, self.payload, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        popular = json.loads(data.decode("utf-8"))
        return popular['items']

    # Function returns the youtube-link of the most popular movies in the database by connecting to the API.
    def getTrailer(self, id):
        self.conn.request("GET", "/en/API/YouTubeTrailer/" + self.apiKey + '/' + id, self.payload, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        trailer = json.loads(data.decode("utf-8"))
        return trailer['videoUrl']

    # Function searches for movies in the database by connecting to the API given a title and returns the json of the
    # search result.
    def searchMovie(self, title):
        self.conn.request("GET", "/en/API/SearchTitle/" + self.apiKey + '/' + title.replace(' ', '%20'), self.payload, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        searchResult = json.loads(data.decode("utf-8"))
        return searchResult['results']