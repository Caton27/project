from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sqlite3
import sys
import datetime

class AboutWindow(QWidget):
    """Window"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system - About")

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.db")
        self.db.open()

        self.create_about_layout()
        self.setLayout(self.about_layout)

    def create_about_layout(self):
        self.about_layout = QVBoxLayout()

        #widgets    
        #self.aboutText.setWordWrap(True)

        self.theDate = datetime.datetime.today()
        self.theDate = self.theDate.strftime("%d/%m/%Y %H:%M.%S")
        self.initiatedText = QLabel("Program initiated: {0}".format(self.theDate))
        
        self.about_layout.addWidget(self.initiatedText)


        #add widgets
        self.about_layout_widget = QWidget()
        self.about_layout_widget.setLayout(self.about_layout)

        return self.about_layout_widget


if __name__ == "__main__":
    application = QApplication(sys.argv)
    aboutWindow = AboutWindow()
    aboutWindow.show()
    aboutWindow.raise_()
    aboutWindow.resize(600,500)
    application.exec_()
