import json
from pathlib import Path

class listHandler:

    # Adds movie to the desired list provided name of the json file and the json of the movie.
    def addToJson(self, filename, movie):
        path = Path('./' + filename)
        with open(path) as json_file:
            data = json.load(json_file)
            temp = data['movies']
            temp.append(movie)

        with open('./' + filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    # Function deletes a movie from json file provided the name of the file and the movie json.
    def deleteFromJson(self, filename, id):
        path = Path('./' + filename)
        with open(path) as json_file:
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
        path = Path('./' + filename)
        with open(path) as json_file:
            data = json.load(json_file)

        return data['movies']