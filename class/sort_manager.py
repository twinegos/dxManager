# encoding:utf-8

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class SortManager:
    """정렬 관련 기능을 담당하는 클래스"""

    def __init__(self, main_window):
        """SortManager 초기화

        Args:
            main_window: DxManager 인스턴스 참조
        """
        self.main_window = main_window
        print("SortManager 초기화 완료")

    def sort_by_taskName(self):
        """shotListView의 태스크명 정렬"""
        self.main_window.sort_column = 1
        self.main_window.sort_order = Qt.DescendingOrder if self.main_window.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortShotlistview()
        self.main_window.temp_listview_manager.set_listView_view(self.main_window.shotListview, self.main_window.shotListview.model())

    def sort_by_status(self):
        """shotListView의 상태명 정렬"""
        self.main_window.sort_column = 3
        self.main_window.sort_order = Qt.DescendingOrder if self.main_window.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortShotlistview()
        self.main_window.temp_listview_manager.set_listView_view(self.main_window.shotListview, self.main_window.shotListview.model())

    def sort_by_part(self):
        """shotListView의 파트명 정렬"""
        self.main_window.sort_column = 4
        self.main_window.sort_order = Qt.DescendingOrder if self.main_window.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortShotlistview()
        self.main_window.temp_listview_manager.set_listView_view(self.main_window.shotListview, self.main_window.shotListview.model())

    def sort_by_proj(self):
        """shotListView의 프로젝트명 정렬"""
        self.main_window.sort_column = 0
        self.main_window.sort_order = Qt.DescendingOrder if self.main_window.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortShotlistview()
        self.main_window.temp_listview_manager.set_listView_view(self.main_window.shotListview, self.main_window.shotListview.model())

    def sortShotlistview(self):
        """샷 리스트뷰 정렬 실행"""
        model = self.main_window.shotListview.model()

        if isinstance(model, QSortFilterProxyModel):
            source_model = model.sourceModel()
        else:
            source_model = model

        # 정렬상태유지
        if source_model != None:
            source_model.setSortOrder(self.main_window.sort_order)
            source_model.sort(self.main_window.sort_column, self.main_window.sort_order)
            self.main_window.setItemColor_taskList()

    def sort_sch_listView_task(self, sche_class, sche_listview, label_day):
        """스케쥴 리스트뷰의 태스크명 정렬"""
        model = sche_listview.model()
        selectDate = label_day.text()
        year = int(self.main_window.comboYear.currentText())
        month = int(selectDate.split(" ")[0].split("/")[0])
        day = int(selectDate.split(" ")[0].split("/")[1])

        dateDic = {"year":year, "month":month, "day":day}

        sche_class.sort_order = Qt.DescendingOrder if sche_class.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortScheduleListview(sche_listview, model, sche_class.sort_order, 1, dateDic)

    def sort_sch_listView_status(self, sche_class, sche_listview, label_day):
        """스케쥴 리스트뷰의 상태명 정렬"""
        model = sche_listview.model()
        selectDate = label_day.text()
        year = int(self.main_window.comboYear.currentText())
        month = int(selectDate.split(" ")[0].split("/")[0])
        day = int(selectDate.split(" ")[0].split("/")[1])

        dateDic = {"year":year, "month":month, "day":day}

        sche_class.sort_order = Qt.DescendingOrder if sche_class.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortScheduleListview(sche_listview, model, sche_class.sort_order, 3, dateDic)

    def sort_sch_listView_part(self, sche_class, sche_listview, label_day):
        """스케쥴 리스트뷰의 part명의 정렬"""
        model = sche_listview.model()
        selectDate = label_day.text()
        year = int(self.main_window.comboYear.currentText())
        month = int(selectDate.split(" ")[0].split("/")[0])
        day = int(selectDate.split(" ")[0].split("/")[1])

        dateDic = {"year":year, "month":month, "day":day}

        sche_class.sort_order = Qt.DescendingOrder if sche_class.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortScheduleListview(sche_listview, model, sche_class.sort_order, 4, dateDic)

    def sort_sch_listView_proj(self, sche_class, sche_listview, label_day):
        """스케쥴 리스트뷰의 project명의 정렬"""
        model = sche_listview.model()
        selectDate = label_day.text()
        year = int(self.main_window.comboYear.currentText())
        month = int(selectDate.split(" ")[0].split("/")[0])
        day = int(selectDate.split(" ")[0].split("/")[1])

        dateDic = {"year":year, "month":month, "day":day}

        sche_class.sort_order = Qt.DescendingOrder if sche_class.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
        self.sortScheduleListview(sche_listview, model, sche_class.sort_order, 0, dateDic)

    def sortScheduleListview(self, listview, model, sortOrder, sortColumn, date=None):
        """스케쥴 리스트뷰의 소팅실행"""
        if isinstance(model, QSortFilterProxyModel):
            source_model = model.sourceModel()
        else:
            source_model = model

        # 정렬상태유지
        if source_model != None:
            source_model.setSortOrder(sortOrder)
            source_model.sort(sortColumn, sortOrder)
            self.main_window.set_itemBackgroundColor(source_model, date)
            self.main_window.temp_listview_manager.set_listView_view(listview, source_model)