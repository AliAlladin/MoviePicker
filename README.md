# MoviePicker
MoviePicker is a small application made with Python 3 that runs on your computer and recommends you movies with the help of the [IMDb-api](https://imdb-api.com). The GUI for the application has been made with the [PyQt5](https://pypi.org/project/PyQt5/) toolkit and [Qt designer](https://www.qt.io/design). 

## Installation
### Mac OS
1. Download "MoviePicker.app.zip" from [releases](https://github.com/AliAlladin/MoviePicker/releases/tag/Mac).
2. Unzip the folder.
3. Run the MoviePicker application by double clicking on it.

### Windows
1. Download "MoviePicker.zip" from [releases](https://github.com/AliAlladin/MoviePicker/releases/tag/Windows).
2. Unzip the folder.
3. Run the MoviePicker application by double clicking on it.

## Usage
![start screen](/Screenshots/start_screen.png)

When you start the application you will be greeted with the start screen. Here you can choose wether you want to get movie recomendations from the Top 250 or Most popular list in the Imdb-database. There are also two buttons in the top right corner through which you can access your lists of alread seen movies and watchlist respectively.

![movie screen](/Screenshots/movie_screen.png)

Independent of whether you chose "Top 250" or "Most Popular" the movies will be presented on the same page. Along with some information about the movie there's also a link to the trailer that opens in your browser on YouTube. There are also three buttons on this page, "Already seen" that adds movie to "Seen" and suggests you a new movie, "Add to watchlist" that adds the movie to your watchlist and suggests you a new movie and finally "new suggestion" that simply suggests another movie. Movies that have been added to "seen" or "watchlist" won't be suggested again unless you remove them from the list. If you want to return to the start-screen you can do so by clicking the "logo" in the top-left corner.

![list screen](/Screenshots/list_screen.png)

Finally we have the lists that can be accessed with their respective buttons. You can scroll through the list to get an overview of the movies and if you want to delete a movie from the list it can be done by simply clicking on the X button.

## Disclaimer
- The API-key used belongs to a free account which means that you can only make 100 calls/day.
- The application has not been tested on windows but should run just as well as on Mac OS as an executable application (.exe file).
