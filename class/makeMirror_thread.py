from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


"""
# 프로젝트가 끝나고 tatic에서 프로젝트가 닫힐경우 스케쥴파일과 연결시킬 미러파일 생성을 위한 쓰레드
class WorkerThread_makeMirror(QThread):
    finished = Signal()
    error = Signal(str)

    def __init__(self, jsonData, dxManager, parent=None):
        super().__init__(parent)
        self.dxManager = dxManager
        self.jsonData = jsonData

    def run(self):
        try:
            self.dxManager.makeMirrorSchedule(self.jsonData)
            self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))
"""
