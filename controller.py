import json
import random
from apiCommunicator import api
from listHandler import *

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

    # Function returns the json of the 100 most popular movies in the database by connecting to the API.
    def getPopular(self):
        self.conn.request("GET", "/en/API/MostPopularMovies/" + self.apiKey, self.payload, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        popular = json.loads(data.decode("utf-8"))
        return popular['items']

    # Function searches for movies in the database by connecting to the API given a title and returns the json of the
    # search result.
    def searchMovie(self, title):
        self.conn.request("GET", "/en/API/SearchTitle/" + self.apiKey + '/' + title.replace(' ', '%20'), self.payload, self.headers)
        res = self.conn.getresponse()
        data = res.read()
        searchResult = json.loads(data.decode("utf-8"))
        return searchResult['results']

# Instance of the class.
api = apiCommunicator()

import json

class listHandler:
    # Adds movie to the desired list provided name of the json file and the json of the movie.
    def addToJson(self, filename, movie):
        with open('./' + filename) as json_file:
            data = json.load(json_file)
            temp = data['movies']
            temp.append(movie)

        with open('./' + filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    # Function deletes a movie from json file provided the name of the file and the movie json.
    def deleteFromJson(self, filename, id):
        with open('./' + filename) as json_file:
            data = json.load(json_file)

        temp = data['movies']
        for i in range(len(temp)):
            if temp[i]['id'] == id:
                del temp[i]
                break

        with open('./' + filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    def alreadyInList(self, filename, movie):
        with open('./' + filename) as json_file:
            data = json.load(json_file)

        temp = data['movies']
        for i in range(len(temp)):
            if temp[i]['id'] == movie['id']:
                return True

        return False

    def getList(self, filename):
        with open('./' + filename) as json_file:
            data = json.load(json_file)
        return data['movies']

listHandler = listHandler()

# Returns a random movie from either top250 or popular
def getRandomMovie(apiName):
    #global movies
    #if apiName == 'top250':
    #    movies = api.getTop250()
    #elif apiName == 'popular':
    #    movies = api.getPopular()

    with open('./top250.json') as top250:
        top250Movies = json.loads(top250.read())

    movie = random.choice(top250Movies['items'])

    if not listHandler.alreadyInList('seen.json', movie) and not listHandler.alreadyInList('watchlist.json', movie):
        return movie
    else:
        getRandomMovie(apiName)

def getAlreadySeen():
    return listHandler.getList('seen.json')

def getWatchlist():
    return listHandler.getList('watchlist.json')

def removeFromWatchList(id):
    listHandler.deleteFromJson('watchlist.json', id)

def removeFromSeen(id):
    listHandler.deleteFromJson('seen.json', id)