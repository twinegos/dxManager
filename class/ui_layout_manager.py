# encoding:utf-8

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class UILayoutManager:
    def __init__(self, main_window):
        """
        UI 레이아웃 및 위젯 관리를 담당하는 클래스
        """
        self.main_window = main_window

    def update_splitter_size(self):
        """
        스플리터 크기 업데이트
        """
        Listview_Num = self.main_window.dayUi.splitter.count()
        total_min_width = Listview_Num * self.main_window.listview_minimum
        self.main_window.dayUi.splitter.setMinimumWidth(total_min_width)
        self.main_window.dayUi.splitter.adjustSize()
        self.main_window.dayUi.scrollArea.adjustSize()

    def reset_splitter_size(self):
        """
        스케줄 리스트뷰의 스플리터 사이즈 리셋
        """
        listViewNum = int(self.main_window.listViewNumLineEdit.text())
        splitter_width = listViewNum * self.main_window.listview_minimum

        equal_size = splitter_width // listViewNum
        sizes = [equal_size] * listViewNum

        self.main_window.dayUi.splitter.setSizes(sizes)
        self.main_window.dayUi.splitter.setFixedWidth(splitter_width)

    def rescale_listview(self, scaleUI, fontScale):
        """
        리스트뷰 크기 및 폰트 조정
        """
        currentNumListView = self.main_window.day_listViewLayout.count()

        for i in range(currentNumListView):
            layout_listview = self.main_window.day_listViewLayout.itemAt(i)

            if layout_listview:
                widgetItem_frame = layout_listview.layout().itemAt(2)

                if widgetItem_frame:
                    frame = widgetItem_frame.widget()

                    if frame:
                        currentListview = frame.layout().itemAt(0).widget()

                        font = QFont()
                        font.setPointSize(fontScale)
                        currentListview.setFont(font)