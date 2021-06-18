import http.client
import json
conn = http.client.HTTPSConnection("imdb-api.com", 443)
payload = ''
headers = {}
apiKey = 'k_duwxdunl'
conn.request("GET", "/en/API/Top250Movies/" + apiKey, payload, headers)
res = conn.getresponse()
data = res.read()

parsed = json.loads(data.decode("utf-8"))
#print(type(parsed['items']))

# Menu for the program
def printMenu():
    print('''---------- MoviePicker ----------
1. Let me search a for a movie
2. Find me something good
3. Watchlist
4. Already seen
''')

# Gets the chice of the user.
def getChoice():
    choice = input('Type a number and press enter: ')
    print()
    if choice == '1':
        searchMovie()
    elif choice == '2':
        print('You chose 2')
    elif choice == '3':
        print('You chose 3')
    elif choice == '4':
        print('You chose 4')
    else:
        print('\nPlease choose one of the alternatives in the menu: ')
        getChoice()

def searchMovie():
    title = input("Type the title of the movie and press enter: ")
    conn.request("GET", "/en/API/SearchTitle/" + apiKey + '/' + title.replace(' ', '%20'), payload, headers)
    res = conn.getresponse()
    movies = json.loads(res.read().decode("utf-8"))

    for movie in movies['results']:
        print(movie['title'])

printMenu()
getChoice()