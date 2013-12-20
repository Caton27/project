from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3
import sys

class FlowerbedsWindow(QMainWindow):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system - Flowerbeds")
        self.stackedLayout = QStackedLayout()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.db")
        self.db.open()

        self.create_flowerbeds_layout()
        self.flowerbeds_layout_widget.setMinimumSize(QSize(800,450))
        self.stackedLayout.addWidget(self.flowerbeds_layout_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.central_widget)
        

    def create_flowerbeds_layout(self):
        CurrentFlowerbedID = 1
        with sqlite3.connect("FlowerbedDatabase.db") as db2:
            self.cursor = db2.cursor()
            values = (CurrentFlowerbedID,)
            self.cursor.execute("select * from Plant where flowerbedID = ?", values)
            numPlants = len(self.cursor.fetchall())
            self.cursor.execute("select * from Operation where flowerbedID = ?", values)
            numOperations = len(self.cursor.fetchall())
            
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
        maxHeight1 = 115 + 30 * (numPlants - 3)
        self.flowerbedQuery = QSqlQuery()
        self.flowerbedQuery.prepare("""SELECT
                                       plantGrowing as "Plant",
                                       datePlanted as "Date Planted",
                                       waterNeed as "Water Need"
                                       FROM Plant
                                       WHERE FlowerbedID = ?""")
        self.flowerbedQuery.addBindValue(CurrentFlowerbedID)
        self.flowerbedQuery.exec_()
        self.flowerbedModel = QSqlQueryModel()
        self.flowerbedModel.setQuery(self.flowerbedQuery)
        self.flowerbedTableView = QTableView()
        self.flowerbedTableView.setModel(self.flowerbedModel)

        self.flowerbedTableView.setFixedWidth(334)
        self.flowerbedTableView.setMinimumHeight(112)
        self.flowerbedTableView.setMaximumHeight(maxHeight1)
        
        self.layout2.addWidget(self.flowerbedTableView)
        self.layout2.setAlignment(Qt.AlignLeft)
        self.layout2.setAlignment(Qt.AlignTop)


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
        maxHeight2 = 115 + 30 * (numOperations - 3)
        self.operationQuery = QSqlQuery()
        self.operationQuery.prepare("""SELECT
                                       Operation.date as "Date",
                                       Operation.time as "Time",
                                       Operation.duration as "Duration (s)",
                                       Operation.amount as "Amount (L)",
                                       Operation.cost as "Cost (£)",
                                       Reading.reading(readingBeforeID) as "1st Reading",
                                       Reading.reading(readingAfterID) as "2nd Reading"
                                       FROM Operation, Reading
                                       WHERE Operation.FlowerbedID = ?""")
        self.operationQuery.addBindValue(CurrentFlowerbedID)
        self.operationQuery.exec_()
        self.operationModel = QSqlQueryModel()
        self.operationModel.setQuery(self.operationQuery)
        self.operationTableView = QTableView()
        self.operationTableView.setModel(self.operationModel)

        self.operationTableView.setFixedWidth(724)
        self.operationTableView.setMinimumHeight(112)
        self.operationTableView.setMaximumHeight(maxHeight2)
        
        self.layout4.addWidget(self.operationTableView)
        self.layout4.setAlignment(Qt.AlignLeft)
        self.layout4.setAlignment(Qt.AlignTop)

        
        #flowerbed links
        linked = ["x","y","z"]
        self.flowerbedLinks = QLabel("This flowerbed is currently linked to moisture sensors number {0}, {1} and {2}.".format(linked[0],linked[1],linked[2]))
        self.infoFont = QFont()
        self.infoFont.setPointSize(8)
        self.flowerbedLinks.setFont(self.infoFont)
        self.flowerbedLinks.setAlignment(Qt.AlignBottom)
        
        #add layouts
        self.flowerbeds_layout.addLayout(self.layout1)
        self.flowerbeds_layout.addLayout(self.layout2)
        self.flowerbeds_layout.addLayout(self.layout3)
        self.flowerbeds_layout.addLayout(self.layout4)
        self.flowerbeds_layout.addWidget(self.flowerbedLinks)

        self.flowerbeds_layout_widget = QWidget()
        self.flowerbeds_layout_widget.setLayout(self.flowerbeds_layout)

        return self.flowerbeds_layout_widget

    def temp(self):
        pass


if __name__ == "__main__":
    application = QApplication(sys.argv)
    flowerbedsWindow = FlowerbedsWindow()
    flowerbedsWindow.show()
    flowerbedsWindow.raise_()
    application.exec_()
