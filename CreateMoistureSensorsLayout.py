from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3
import sys

class MoistureSensorsWindow(QMainWindow):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system - Moisture Sensors")
        self.stackedLayout = QStackedLayout()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.db")
        self.db.open()

        self.create_moisture_sensors_layout()
        self.moisture_sensors_layout_widget.setMinimumSize(QSize(600,350))
        self.stackedLayout.addWidget(self.moisture_sensors_layout_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.central_widget)

        
    def create_moisture_sensors_layout(self):
        with sqlite3.connect("FlowerbedDatabase.db") as db2:
            self.cursor = db2.cursor()
            self.cursor.execute("select sensorID from Sensor where sensorTypeID = 1")
            moistureSensorsList = []
            for each1 in self.cursor.fetchall():
                for each2 in each1:
                    moistureSensorsList.append(each2)

        self.moisture_sensors_layout = QVBoxLayout()

        self.layout1 = QGridLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()

        self.titleFont = QFont()
        self.titleFont.setPointSize(13)
        self.titleFont.setBold(True)

        #layout 1
        self.moistureSensorsLabel = QLabel("Moisture Sensor")
        self.moistureSensorsLabel.setFont(self.titleFont)
        self.moistureSensorsLabel.setFixedWidth(200)

        self.moistureSensorsComboBox = QComboBox()
        for each in moistureSensorsList:
            self.moistureSensorsComboBox.addItem(str(each))
        self.moistureSensorsComboBox.setFixedWidth(30)
        self.moistureSensorsComboBox.currentIndexChanged.connect(self.select_moisture_sensors)

        self.timeframeLabel = QLabel("Timeframe")
        self.timeframeLabel.setFont(self.titleFont)


        self.timeframeComboBox = QComboBox()
        self.timeframeComboBox.addItem("24 hours")
        self.timeframeComboBox.addItem("7 days")
        self.timeframeComboBox.addItem("30 days")
        self.timeframeComboBox.addItem("6 months")
        self.timeframeComboBox.addItem("1 year")
        self.timeframeComboBox.addItem("all time")
        self.timeframeComboBox.setFixedWidth(80)
        self.timeframeComboBox.currentIndexChanged.connect(self.select_moisture_sensors)


        self.layout1.addWidget(self.moistureSensorsLabel,0,1)
        self.layout1.addWidget(self.moistureSensorsComboBox,0,2)
        self.layout1.addWidget(self.timeframeLabel,1,1)
        self.layout1.addWidget(self.timeframeComboBox,1,2)
        self.layout1.setAlignment(Qt.AlignTop)

        #layout 2
        self.moistureSensorsTableView = QTableView()
        self.select_moisture_sensors()

        self.moistureSensorsTableView.setFixedWidth(434)
        self.moistureSensorsTableView.setMinimumHeight(112)
        self.moistureSensorsTableView.setMaximumHeight(self.maxHeight1)
        
        self.layout2.addWidget(self.moistureSensorsTableView)
        self.layout2.setAlignment(Qt.AlignLeft)
        self.layout2.setAlignment(Qt.AlignTop)

        #flowerbed links
        with sqlite3.connect("FlowerbedDatabase.db") as db2:
            self.cursor = db2.cursor()
            values = (self.currentMoistureSensorsID,)
            self.cursor.execute("select flowerbedID from Sensor where sensorID = ?",values)
            temp = self.cursor.fetchall()
            for each in temp:
                for each in each:
                    linked1 = each
        self.flowerbedLinks = QLabel("This moisture sensor is currently linked to flowerbed number {0}.".format(linked1))
        self.infoFont = QFont()
        self.infoFont.setPointSize(8)
        self.flowerbedLinks.setFont(self.infoFont)
        self.flowerbedLinks.setAlignment(Qt.AlignBottom)

        #moisture sensor links
        linked2 = ["y","z"]
        self.moistureSensorLinks = QLabel("Moisture sensor numbers {0} and {1} are also linked to flowerbed number {2}.".format(linked2[0],linked2[1],linked1))
        self.moistureSensorLinks.setFont(self.infoFont)
        self.moistureSensorLinks.setAlignment(Qt.AlignBottom)
        
        #add layouts
        self.moisture_sensors_layout.addLayout(self.layout1)
        self.moisture_sensors_layout.addLayout(self.layout2)
        self.moisture_sensors_layout.addWidget(self.flowerbedLinks)
        self.moisture_sensors_layout.addWidget(self.moistureSensorLinks)

        self.moisture_sensors_layout_widget = QWidget()
        self.moisture_sensors_layout_widget.setLayout(self.moisture_sensors_layout)

        return self.moisture_sensors_layout_widget

    def select_moisture_sensors(self):
        self.currentMoistureSensorsID = self.moistureSensorsComboBox.currentIndex() + 3
        print(self.currentMoistureSensorsID)

        with sqlite3.connect("FlowerbedDatabase.db") as db2:
            self.cursor = db2.cursor()
            values = (self.currentMoistureSensorsID,)
            self.cursor.execute("select * from Reading where sensorID = ?", values)
            self.numOperations = len(self.cursor.fetchall())

        self.maxHeight1 = 115 + 30 * (self.numOperations - 3)
        self.moistureSensorsQuery = QSqlQuery()
        self.moistureSensorsQuery.prepare("""SELECT
                                       date as "Date",
                                       time as "Time",
                                       reading as "Reading",
                                       averageReading as "Average Reading"
                                       FROM Reading
                                       WHERE SensorID = ?""")
        self.moistureSensorsQuery.addBindValue(self.currentMoistureSensorsID)
        self.moistureSensorsQuery.exec_()
        self.moistureSensorsModel = QSqlQueryModel()
        self.moistureSensorsModel.setQuery(self.moistureSensorsQuery)
        self.moistureSensorsTableView.setModel(self.moistureSensorsModel)

        
    def temp(self):
        pass


if __name__ == "__main__":
    application = QApplication(sys.argv)
    moistureSensorsWindow = MoistureSensorsWindow()
    moistureSensorsWindow.show()
    moistureSensorsWindow.raise_()
    application.exec_()
