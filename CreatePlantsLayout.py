from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3
import sys
import datetime

class PlantsWindow(QWidget):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system - Plants")

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.db")
        self.db.open()

        self.create_plants_layout()
        self.setLayout(self.plants_layout)

    def create_plants_layout(self):
        with sqlite3.connect("FlowerbedDatabase.db") as db2:
            self.cursor = db2.cursor()
            self.cursor.execute("select flowerbedID from Flowerbed")
            flowerbedList = []
            for each1 in self.cursor.fetchall():
                for each2 in each1:
                    flowerbedList.append(each2)

        self.plants_layout = QVBoxLayout()
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QGridLayout()
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
            self.flowerbedsComboBox.addItem(str(each))
        self.flowerbedsComboBox.setFixedWidth(30)
        self.flowerbedsComboBox.currentIndexChanged.connect(self.select_flowerbed)

        self.layout1.addWidget(self.flowerbedLabel)
        self.layout1.addWidget(self.flowerbedsComboBox)
        self.layout1.setAlignment(Qt.AlignTop)

        #layout 2
        self.flowerbedTableView = QTableView()
        self.currentFlowerbedID = self.flowerbedsComboBox.currentIndex() + 1
        self.maxHeight = 295
        self.flowerbedQuery = QSqlQuery()
        self.flowerbedQuery.prepare("""SELECT
                                       plantGrowing as "Plant",
                                       datePlanted as "Date Planted",
                                       waterNeed as "Water Need",
                                       notes as "Notes"
                                       FROM Plant
                                       WHERE FlowerbedID = ?""")
        self.flowerbedQuery.addBindValue(self.currentFlowerbedID)
        self.flowerbedQuery.exec_()
        self.flowerbedModel = QSqlTableModel()
        self.flowerbedModel.setQuery(self.flowerbedQuery)
        self.flowerbedModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.flowerbedTableView.setModel(self.flowerbedModel)

        self.flowerbedTableView.setFixedWidth(434)
        self.flowerbedTableView.setMaximumWidth(724)
        self.flowerbedTableView.setMinimumHeight(115)
        self.flowerbedTableView.setMaximumHeight(self.maxHeight)
        
        self.layout2.addWidget(self.flowerbedTableView)
        self.layout2.setAlignment(Qt.AlignLeft)
        self.layout2.setAlignment(Qt.AlignTop)


        #layout 3
        self.addPlantsLabel = QLabel("Add a new plant")
        self.addPlantsLabel.setFont(self.titleFont)
        self.addPlantsLabel.setAlignment(Qt.AlignTop)
        
        self.plantNameLabel = QLabel("Plant name")
        self.plantNameLabel.setFixedWidth(145)
        self.plantNameLineEdit = QLineEdit()
        self.plantNameLineEdit.setFixedWidth(130)
        
        self.datePlantedLabel = QLabel("Date planted")
        self.datePlantedLineEdit = QLineEdit()
        self.datePlantedLineEdit.setFixedWidth(80)
        self.datePlantedTempLabel = QLabel("")
        self.datePlantedTempLabel.setFixedWidth(30)
        self.datePlantedPushButton = QPushButton("D")
        self.datePlantedPushButton.setFixedWidth(20)
        self.datePlantedPushButton.clicked.connect(self.temp) #temp

        self.waterReqLabel = QLabel("Water requirements")
        self.waterReqLabel.setFixedWidth(115)
        self.waterReqLineEdit = QLineEdit()
        self.waterReqLineEdit.setFixedWidth(100)

        self.notesLabel = QLabel("Notes")
        self.notesLineEdit = QLineEdit()
        self.notesLineEdit.setMinimumWidth(200)

        self.layout3.addWidget(self.addPlantsLabel,0,0)
        self.layout3.addWidget(self.plantNameLabel,1,0)
        self.layout3.addWidget(self.datePlantedLabel,1,1)
        self.layout3.addWidget(self.datePlantedTempLabel,1,2)
        self.layout3.addWidget(self.waterReqLabel,1,3)
        self.layout3.addWidget(self.notesLabel,1,4)
        self.layout3.addWidget(self.plantNameLineEdit,2,0)
        self.layout3.addWidget(self.datePlantedLineEdit,2,1)
        self.layout3.addWidget(self.datePlantedPushButton,2,2)
        self.layout3.addWidget(self.waterReqLineEdit,2,3)
        self.layout3.addWidget(self.notesLineEdit,2,4)

        self.layout3.setAlignment(Qt.AlignTop)
        

        #layout 4
        self.confirmPushButton = QPushButton("Confirm changes")
        self.confirmPushButton.clicked.connect(self.save_changes)

        self.clearPushButton = QPushButton("Clear changes")
        self.clearPushButton.clicked.connect(self.clear_changes)

        self.layout4.addWidget(self.confirmPushButton)
        self.layout4.addWidget(self.clearPushButton)

        self.layout4.setAlignment(Qt.AlignTop)

        
        self.plants_layout.addLayout(self.layout1)
        self.plants_layout.addLayout(self.layout2)
        self.plants_layout.addLayout(self.layout3)
        self.plants_layout.addLayout(self.layout4)
        
        self.plants_layout_widget = QWidget()
        self.plants_layout_widget.setLayout(self.plants_layout)

        return self.plants_layout_widget

    def save_changes(self):
        self.flowerbedModel.submitAll() #Don't know why this doesn't work

        #once everything is submitted
        self.clear_changes()

    def clear_changes(self):
        self.plantNameLineEdit.clear()
        self.datePlantedLineEdit.clear()
        self.waterReqLineEdit.clear()
        self.notesLineEdit.clear()
    
    def select_flowerbed(self):
        self.currentFlowerbedID = self.flowerbedsComboBox.currentIndex() + 1
        self.newQuery = QSqlQuery()
        self.newQuery.prepare("""SELECT
                                 plantGrowing as "Plant",
                                 datePlanted as "Date Planted",
                                 waterNeed as "Water Need",
                                 notes as "Notes"
                                 FROM Plant
                                 WHERE FlowerbedID = ?""")
        self.newQuery.addBindValue(self.currentFlowerbedID)
        self.newQuery.exec_()
        self.flowerbedModel.setQuery(self.newQuery)
        self.flowerbedTableView.setModel(self.flowerbedModel)
    
    def temp(self):
        pass


if __name__ == "__main__":
    application = QApplication(sys.argv)
    plantsWindow = PlantsWindow()
    plantsWindow.show()
    plantsWindow.raise_()
    plantsWindow.resize(700,300)
    application.exec_()
