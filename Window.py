from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class MainWindow(QMainWindow):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system")
        self.stackedLayout = QStackedLayout()
        
        self.setMenuBar = self.menu_bar()
        self.initial_layout_widget = self.create_initial_layout()
        self.initial_layout_widget.setMinimumSize(QSize(500,300))
        self.stackedLayout.addWidget(self.initial_layout_widget)
        

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.central_widget)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.py")
        self.db.open()

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



    def create_initial_layout(self):
        self.initial_layout = QVBoxLayout()

        self.welcomeLabel = QLabel("Welcome")
        self.welcomeFont = QFont()
        self.welcomeFont.setPointSize(20)
        self.welcomeFont.setBold(True)
        self.welcomeLabel.setFont(self.welcomeFont)
        self.welcomeLabel.setAlignment(Qt.AlignHCenter|Qt.AlignBottom)
        
        self.messageLabel = QLabel("Select an option from the menu bar to begin using the program")
        self.messageFont = QFont()
        self.messageFont.setPointSize(10)
        self.messageLabel.setFont(self.messageFont)
        self.messageLabel.setAlignment(Qt.AlignHCenter)

        self.initial_layout.addWidget(self.welcomeLabel)
        self.initial_layout.addWidget(self.messageLabel)

        self.initial_layout_widget = QWidget()
        self.initial_layout_widget.setLayout(self.initial_layout)

        return self.initial_layout_widget



    def create_flowerbeds_layout(self):
        flowerbedList = ["1","2","3","4","5"]
        self.flowerbeds_layout = QVBoxLayout()

        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()

        self.titleFont = QFont()
        self.titleFont.setPointSize(13)
        self.titleFont.setBold(True)
        
        #layout 1
        self.flowerbedLabel = QLabel("Flowerbed")
        self.flowerbedLabel.setFont(self.titleFont)
        self.flowerbedLabel.setFixedWidth(100)

        self.flowerbedsComboBox = QComboBox()
        for each in flowerbedList:
            self.flowerbedsComboBox.addItem(each)
        self.flowerbedsComboBox.setFixedWidth(30)

        self.viewFlowerbedButton = QPushButton("View flowerbed")
        self.viewFlowerbedButton.clicked.connect(self.temp)
        self.viewFlowerbedButton.setFixedWidth(100)

        self.addFlowerbedButton = QPushButton("Add new flowerbed")
        self.addFlowerbedButton.clicked.connect(self.temp)
        self.addFlowerbedButton.setFixedWidth(120)
        
        self.layout1.addWidget(self.flowerbedLabel)
        self.layout1.addWidget(self.flowerbedsComboBox)
        self.layout1.addWidget(self.viewFlowerbedButton)
        self.layout1.addWidget(self.addFlowerbedButton)
        self.layout1.setAlignment(Qt.AlignTop)

        #layout 2
        
        #layout 3
        self.timeframeLabel = QLabel("Timeframe")
        self.timeframeLabel.setFont(self.titleFont)
        self.timeframeLabel.setFixedWidth(100)

        self.timeframeComboBox = QComboBox()
        self.timeframeComboBox.addItem("24 hours")
        self.timeframeComboBox.addItem("7 days")
        self.timeframeComboBox.addItem("30 days")
        self.timeframeComboBox.addItem("6 months")
        self.timeframeComboBox.addItem("1 year")
        self.timeframeComboBox.addItem("all time")
        self.timeframeComboBox.setFixedWidth(80)

        self.layout3.addWidget(self.timeframeLabel)
        self.layout3.addWidget(self.timeframeComboBox)
        self.layout3.setAlignment(Qt.AlignTop)

        #layout 4

        #flowerbed links
        linked = ["x","y","z"]
        self.flowerbedLinks = QLabel("This flowerbed is currently linked to moisture sensors number {0}, {1} and {2}.".format(linked[0],linked[1],linked[2]))
        self.infoFont = QFont()
        self.infoFont.setPointSize(8)
        self.flowerbedLinks.setFont(self.infoFont)
        self.flowerbedLinks.setAlignment(Qt.AlignBottom)
        
        #add layouts
        self.flowerbeds_layout.addLayout(self.layout1)
        #self.flowerbeds_layout.addLayout(self.layout2)
        self.flowerbeds_layout.addLayout(self.layout3)
        #self.flowerbeds_layout.addLayout(self.layout4)
        self.flowerbeds_layout.addWidget(self.flowerbedLinks)

        self.flowerbeds_layout_widget = QWidget()
        self.flowerbeds_layout_widget.setLayout(self.flowerbeds_layout)

        

    def flowerbeds_view(self):
        self.create_flowerbeds_layout()
        self.stackedLayout.addWidget(self.flowerbeds_layout_widget)
        self.stackedLayout.setCurrentIndex(1)
        
    
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
    
