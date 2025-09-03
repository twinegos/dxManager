from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# 진급, 및 부서이동으로 인한 개인정보 변경시 이를 적용하기 위한 쓰레드
class updateUserInfoThread(QThread):
    completed_signal = Signal()

    def __init__(self, members, dx_manager, parent=None):
        super().__init__(parent)
        self.dx_manager = dx_manager
        self.members = members

    def run(self):
        self.dx_manager.updateUserInfo(self.members)

