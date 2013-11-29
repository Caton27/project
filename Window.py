from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import sys

class Window(QMainWindow):
    """Window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Irigation system")
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("FlowerbedDatabase.db")
        self.db.open