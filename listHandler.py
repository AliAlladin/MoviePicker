import json

# Adds movie to the desired list provided name of the json file and the json of the movie.
def addToJson(filename, movie):
    with open('./' + filename) as json_file:
        data = json.load(json_file)
        temp = data['movies']
        temp.append(movie)

    with open('./' + filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)
