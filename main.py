import json
import random

from apiCommunicator import api
from listHandler import listHandler

# Menu for the program
def printMenu():
    print('''
---------- MoviePicker ----------
1. Let me search a for a movie
2. Find me something good
3. Watchlist
4. Already seen
''')

# Gets the choice of the user.
def getChoice():
    choice = input('Type a number and press enter: ')
    print()

    if choice == '1':
        title = input("Type the title of the movie and press enter: ")
        movies = api.searchMovie(title)
        for movie in movies:
            print(movie)
    elif choice == '2':
        findSomethingGood()
    elif choice == '3':
        print('You chose 3')
    elif choice == '4':
        print('You chose 4')
    else:
        print('\nPlease choose one of the alternatives in the menu: ')
        getChoice()

# Recommends the user random movies from the top 250.
def findSomethingGood():
    while(True):
        movie = getRandomMovie()
        if not listHandler.alreadyInList('seen.json', movie) and not listHandler.alreadyInList('watchlist.json', movie):
            print(movie)
        else:
            findSomethingGood()

        choice = input('Already seen this movie? (yes/no): ')
        if choice == 'yes':
            listHandler.addToJson('seen.json', movie)
            continue
        elif choice == 'no':
            choice = input('Want add this to your watchlist? (yes/no): ')
            if choice == 'yes':
                listHandler.addToJson('watchlist.json', movie)
                print('Added to your watchlist!\n')

            choice = input('Want another recommendation? (yes/no): ')
            if choice == 'yes':
                continue
            elif choice == 'no':
                break

def getRandomMovie():
    # top250Movies = api.getTop250();
    with open('./top250.json') as top250:
        top250Movies = json.loads(top250.read())

    movie = random.choice(top250Movies['items'])

    if not listHandler.alreadyInList('seen.json', movie) and not listHandler.alreadyInList('watchlist.json', movie):
        return movie
    else:
        getRandomMovie()

    # return random.choice(top250Movies)

def main():
    while(True):
        printMenu()
        getChoice()

if __name__ == "__main__":
    main()