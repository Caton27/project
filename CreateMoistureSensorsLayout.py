from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3
import sys
import datetime

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
        self.timeframeComboBox.currentIndexChanged.connect(self.select_timeframe)


        self.layout1.addWidget(self.moistureSensorsLabel,0,1)
        self.layout1.addWidget(self.moistureSensorsComboBox,0,2)
        self.layout1.addWidget(self.timeframeLabel,1,1)
        self.layout1.addWidget(self.timeframeComboBox,1,2)
        self.layout1.setAlignment(Qt.AlignTop)

        #layout 2
        self.moistureSensorsTableView = QTableView()
        self.currentMoistureSensorsID = self.moistureSensorsComboBox.currentIndex() + 3
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

        self.moistureSensorsTableView.setFixedWidth(434)
        self.moistureSensorsTableView.setMinimumHeight(115)
        
        self.layout2.addWidget(self.moistureSensorsTableView)
        self.layout2.setAlignment(Qt.AlignLeft)
        self.layout2.setAlignment(Qt.AlignTop)

        #links
        self.infoFont = QFont()
        self.infoFont.setPointSize(8)
        
        self.get_linked()
        self.flowerbedLinks.setFont(self.infoFont)
        self.flowerbedLinks.setAlignment(Qt.AlignBottom)
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
        self.moistureSensorsQuery.prepare("""SELECT
                                       date as "Date",
                                       time as "Time",
                                       reading as "Reading",
                                       averageReading as "Average Reading"
                                       FROM Reading
                                       WHERE SensorID = ?""")
        self.moistureSensorsQuery.addBindValue(self.currentMoistureSensorsID)
        self.moistureSensorsQuery.exec_()
        self.moistureSensorsModel.setQuery(self.moistureSensorsQuery)
        self.moistureSensorsTableView.setModel(self.moistureSensorsModel)
        self.get_linked()

    def select_timeframe(self):
        #datetime & PyQtSql
        self.currentTimeframe = self.timeframeComboBox.currentIndex()
        if self.currentTimeframe == 0:
            self.comparisonDate = datetime.timedelta(1)
        elif self.currentTimeframe == 1:
            self.comparisonDate = datetime.timedelta(7)
        elif self.currentTimeframe == 2:
            self.comparisonDate = datetime.timedelta(30)
        elif self.currentTimeframe == 3:
            self.comparisonDate = datetime.timedelta(183)
        elif self.currentTimeframe == 4:
            self.comparisonDate = datetime.timedelta(365)
        elif self.currentTimeframe == 5:
            self.comparisonDate = datetime.timedelta(99999)
        else:
            pass
        self.moistureSensorsQuery.prepare("""SELECT
                                       date as "Date",
                                       time as "Time",
                                       reading as "Reading",
                                       averageReading as "Average Reading"
                                       FROM Reading
                                       WHERE SensorID = ?""")
        self.moistureSensorsQuery.addBindValue(self.currentMoistureSensorsID)
        self.moistureSensorsQuery.exec_()
        self.moistureSensorsModel.setQuery(self.moistureSensorsQuery)
        self.moistureSensorsTableView.setModel(self.moistureSensorsModel)
        

#works initially, but doesn't update when self.currentMoistureSensorID is changed
    def get_linked(self):
        with sqlite3.connect("FlowerbedDatabase.db") as db2:
            self.cursor = db2.cursor()
            values = (self.currentMoistureSensorsID,)
            self.cursor.execute("select flowerbedID from Sensor where sensorID = ?",values)
            for each in self.cursor.fetchall():
                for each in each:
                    self.linked1 = each
        self.flowerbedLinks = QLabel("""This moisture sensor is currently linked to flowerbed number {0}.""".format(self.linked1))
        
        with sqlite3.connect("FlowerbedDatabase.db") as db2:
            self.cursor = db2.cursor()
            values = (self.linked1,)
            self.cursor.execute("select sensorID from Sensor where flowerbedID = ?",values)
            temp = self.cursor.fetchall()
            self.linked2 = []
            for each in temp:
                for each in each:
                    if str(each) != str(self.currentMoistureSensorsID):
                        self.linked2.append(each)
        self.moistureSensorLinks = QLabel("Moisture sensor numbers {0} and {1} are also linked to flowerbed number {2}.".format(self.linked2[0],self.linked2[1],self.linked1))

    
    def temp(self):
        pass


if __name__ == "__main__":
    application = QApplication(sys.argv)
    moistureSensorsWindow = MoistureSensorsWindow()
    moistureSensorsWindow.show()
    moistureSensorsWindow.raise_()
    moistureSensorsWindow.resize(500,500)
    application.exec_()
