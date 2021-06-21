# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color : #012940;")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Sweden))
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 50, 1000, 280))
        self.stackedWidget.setObjectName("stackedWidget")

        #----------------------- Start Page ---------------------------#
        self.start = QtWidgets.QWidget()
        self.start.setObjectName("start")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.start)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 80, 252, 116))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # "Top 250" button
        self.top250Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.top250Button.setMinimumSize(QtCore.QSize(250, 50))
        self.top250Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.top250Button.setStyleSheet("QPushButton {\n"
                                        "    background-color: #049DBF;\n"
                                        "    color: white;\n"
                                        "    font: bold 18pt \"Avenir\";\n"
                                        "    border-radius: 25px;\n"
                                        "    margin-right: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #058ba8;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #025373;\n"
                                        "}")
        self.top250Button.setObjectName("top250Button")
        self.top250Button.clicked.connect(lambda: self.goToMovies('top250'))

        self.verticalLayout.addWidget(self.top250Button)

        # "Most popular" button
        self.mostPopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mostPopButton.setEnabled(True)
        self.mostPopButton.setMinimumSize(QtCore.QSize(250, 50))
        self.mostPopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mostPopButton.setStyleSheet(   "QPushButton {\n"
                                            "    background-color: #A60D70;\n"
                                            "    color: white;\n"
                                            "    font: bold 18pt \"Avenir\";\n"
                                            "    border-radius: 25px;\n"
                                            "    margin-right: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: #960c66;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #87095b;\n"
                                            "}")
        self.mostPopButton.setObjectName("mostPopButton")
        self.mostPopButton.clicked.connect(lambda: self.goToMovies('popular'))
        self.verticalLayout.addWidget(self.mostPopButton)

        self.stackedWidget.addWidget(self.start)
        #--------------------------------------------------------------#

        #---------------------- Movies Page ---------------------------#
        self.movies = QtWidgets.QWidget()
        self.movies.setObjectName("movies")

        # "Crew" label
        self.crewLabel = QtWidgets.QLabel(self.movies)
        self.crewLabel.setGeometry(QtCore.QRect(220, 110, 50, 30))
        self.crewLabel.setStyleSheet("color : white;\n"
                                     "font: bold 18pt \"Avenir\";")
        self.crewLabel.setObjectName("crewLabel")

        # IMDb-rating
        self.imdbRating = QtWidgets.QLabel(self.movies)
        self.imdbRating.setGeometry(QtCore.QRect(340, 70, 450, 30))
        self.imdbRating.setStyleSheet("color : white;\n"
                                      "font: 18pt \"Avenir\";")
        self.imdbRating.setObjectName("imdbRating")

        # Title
        self.title = QtWidgets.QLabel(self.movies)
        self.title.setGeometry(QtCore.QRect(220, 20, 700, 40))
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setStyleSheet("color : white;\n"
                                 "font: bold 24pt \"Avenir\";")
        self.title.setObjectName("title")


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.movies)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 210, 761, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttons_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttons_2.setContentsMargins(0, 0, 0, 0)
        self.buttons_2.setObjectName("buttons_2")

        # "Already seen" button
        self.addToSeenButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToSeenButton.setMinimumSize(QtCore.QSize(0, 50))
        self.addToSeenButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addToSeenButton.setStyleSheet( "QPushButton {\n"
                                            "    background-color: #049DBF;\n"
                                            "    color: white;\n"
                                            "    font: bold 18pt \"Avenir\";\n"
                                            "    border-radius: 25px;\n"
                                            "    margin-right: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: #058ba8;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #025373;\n"
                                            "}")
        self.addToSeenButton.setObjectName("addToSeenButton")
        self.addToSeenButton.clicked.connect(self.addToSeen)
        self.buttons_2.addWidget(self.addToSeenButton)

        # "Add to watchlist" button
        self.addToWatchlistButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addToWatchlistButton.setMinimumSize(QtCore.QSize(0, 50))
        self.addToWatchlistButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addToWatchlistButton.setStyleSheet("QPushButton {\n"
                                                "    background-color: #049DBF;\n"
                                                "    color: white;\n"
                                                "    font: bold 18pt \"Avenir\";\n"
                                                "    border-radius: 25px;\n"
                                                "    margin-right: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #058ba8;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #025373;\n"
                                                "}")
        self.addToWatchlistButton.setObjectName("addToWatchlistButton")
        self.addToWatchlistButton.clicked.connect(self.addToWatchList)
        self.buttons_2.addWidget(self.addToWatchlistButton)

        # "New suggestion" button
        self.newSuggestionButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.newSuggestionButton.setMinimumSize(QtCore.QSize(0, 50))
        self.newSuggestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newSuggestionButton.setStyleSheet( "QPushButton {\n"
                                                "    background-color: #049DBF;\n"
                                                "    color: white;\n"
                                                "    font: bold 18pt \"Avenir\";\n"
                                                "    border-radius: 25px;\n"
                                                "    margin-right: 5px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #058ba8;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #025373;\n"
                                                "}")
        self.newSuggestionButton.setObjectName("newSuggestionButton")
        self.buttons_2.addWidget(self.newSuggestionButton)
        self.newSuggestionButton.clicked.connect(self.newSuggestion)

        # Crew list
        self.crewList = QtWidgets.QLabel(self.movies)
        self.crewList.setGeometry(QtCore.QRect(280, 110, 450, 30))
        self.crewList.setStyleSheet("color : white;\n"
                                    "font: 18pt \"Avenir\";")
        self.crewList.setObjectName("crewList")

        # Poster image
        self.posterImage = QtWidgets.QLabel(self.movies)
        self.posterImage.setGeometry(QtCore.QRect(20, 20, 180, 240))
        self.posterImage.setScaledContents(True)
        self.posterImage.setObjectName("posterImage")

        # Rating label
        self.ratingLabel = QtWidgets.QLabel(self.movies)
        self.ratingLabel.setGeometry(QtCore.QRect(220, 70, 110, 30))
        self.ratingLabel.setStyleSheet("color : white;\n"
                                        "font: bold 18pt \"Avenir\";")
        self.ratingLabel.setObjectName("ratingLabel")

        # Trailer link
        self.trailerLink = QtWidgets.QPushButton(self.movies)
        self.trailerLink.setGeometry(QtCore.QRect(220, 150, 321, 32))
        self.trailerLink.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trailerLink.setStyleSheet("QPushButton {\n"
                                        "    color : #04C4D9;\n"
                                        "    font: 18pt \"Avenir\";\n"
                                        "    text-align:left;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    font: 19pt \"Avenir\";\n"
                                        "}")
        self.trailerLink.setFlat(True)
        self.trailerLink.setObjectName("trailerLink")

        self.stackedWidget.addWidget(self.movies)
        #--------------------------------------------------------------#

        #------------------------- Lists ------------------------------#
        self.lists = QtWidgets.QWidget()
        self.lists.setObjectName("lists")

        self.scrollArea = QtWidgets.QScrollArea(self.lists)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1000, 280))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.list = QtWidgets.QWidget()
        self.list.setGeometry(QtCore.QRect(0, 0, 998, 278))
        self.list.setObjectName("list")

        self.listItem = QtWidgets.QWidget(self.list)
        self.listItem.setGeometry(QtCore.QRect(0, 0, 1000, 80))
        self.listItem.setStyleSheet("")
        self.listItem.setObjectName("listItem")

        self.listItemImage = QtWidgets.QLabel(self.listItem)
        self.listItemImage.setGeometry(QtCore.QRect(20, 10, 50, 60))
        self.listItemImage.setStyleSheet("background-color:red;")
        self.listItemImage.setText("")
        self.listItemImage.setPixmap(QtGui.QPixmap("studentplakat.jpg"))
        self.listItemImage.setScaledContents(True)
        self.listItemImage.setObjectName("listItemImage")

        self.listItemRatingLabel = QtWidgets.QLabel(self.listItem)
        self.listItemRatingLabel.setGeometry(QtCore.QRect(90, 40, 111, 30))
        self.listItemRatingLabel.setStyleSheet("color : white;\n"
                                                "font: bold 18pt \"Avenir\";")
        self.listItemRatingLabel.setObjectName("listItemRatingLabel")

        self.listItemTitle = QtWidgets.QLabel(self.listItem)
        self.listItemTitle.setGeometry(QtCore.QRect(90, 10, 821, 31))
        self.listItemTitle.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listItemTitle.setStyleSheet("color : white;\n"
                                        "font: bold 24pt \"Avenir\";")
        self.listItemTitle.setObjectName("listItemTitle")

        self.deleteButton = QtWidgets.QPushButton(self.listItem)
        self.deleteButton.setGeometry(QtCore.QRect(920, 10, 50, 50))
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setStyleSheet("color: white;\n"
                                        "font: 48pt \"Avenir\";")
        self.deleteButton.setFlat(True)
        self.deleteButton.setObjectName("deleteButton")

        self.listItemCrewList = QtWidgets.QLabel(self.listItem)
        self.listItemCrewList.setGeometry(QtCore.QRect(320, 40, 700, 30))
        self.listItemCrewList.setStyleSheet("color : white;\n"
                                            "font: 18pt \"Avenir\";")
        self.listItemCrewList.setObjectName("listItemCrewList")

        self.listItemCrewLabel_2 = QtWidgets.QLabel(self.listItem)
        self.listItemCrewLabel_2.setGeometry(QtCore.QRect(260, 40, 50, 30))
        self.listItemCrewLabel_2.setStyleSheet("color : white;\n"
                                                "font: bold 18pt \"Avenir\";")
        self.listItemCrewLabel_2.setObjectName("listItemCrewLabel_2")

        self.listItemRating = QtWidgets.QLabel(self.listItem)
        self.listItemRating.setGeometry(QtCore.QRect(200, 40, 31, 30))
        self.listItemRating.setStyleSheet("color : white;\n"
                                            "font: 18pt \"Avenir\";")
        self.listItemRating.setObjectName("listItemRating")

        self.scrollArea.setWidget(self.list)
        #--------------------------------------------------------------#

        #------------------------- Menu -------------------------------#
        self.stackedWidget.addWidget(self.lists)
        self.menu = QtWidgets.QWidget(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 1000, 50))
        self.menu.setAutoFillBackground(False)
        self.menu.setStyleSheet("background-color : #011826;")
        self.menu.setObjectName("menu")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.menu)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(690, 0, 291, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.menuButtons_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.menuButtons_2.setContentsMargins(0, 0, 0, 0)
        self.menuButtons_2.setObjectName("menuButtons_2")
        
        self.seenButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.seenButton.setEnabled(True)
        self.seenButton.setMinimumSize(QtCore.QSize(0, 30))
        self.seenButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seenButton.setStyleSheet("QPushButton {\n"
                                        "    background-color: #A60D70;\n"
                                        "    color: white;\n"
                                        "    font: bold 16pt \"Avenir\";\n"
                                        "    border-radius: 15px;\n"
                                        "    margin-right: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #960c66;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #87095b;\n"
                                        "}")
        self.seenButton.setObjectName("seenButton")
        self.seenButton.clicked.connect(lambda: self.goToList('seen'))
        
        self.menuButtons_2.addWidget(self.seenButton)
        self.watchlistButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.watchlistButton.setMinimumSize(QtCore.QSize(0, 30))
        self.watchlistButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.watchlistButton.setStyleSheet("QPushButton {\n"
                                            "    background-color: #A60D70;\n"
                                            "    color: white;\n"
                                            "    font: bold 16pt \"Avenir\";\n"
                                            "    border-radius: 15px;\n"
                                            "    margin-right: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: #960c66;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    background-color: #87095b;\n"
                                            "}")
        self.watchlistButton.setObjectName("watchlistButton")
        self.menuButtons_2.addWidget(self.watchlistButton)
        self.logo = QtWidgets.QPushButton(self.menu)
        self.logo.setGeometry(QtCore.QRect(20, 10, 160, 30))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logo.setStyleSheet("font: 24pt \"Raleway\";\n"
                                "color: white;\n"
                                "text-align:left;")
        self.logo.setFlat(True)
        self.logo.setObjectName("logo")
        self.logo.clicked.connect(self.goToStart)
        #--------------------------------------------------------------#

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.top250Button.setText(_translate("MainWindow", "Top 250"))
        self.mostPopButton.setText(_translate("MainWindow", "Most Popular"))
        self.crewLabel.setText(_translate("MainWindow", "Crew:"))
        self.imdbRating.setText(_translate("MainWindow", "<html><head/><body><p>8.6</p></body></html>"))
        self.title.setText(_translate("MainWindow", "It\'s a Wonderful Life (1946)"))
        self.addToSeenButton.setText(_translate("MainWindow", "Already seen"))
        self.addToWatchlistButton.setText(_translate("MainWindow", "Add to watchlist"))
        self.newSuggestionButton.setText(_translate("MainWindow", "New suggestion"))
        self.crewList.setText(_translate("MainWindow", "<html><head/><body><p>Frank Capra (dir.), James Stewart, Donna Ree</p></body></html>"))
        self.ratingLabel.setText(_translate("MainWindow", "IMDb-rating: "))
        self.trailerLink.setText(_translate("MainWindow", "Watch trailer (opens in YouTube)"))
        self.listItemRatingLabel.setText(_translate("MainWindow", "IMDb-rating:"))
        self.listItemTitle.setText(_translate("MainWindow", "It\'s a Wonderful Life (1946)"))
        self.deleteButton.setText(_translate("MainWindow", "x"))
        self.listItemCrewList.setText(_translate("MainWindow", "Person 1"))
        self.listItemCrewLabel_2.setText(_translate("MainWindow", "Crew:"))
        self.listItemRating.setText(_translate("MainWindow", "8.6"))
        self.seenButton.setText(_translate("MainWindow", "Seen"))
        self.watchlistButton.setText(_translate("MainWindow", "Watchlist"))
        self.logo.setText(_translate("MainWindow", "MoviePicker"))

    def newSuggestion(self, apiName):
        global movie
        movie = getRandomMovie(apiName)
        try:
            self.title.setText(movie['fullTitle'])

            image_url = movie['image']
            image = QtGui.QPixmap()
            image.loadFromData(requests.get(image_url).content)
            self.posterImage.setPixmap(image)

            self.imdbRating.setText(movie['imDbRating'])

            self.crewList.setText(movie['crew'])
        except TypeError:
            print("TypeError")
            self.newSuggestion(apiName)

    def addToSeen(self):
        listHandler.addToJson('seen.json', movie)
        self.newSuggestion()

    def addToWatchList(self):
        listHandler.addToJson('watchlist.json', movie)
        self.newSuggestion()

    def goToMovies(self, apiName):
        self.newSuggestion(apiName)
        self.stackedWidget.setCurrentWidget(self.movies)

    def goToStart(self):
        self.stackedWidget.setCurrentWidget(self.start)

    def goToList(self, list):
        self.stackedWidget.setCurrentWidget(self.lists)


if __name__ == "__main__":
    import sys
    from controller import *

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
