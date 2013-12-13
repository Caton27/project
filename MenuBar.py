from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

def menu_bar(self):
    self.statusBar()
    self.menubar = self.menuBar()
    
    #view menu
    #creating the flowerbeds action
    self.flowerbedsAction = QAction(QIcon(), "Flowerbeds", self)
    self.flowerbedsAction.setStatusTip("View existing flowerbeds")
    self.flowerbedsAction.triggered.connect(self.temp)

    #creating the moisture sensors action
    self.moistureSensorsAction = QAction(QIcon(), "Moisture Sensors", self)
    self.moistureSensorsAction.setStatusTip("View existing moisture sensors")
    self.moistureSensorsAction.triggered.connect(self.temp)

    #creating the sunlight readings action
    self.sunlightReadingsAction = QAction(QIcon(), "Sunlight Readings", self)
    self.sunlightReadingsAction.setStatusTip("View past sunlight readings")
    self.sunlightReadingsAction.triggered.connect(self.temp)

    #creating the rainfall readings action
    self.rainfallReadingsAction = QAction(QIcon(), "Rainfall Sensors", self)
    self.rainfallReadingsAction.setStatusTip("View past rainfall readings")
    self.rainfallReadingsAction.triggered.connect(self.temp)

    #creating the volumetrics action
    self.volumetricsAction = QAction(QIcon(), "Volumetrics", self)
    self.volumetricsAction.setStatusTip("View system volumetrics")
    self.volumetricsAction.triggered.connect(self.temp)

    #adding actions to the view menu
    self.viewMenu = self.menubar.addMenu("View")
    self.viewMenu.addAction(self.flowerbedsAction)
    self.viewMenu.addAction(self.moistureSensorsAction)
    self.viewMenu.addAction(self.sunlightReadingsAction)
    self.viewMenu.addAction(self.rainfallReadingsAction)
    self.viewMenu.addAction(self.volumetricsAction)


    #edit menu
    #creating the plants action
    self.plantsAction = QAction(QIcon(), "Plants", self)
    self.plantsAction.setStatusTip("Edit plants")
    self.plantsAction.triggered.connect(self.temp)

    #creating the relationships action
    self.relationshipsAction = QAction(QIcon(), "Relationships", self)
    self.relationshipsAction.setStatusTip("Edit existing relationships")
    self.relationshipsAction.triggered.connect(self.temp)

    #creating the new hardware action
    self.newHardwareAction = QAction(QIcon(), "New Hardware", self)
    self.newHardwareAction.setStatusTip("Add new hardware to the system")
    self.newHardwareAction.triggered.connect(self.temp)

    #adding actions to the edit menu
    self.editMenu = self.menubar.addMenu("Edit")
    self.editMenu.addAction(self.plantsAction)
    self.editMenu.addAction(self.relationshipsAction)
    self.editMenu.addAction(self.newHardwareAction)


    #options menu
    #creating the queries action
    self.queriesAction = QAction(QIcon(), "Queries", self)
    self.queriesAction.setStatusTip("Input custom queries")
    self.queriesAction.triggered.connect(self.temp)

    #adding actions to the options menu
    self.optionsMenu = self.menubar.addMenu("Options")
    self.optionsMenu.addAction(self.queriesAction)


    #help menu
    #creating the about {program name} action
    self.aboutAction = QAction(QIcon(), "About", self)
    self.aboutAction.setStatusTip("Input custom queries")
    self.aboutAction.triggered.connect(self.temp)

    self.helpAction = QAction(QIcon(), "Help", self)
    self.helpAction.setStatusTip("Input custom queries")
    self.helpAction.triggered.connect(self.temp)

    #adding actions to the options menu
    self.helpMenu = self.menubar.addMenu("Help")
    self.helpMenu.addAction(self.aboutAction)
    self.helpMenu.addAction(self.helpAction)

