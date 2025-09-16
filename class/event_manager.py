# encoding:utf-8

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class EventManager:
    """이벤트 처리, 시그널/슬롯 연결, 타이머 관리를 담당하는 클래스"""

    def __init__(self, main_window):
        """EventManager 초기화

        Args:
            main_window: DxManager 인스턴스 참조
        """
        self.main_window = main_window
        print("EventManager 초기화 완료")

    def handle_event_filter(self, source, event):
        """이벤트 필터링 처리"""
        if event.type() == QEvent.FocusIn and isinstance(source, QListView):
            self.main_window.current_focused_list_view = source

        if source is self.main_window.teamTree and event.type() == QEvent.MouseButtonPress:
            index = self.main_window.teamTree.indexAt(event.pos())

            if index.isValid():
                item = self.main_window.teamTreeModel.itemFromIndex(index)

                if item and item.isCheckable():
                    rect = self.main_window.teamTree.visualRect(index)
                    opts = QStyleOptionViewItem(self.main_window.teamTree.viewOptions())
                    opts.rect = rect
                    opts.state |= QStyle.StateFlag.State_Enabled | QStyle.StateFlag.State_On
                    check_rect = self.main_window.teamTree.style().subElementRect(
                        self.main_window.teamTree.style().SE_ItemViewItemCheckIndicator,
                        opts,
                        self.main_window.teamTree
                    )

                    if check_rect.isEmpty():
                        check_rect = QRect(0,0,16,16)

                    check_rect = check_rect.translated(rect.topLeft())

                    if check_rect.contains(event.pos()):
                        self.main_window.checkArea_click = 1
                        return True

        return QObject.eventFilter(self.main_window, source, event)

    def handle_key_press_event(self, event):
        """키보드 이벤트 처리"""
        if event.key() == Qt.Key_Delete:
            # 현재 스케쥴 리스트뷰의 갯수
            num_listview = self.main_window.dayUi.splitter.count()

            # 현재 스케쥴 리스트뷰의 태스크들 처리
            for i in range(num_listview):
                widget = self.main_window.dayUi.splitter.widget(i)
                listview_layout = widget.layout()

                if listview_layout:
                    frame = listview_layout.itemAt(2).widget()
                    frameLayout = frame.layout()
                    listview = frameLayout.itemAt(0).widget()

                    self.main_window.delete_selected_items(listview)

            self.main_window.updateJson(0)
            self.main_window.reloadShotList()

    def handle_drop_event(self, dropped_items, listView_name):
        """드래그앤드롭 이벤트 처리"""
        num_listview = self.main_window.dayUi.splitter.count()

        listView_list = []
        for i in range(num_listview):
            widget = self.main_window.dayUi.splitter.widget(i)
            listview_layout = widget.layout()

            if listview_layout:
                frame = listview_layout.itemAt(2).widget()
                frameLayout = frame.layout()
                listview_widget = frameLayout.itemAt(0).widget()
                listView_list.append(listview_widget)

        date_labels = self.main_window.getLabelData()

        drop_date = ''
        for i in range(len(listView_list)):
            if listView_name == (listView_list[i].objectName()):
                drop_date = date_labels[i]

        dropData = self.main_window.dropData if hasattr(self.main_window, 'dropData') else {}
        dropData['drop_date'] = drop_date
        dropData['drop_items'] = dropped_items
        self.main_window.dropData = dropData

        self.main_window.updateJson(0)

        # 스케쥴 리스트뷰로 드래그 드랍이 발생한 경우 샷리스트뷰의 태스크 색을 회색으로 변경
        self.main_window.changeColor_assignedTask()

    def setup_connections(self):
        """시그널/슬롯 연결 설정"""
        # 메뉴 연결
        self.main_window.menu_Edit.triggered.connect(self.main_window.showMemberEditDialog)

        # 버튼 연결
        self.main_window.forwardDayBtn.clicked.connect(self.main_window.forwardDay)
        self.main_window.backwardDayBtn.clicked.connect(self.main_window.backwardDay)
        self.main_window.scheduleViewBtn.clicked.connect(self.main_window.showScheduleFrame)
        self.main_window.dashboardViewBtn.clicked.connect(self.main_window.showDashboardFrame)
        self.main_window.dataInfoBtn.clicked.connect(self.main_window.showWorkdataWin)

        # 정렬 버튼 연결
        self.main_window.ui.sortBtn_name.clicked.connect(self.main_window.sort_by_taskName)
        self.main_window.ui.sortBtn_status.clicked.connect(self.main_window.sort_by_status)
        self.main_window.ui.sortBtn_part.clicked.connect(self.main_window.sort_by_part)
        self.main_window.ui.sortBtn_proj.clicked.connect(self.main_window.sort_by_proj)

        # 콤보박스 연결
        self.main_window.comboDay.currentIndexChanged.connect(self.main_window.changeComboDate)
        self.main_window.comboMonth.currentIndexChanged.connect(self.main_window.changeComboDate)
        self.main_window.comboYear.currentIndexChanged.connect(self.main_window.changeComboDate)

        # 선택 모델 연결
        self.main_window.projSelection_model.selectionChanged.connect(self.main_window.process_sel_project)