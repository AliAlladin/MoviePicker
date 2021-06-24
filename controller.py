import json
import random
from apiCommunicator import *
from listHandler import *

class controller:
    def __init__(self):
        self.apiComunicator = apiCommunicator()
        self.listHandler = listHandler()

    # Returns a random movie from either top250 or popular
    def getRandomMovie(self, apiName):
        # global movies
        # if apiName == 'top250':
        #    movies = api.getTop250()
        # elif apiName == 'popular':
        #    movies = api.getPopular()

        with open('./top250.json') as top250:
            top250Movies = json.loads(top250.read())

        movie = random.choice(top250Movies['items'])

        if not self.listHandler.alreadyInList('seen.json', movie) and not self.listHandler.alreadyInList('watchlist.json', movie):
            return movie
        else:
            self.getRandomMovie(apiName)

    # Returns movies from 'seen'
    def getAlreadySeen(self):
        return self.listHandler.getList('seen.json')

    # Returns movies in 'watchlist'
    def getWatchlist(self):
        return self.listHandler.getList('watchlist.json')

    # Adds movie to 'watchlist'
    def addToWatchlist(self, movie):
        self.listHandler.addToJson('watchlist.json', movie)

    # Adds movie to 'seen'
    def addToSeen(self, movie):
        self.listHandler.addToJson('seen.json', movie)

    # Deletes movie from 'watchlist' provided the id of the movie
    def removeFromWatchList(self, id):
        self.listHandler.deleteFromJson('watchlist.json', id)

    # Deletes movie from 'seen' provided the id of the movie
    def removeFromSeen(self, id):
        self.listHandler.deleteFromJson('seen.json', id)


    def getTrailerLink(self, id):
        return self.apiComunicator.getTrailer(id)