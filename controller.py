import random
import webbrowser

from apiCommunicator import *
from listHandler import *

class controller:
    def __init__(self):
        self.apiComunicator = apiCommunicator()
        self.listHandler = listHandler()

    # Returns a random movie from either top250 or popular
    def getRandomMovie(self, apiName):
        global movies
        if apiName == 'top250':
           movies = self.apiComunicator.getTop250()
        elif apiName == 'popular':
           movies = self.apiComunicator.getPopular()

        movie = random.choice(movies)

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

    def playTrailer(self, movie):
        try:
            link = self.getTrailerLink(movie['id'])
            print(link)
            webbrowser.open(link)
        except NameError:
            pass