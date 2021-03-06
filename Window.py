from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from CreateInitialLayout import *
from CreateFlowerbedsLayout import *
from CreateMoistureSensorsLayout import *
from CreateSunlightReadingsLayout import *
from CreateRainfallReadingsLayout import *

import sys

class MainWindow(QMainWindow):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system")
        self.stackedLayout = QStackedLayout()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.db")
        self.db.open()
        
        self.setMenuBar = self.menu_bar()
        self.create_windows()
        self.add_windows()
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.central_widget)

    def menu_bar(self):
        self.statusBar()
        self.menubar = self.menuBar()
        
        #view menu
        #creating the flowerbeds action
        self.flowerbedsAction = QAction(QIcon(), "Flowerbeds", self)
        self.flowerbedsAction.setStatusTip("View existing flowerbeds")
        self.flowerbedsAction.triggered.connect(self.flowerbeds_view)

        #creating the moisture sensors action
        self.moistureSensorsAction = QAction(QIcon(), "Moisture Sensors", self)
        self.moistureSensorsAction.setStatusTip("View existing moisture sensors")
        self.moistureSensorsAction.triggered.connect(self.moisture_sensors_view)

        #creating the sunlight readings action
        self.sunlightReadingsAction = QAction(QIcon(), "Sunlight Readings", self)
        self.sunlightReadingsAction.setStatusTip("View past sunlight readings")
        self.sunlightReadingsAction.triggered.connect(self.sunlight_view)

        #creating the rainfall readings action
        self.rainfallReadingsAction = QAction(QIcon(), "Rainfall Readings", self)
        self.rainfallReadingsAction.setStatusTip("View past rainfall readings")
        self.rainfallReadingsAction.triggered.connect(self.rainfall_view)

        #creating the volumetrics action
        self.volumetricsAction = QAction(QIcon(), "Volumetrics", self)
        self.volumetricsAction.setStatusTip("View system volumetrics")
        self.volumetricsAction.triggered.connect(self.temp)

        #adding actions to the view menu
        self.viewMenu = self.menubar.addMenu("View")
        self.viewMenu.addAction(self.flowerbedsAction)
        self.viewMenu.addAction(self.moistureSensorsAction)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.sunlightReadingsAction)
        self.viewMenu.addAction(self.rainfallReadingsAction)
        self.viewMenu.addSeparator()
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
        self.editMenu.addSeparator()
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
        self.aboutAction.setStatusTip("About the program")
        self.aboutAction.triggered.connect(self.temp)

        self.helpAction = QAction(QIcon(), "Help", self)
        self.helpAction.setStatusTip("Help")
        self.helpAction.triggered.connect(self.temp)

        #adding actions to the options menu
        self.helpMenu = self.menubar.addMenu("Help")
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addAction(self.helpAction)


    def temp():
        pass

    def create_windows(self):
        self.initial_layout_widget = InitialLayoutWindow()
        self.flowerbeds_layout_widget = FlowerbedsWindow()
        self.moisture_sensors_layout_widget = MoistureSensorsWindow()
        self.sunlight_layout_widget = SunlightWindow()
        self.rainfall_layout_widget = RainfallWindow()

    def add_windows(self):
        self.stackedLayout.addWidget(self.initial_layout_widget)
        self.stackedLayout.addWidget(self.flowerbeds_layout_widget)   
        self.stackedLayout.addWidget(self.moisture_sensors_layout_widget)
        self.stackedLayout.addWidget(self.sunlight_layout_widget)
        self.stackedLayout.addWidget(self.rainfall_layout_widget)

    def flowerbeds_view(self):
        self.stackedLayout.setCurrentIndex(1)

    def moisture_sensors_view(self):
        self.stackedLayout.setCurrentIndex(2)

    def sunlight_view(self):
        self.stackedLayout.setCurrentIndex(3)

    def rainfall_view(self):
        self.stackedLayout.setCurrentIndex(4)
        
        
    
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    window.resize(600,350)
    application.exec_()
    
