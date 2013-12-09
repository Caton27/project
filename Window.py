from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from PyQt4 import QtGui


import sys

class MainWindow(QMainWindow):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system")
        self.stackedLayout = QStackedLayout()
        self.menu_bar_widget = self.menu_bar()
        self.stackedLayout.addWidget(self.menu_bar_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.central_widget)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.py")
        self.db.open()

    def menu_bar(self):
        flowerbedsAction = QtGui.QAction("Flowerbeds")
        flowerbedsAction.setStatusTip("View existing flowerbeds")
        flowerbedsAction.triggered.connect(self.flowerbeds_layout)

        moistureSensorsAction = QtGui.QAction("Moisture Sensors")
        moistureSensorsAction.setStatusTip("View existing moisture sensors")
        moistureSensorsAction.triggered.connect(self.moisture_sensors_layout)

        self.statusBar()
        
        menubar = self.menuBar()
        viewMenu = menubar.addMenu("View")
        viewMenu.addAction(flowerbedsAction)
        viewMenu.addAction(moistureSensorsAction)
    
##    def create_initial_layout(self):
##        
##    
##    def create_view_flowerbeds_layout(self):
##        self.layout = QVBoxLayout()
##        self.layout1 = QHBoxLayout()
##        self.layout2 = QHBoxLayout()
##        self.layout3 = QHBoxLayout()
##        self.layout4 = QHBoxLayout()
##
##        #create widgets for the first horizontal box layout
##        self.title_label = QLabel("Flowerbeds")
##        self.flowerbedNumber = QWhateverItIs() #drop-down menu
##        self.addNewFlowerbed_button = QPushButton("Add new flowerbed")
##
##        #add widgets to the first horizontal box layout
##        self.layout1.addWidget(self.title_label)
##        self.layout1.addWidget(self.flowerbedNumber)
##        self.layout1.addWidget(self.addNewFlowerbed_button)

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
    
