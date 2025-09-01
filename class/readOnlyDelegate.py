from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# 테이블뷰의 특정 열의 하위 셀들을 편집되지 않게 하기
class ReadOnlyDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        return None
