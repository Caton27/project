from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3
import sys
import datetime

class VolumetricsWindow(QWidget):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system - Volumetrics")

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.db")
        self.db.open()

        self.create_volumetrics_layout()
        self.setLayout(self.volumetrics_layout)

    def create_volumetrics_layout(self):
        self.volumetrics_layout = QVBoxLayout()

        self.layout1 = QHBoxLayout()
        self.layout2 = QGridLayout()
        self.layout3 = QHBoxLayout()

        self.titleFont = QFont()
        self.titleFont.setPointSize(13)
        self.titleFont.setBold(True)

        #layout 1
        self.timeframeLabel = QLabel("Timeframe")
        self.timeframeLabel.setFont(self.titleFont)
        self.timeframeLabel.setFixedWidth(95)

        self.timeframeComboBox = QComboBox()
        self.timeframeComboBox.addItem("24 hours")
        self.timeframeComboBox.addItem("7 days")
        self.timeframeComboBox.addItem("30 days")
        self.timeframeComboBox.addItem("6 months")
        self.timeframeComboBox.addItem("1 year")
        self.timeframeComboBox.addItem("all time")
        self.timeframeComboBox.setFixedWidth(80)
        self.timeframeComboBox.currentIndexChanged.connect(self.select_timeframe)

        self.totalValuesLabel = QLabel("Total Values")
        self.totalValuesLabel.setFont(self.titleFont)
        self.totalValuesLabel.setAlignment(Qt.AlignHCenter)

        self.layout1.addWidget(self.timeframeLabel)
        self.layout1.addWidget(self.timeframeComboBox)
        self.layout1.addWidget(self.totalValuesLabel)
        self.layout1.setAlignment(Qt.AlignTop)

        #layout 2
        self.volumeWaterLabel = QLabel("Volume of water used:")
        self.volumeWaterLabel.setFixedWidth(170)

        self.volumeLineEdit = QLineEdit()
        self.volumeLineEdit.setFixedWidth(100)
        self.volumeLineEdit.setText("24 Litres")
        
        self.volumeWaterLabel2 = QLabel("Volume of water used:")
        self.volumeWaterLabel2.setFixedWidth(170)

        self.volumeLineEdit2 = QLineEdit()
        self.volumeLineEdit2.setFixedWidth(100)
        self.volumeLineEdit2.setText("902 Litres")


        self.costLayout = QHBoxLayout()
        self.cost1Label = QLabel("Cost:")
        self.cost1Label.setFixedWidth(25)
        self.cost1Label.setAlignment(Qt.AlignLeft)
        self.cost2Label = QLabel("£")
        self.cost2Label.setFixedWidth(5)
        self.cost2Label.setAlignment(Qt.AlignRight)
        self.costLayout.addWidget(self.cost1Label)
        self.costLayout.addWidget(self.cost2Label)

        self.costLayout2 = QHBoxLayout()
        self.cost1Label = QLabel("Cost:")
        self.cost1Label.setFixedWidth(25)
        self.cost1Label.setAlignment(Qt.AlignLeft)
        self.cost2Label = QLabel("£")
        self.cost2Label.setFixedWidth(5)
        self.cost2Label.setAlignment(Qt.AlignRight)
        self.costLayout2.addWidget(self.cost1Label)
        self.costLayout2.addWidget(self.cost2Label)

        self.layout2.addWidget(self.volumeWaterLabel,0,0)
        self.layout2.addWidget(self.volumeLineEdit,0,1)
        self.layout2.addWidget(self.volumeWaterLabel2,0,2)
        self.layout2.addWidget(self.volumeLineEdit2,0,3)
        self.layout2.addLayout(self.costLayout,1,0)
        self.layout2.addLayout(self.costLayout2,1,3)
        self.layout2.setAlignment(Qt.AlignTop)
        self.layout2.setAlignment(Qt.AlignLeft)

        #add layouts
        self.volumetrics_layout.addLayout(self.layout1)
        self.volumetrics_layout.addLayout(self.layout2)


        self.volumetrics_layout_widget = QWidget()
        self.volumetrics_layout_widget.setLayout(self.volumetrics_layout)

        return self.volumetrics_layout_widget

    def select_timeframe(self):
        pass

if __name__ == "__main__":
    application = QApplication(sys.argv)
    volumetricsWindow = VolumetricsWindow()
    volumetricsWindow.show()
    volumetricsWindow.raise_()
    volumetricsWindow.resize(800,400)
    application.exec_()
