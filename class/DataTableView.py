

from PySide2.QtCore import  *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import struct
import json
import os


currentPath = os.path.dirname(os.path.abspath(__file__))









class DataTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(DataTableModel, self).__init__()
        self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

        

