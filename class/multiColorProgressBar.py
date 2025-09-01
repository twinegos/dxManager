from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MultiColorProgressBar(QProgressBar):

    def __int__(self, parent=None):
        super().__init__(parent)
        self.setMinimum(0)
        self.setMaximum(100)
        self.segments = {}


    def addSegment(self, percentage, color):
        if not hasattr(self, 'segments'):
            self.segments = {}

        self.segments[percentage] = color
        self.update()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        #Draw background
        painter.fillRect(0, 0, self.width(), self.height(), QColor("#303030"))#Qt.white)

        #Calculate and draw segments
        current_x = 0
        total_percentage = sum(self.segments.keys())

        for percentage, color in self.segments.items():

            segment_width = int((percentage / 100.0)*self.width())
            painter.fillRect(current_x, 0, segment_width, self.height(), QColor(color))
            current_x += segment_width

        painter.setPen(QColor(53,53,53))#Qt.darkGray)
        painter.drawRect(0,0, self.width(), self.height())

        # 진행률 텍스트 그리기
        text = f"{int(list(self.segments.keys())[0])}%"
        painter.setPen(Qt.gray)

        # 폰트설정
        font = painter.font()
        #font.setBold(True)
        painter.setFont(font)

        # 텍스트를 중앙에 배치
        rect = self.rect()
        painter.drawText(rect, Qt.AlignCenter, text)