# -*- coding: utf-8 -*-
"""
UI 컨트롤러 클래스
dxManager에서 UI 관리 관련 기능을 분리한 모듈
"""

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import config


class UIController:
    def __init__(self, main_window):
        """
        UI 컨트롤러 초기화
        
        Args:
            main_window: 메인 윈도우 인스턴스
        """
        self.main_window = main_window
        self.ui = main_window.ui
        
    def setup_listview_ui(self):
        """리스트뷰 UI 초기 설정"""
        try:
            # 기본 리스트뷰 설정
            self._setup_basic_listviews()
            print("리스트뷰 UI 설정 완료")
        except Exception as e:
            print(f"리스트뷰 UI 설정 오류: {e}")
    
    def _setup_basic_listviews(self):
        """기본 리스트뷰들의 초기 설정"""
        # 기본적인 리스트뷰 설정 로직
        pass
    
    def refresh_listviews(self, direction=None, schedule_data=None):
        """
        리스트뷰들을 새로고침
        
        Args:
            direction: 방향 (0: 현재, 1: 다음, -1: 이전)
            schedule_data: 스케줄 데이터
        """
        try:
            if direction is not None and schedule_data is not None:
                # 스케줄 데이터를 기반으로 리스트뷰 갱신
                self._update_listviews_with_schedule(direction, schedule_data)
            else:
                # 기본 새로고침
                self._refresh_all_listviews()
        except Exception as e:
            print(f"리스트뷰 새로고침 오류: {e}")
    
    def _update_listviews_with_schedule(self, direction, schedule_data):
        """스케줄 데이터로 리스트뷰 업데이트"""
        # 복잡한 리스트뷰 업데이트 로직은 점진적으로 이동
        pass
    
    def _refresh_all_listviews(self):
        """모든 리스트뷰 새로고침"""
        # 기본 새로고침 로직
        pass
    
    def reload_shot_list(self):
        """샷 리스트뷰 다시 로딩"""
        try:
            QApplication.setOverrideCursor(Qt.WaitCursor)
            
            # 샷 리스트 로딩 로직은 점진적으로 이동
            self._load_shot_data()
            
            QApplication.restoreOverrideCursor()
        except Exception as e:
            print(f"샷 리스트 로딩 오류: {e}")
            QApplication.restoreOverrideCursor()
    
    def _load_shot_data(self):
        """샷 데이터 로딩"""
        # 샷 데이터 로딩 로직
        pass
    
    def update_listview_model(self, listview, model_data):
        """
        리스트뷰 모델 업데이트
        
        Args:
            listview: 대상 리스트뷰
            model_data: 모델 데이터
        """
        try:
            if listview and model_data:
                # 모델 데이터로 리스트뷰 업데이트
                self._apply_model_to_listview(listview, model_data)
        except Exception as e:
            print(f"리스트뷰 모델 업데이트 오류: {e}")
    
    def _apply_model_to_listview(self, listview, model_data):
        """리스트뷰에 모델 적용"""
        # 모델 적용 로직
        pass
    
    def set_listview_view_basic(self, listview, model):
        """
        리스트뷰 뷰 기본 설정 (기존 메서드)

        Args:
            listview: 대상 리스트뷰
            model: 모델
        """
        try:
            if listview and model:
                listview.setModel(model)
                self._configure_listview_appearance(listview)
        except Exception as e:
            print(f"리스트뷰 뷰 설정 오류: {e}")
    
    def _configure_listview_appearance(self, listview):
        """리스트뷰 외관 설정"""
        try:
            # 기본 외관 설정
            listview.setAlternatingRowColors(True)
            listview.setSelectionBehavior(QAbstractItemView.SelectRows)
        except Exception as e:
            print(f"리스트뷰 외관 설정 오류: {e}")
    
    def sort_listview(self, listview, model, sort_order, sort_column, date=None):
        """
        리스트뷰 정렬
        
        Args:
            listview: 대상 리스트뷰
            model: 모델
            sort_order: 정렬 순서
            sort_column: 정렬 컬럼
            date: 날짜 (선택적)
        """
        try:
            if model:
                model.sort(sort_column, sort_order)
                listview.sortByColumn(sort_column, sort_order)
        except Exception as e:
            print(f"리스트뷰 정렬 오류: {e}")
    
    def get_listview_selected_items(self, listview):
        """
        리스트뷰 선택된 아이템들 반환 (원본 로직 유지)
        
        Args:
            listview: 대상 리스트뷰
            
        Returns:
            list: 선택된 아이템들
        """
        try:
            selected_indexes = listview.selectedIndexes()
            
            curr_items = []
            for index in selected_indexes:
                item = listview.model().data(index, Qt.DisplayRole)
                
                if item not in curr_items:
                    curr_items.append(item)
            
            return curr_items
        except Exception as e:
            print(f"선택된 아이템 조회 오류: {e}")
            return []
    
    def clear_listview_selection(self, listview):
        """리스트뷰 선택 해제"""
        try:
            if listview and listview.selectionModel():
                listview.selectionModel().clearSelection()
        except Exception as e:
            print(f"리스트뷰 선택 해제 오류: {e}")
    
    def set_listview_filter(self, listview, filter_text):
        """
        리스트뷰 필터 설정
        
        Args:
            listview: 대상 리스트뷰
            filter_text: 필터 텍스트
        """
        try:
            if listview and hasattr(listview.model(), 'setFilterFixedString'):
                listview.model().setFilterFixedString(filter_text)
        except Exception as e:
            print(f"리스트뷰 필터 설정 오류: {e}")
    
    def resize_listview_columns(self, listview):
        """리스트뷰 컬럼 크기 자동 조정"""
        try:
            if listview:
                listview.resizeColumnsToContents()
        except Exception as e:
            print(f"리스트뷰 컬럼 크기 조정 오류: {e}")
    
    def update_team_treeview(self, tree_data):
        """
        팀 트리뷰 업데이트
        
        Args:
            tree_data: 트리 데이터
        """
        try:
            if tree_data:
                self._populate_team_tree(tree_data)
        except Exception as e:
            print(f"팀 트리뷰 업데이트 오류: {e}")
    
    def _populate_team_tree(self, tree_data):
        """팀 트리 데이터 채우기"""
        # 트리 데이터 채우기 로직
        pass
    
    def get_checked_tree_items(self, tree_model):
        """
        체크된 트리 아이템들 반환
        
        Args:
            tree_model: 트리 모델
            
        Returns:
            list: 체크된 아이템들
        """
        try:
            checked_items = []
            if tree_model:
                # 체크된 아이템 수집 로직
                self._collect_checked_items(tree_model.invisibleRootItem(), checked_items)
            return checked_items
        except Exception as e:
            print(f"체크된 아이템 조회 오류: {e}")
            return []
    
    def _collect_checked_items(self, item, checked_items):
        """체크된 아이템들을 재귀적으로 수집"""
        try:
            for row in range(item.rowCount()):
                child = item.child(row)
                if child and child.checkState() == Qt.Checked:
                    checked_items.append(child.text())
                # 하위 아이템들도 확인
                self._collect_checked_items(child, checked_items)
        except Exception as e:
            print(f"체크된 아이템 수집 오류: {e}")
    
    def show_context_menu(self, listview, position):
        """
        컨텍스트 메뉴 표시
        
        Args:
            listview: 대상 리스트뷰
            position: 메뉴 위치
        """
        try:
            if listview:
                menu = QMenu()
                # 컨텍스트 메뉴 아이템들 추가
                self._add_context_menu_items(menu, listview)
                menu.exec_(listview.mapToGlobal(position))
        except Exception as e:
            print(f"컨텍스트 메뉴 표시 오류: {e}")
    
    def _add_context_menu_items(self, menu, listview):
        """컨텍스트 메뉴 아이템들 추가"""
        try:
            # 기본 메뉴 아이템들
            refresh_action = menu.addAction("새로고침")
            refresh_action.triggered.connect(lambda: self.refresh_listviews())

            clear_action = menu.addAction("선택 해제")
            clear_action.triggered.connect(lambda: self.clear_listview_selection(listview))
        except Exception as e:
            print(f"컨텍스트 메뉴 아이템 추가 오류: {e}")

    # ====== TempListViewManager에서 이동된 메서드들 ======

    def setListviewLineEdit(self, value):
        """슬라이더의 value가 홀수만 출력되도록하며, lineEdit의 텍스트가 그값을 받아 표시되도록 함"""
        if value % 2 == 0:
            self.main_window.listViewNumLineEdit.setText(str(value+1))
        else:
            self.main_window.listViewNumLineEdit.setText(str(value))

    def getCurrentListViewDate(self, shiftDays):
        """현재 ListView들의 날짜 정보를 반환"""
        numberListView = self.main_window.dayUi.splitter.count()

        listView_labels = []
        for i in range(numberListView):
            addNum = shiftDays + (-1*((numberListView-1) - i))
            listViewDate = self.main_window.rangeEndDate.addDays(addNum)
            date = {"year":listViewDate.year() , "month":listViewDate.month(), "day":listViewDate.day()}
            listView_labels.append(date)

        return listView_labels

    def set_listView_view(self, listView, model):
        """ListView 뷰 설정 및 필터링 (TempListViewManager에서 이동)"""
        if model != None:
            for row in range(model.rowCount()):
                index = model.index(row)
                taskData = model.data(index, Qt.DisplayRole)

                # 이번주 마감인 태스크들의 온/오프
                taskColor = model.data(index, Qt.BackgroundRole) # 배경색 가져오기

                # taskColor가 None인 경우 안전 처리
                if taskColor is not None:
                    if (taskColor.red() != 94 and taskColor.green() != 29 and  taskColor.blue() != 35) and self.main_window.deadLine_flag==1:
                        listView.setRowHidden(row, True)
                    elif (taskColor.red() != 94 and taskColor.green() != 29 and  taskColor.blue() != 35) and self.main_window.deadLine_flag==0:
                        listView.setRowHidden(row, False)
                else:
                    # taskColor가 None인 경우 기본 동작 (데드라인 플래그에 따라 처리)
                    if self.main_window.deadLine_flag==0:
                        listView.setRowHidden(row, False)

                # 스테이터스 체크박스의 상태에 따른 온/오프
                app_check = self.main_window.dayUi.checkBox_approved_v.isChecked()
                inprogress_check = self.main_window.dayUi.checkBox_inprogress_v.isChecked()
                ready_check = self.main_window.dayUi.checkBox_ready_v.isChecked()
                review_check = self.main_window.dayUi.checkBox_review_v.isChecked()
                hold_check = self.main_window.dayUi.checkBox_hold_v.isChecked()
                ok_check = self.main_window.dayUi.checkBox_ok_v.isChecked()
                wait_check = self.main_window.dayUi.checkBox_wait_v.isChecked()
                omit_check = self.main_window.dayUi.checkBox_omit_v.isChecked()
                retake_check = self.main_window.dayUi.checkBox_retake_v.isChecked()

                if app_check == False and taskData[3] == "Approved":
                    listView.setRowHidden(row, True)

                if inprogress_check == False and taskData[3] == "In-Progress":
                    listView.setRowHidden(row, True)

                if ready_check == False and taskData[3] == "Ready":
                    listView.setRowHidden(row, True)

                if review_check == False and taskData[3] == "Review":
                    listView.setRowHidden(row, True)

                if hold_check == False and taskData[3] == "Hold":
                    listView.setRowHidden(row, True)

                if ok_check == False and taskData[3] == "OK":
                    listView.setRowHidden(row, True)

                if wait_check == False and taskData[3] == "Waiting":
                    listView.setRowHidden(row, True)

                if omit_check == False and taskData[3] == "Omit":
                    listView.setRowHidden(row, True)

                if retake_check == False and taskData[3] == "Retake":
                    listView.setRowHidden(row, True)

    def getListViewItem(self, listView):
        """리스트뷰의 모든 아이템 조회"""
        model = listView.model()
        allIndex = []
        num = range(model.rowCount(QModelIndex()))

        for row in range(model.rowCount(QModelIndex())):
            index = model.index(row)
            allIndex.append(index)

        currItems = []
        for index in allIndex:
            item = listView.model().data(index, Qt.DisplayRole)

            if item not in currItems:
                currItems.append(item)

        return currItems

    def getListViewItem_inJson(self, listView, members):
        """ListView의 JSON 데이터 기반 아이템 조회"""
        num_listview = self.main_window.dayUi.splitter.count()

        label_index = 0
        listView_list=[]
        for i in range(num_listview):

            widget = self.main_window.dayUi.splitter.widget(i)
            listview_layout = widget.layout()

            if listview_layout:
                frame = listview_layout.itemAt(2).widget()
                frameLayout = frame.layout()
                listview_widget = frameLayout.itemAt(0).widget()
                listView_list.append(listview_widget)

        date_labels = self.main_window.getLabelData()

        listView_date = ''
        for i in range(len(listView_list)):
            if listView.objectName() == (listView_list[i].objectName()):
                listView_date = date_labels[i]

        listView_year = listView_date.split('/')[0]
        listView_month = listView_date.split('/')[1]
        listView_day = listView_date.split('/')[2]

        # Import jsonData from global scope
        from dxManager import jsonData

        taskList = []
        for data in jsonData:
            task_dep = {}
            if str(data['year']) == listView_year and str(data['month']) == listView_month and str(data['day']) == listView_day:
                if data['tasks']:
                    for proj in data['tasks'][0]:
                        for task in data['tasks'][0][proj]:
                            task_proj_part = {}
                            proj_part = []

                            proj_part.append(proj)
                            proj_part.append(data["department"])

                            task_proj_part[task] = proj_part

                            if task_proj_part not in taskList:
                                taskList.append(task_proj_part)

        tuple_tasks = self.main_window.convert_to_tuple(taskList, members)

        return (tuple_tasks)

    def makeListView(self, label, listView, parentLayout, childLayout, scaleUI):
        """ListView 위젯 생성"""
        # Import dragDropListView 모듈
        import dragDropListView as ddlv

        listViewLayout = QVBoxLayout()
        listViewLayout.setObjectName(childLayout)
        label_day = QLabel(self.main_window.dayScheduleFrame)
        label_day.setObjectName(label)
        label_day.setText(label)
        font_label = QFont()
        font_label.setPointSize(10)
        font_label.setBold(True)
        font_label.setWeight(75)
        label_day.setFont(font_label)
        listViewLayout.addWidget(label_day, 0, Qt.AlignHCenter)

        listView_day = ddlv.dropListView(self.main_window.dayScheduleFrame)
        listView_day.setEditTriggers(QAbstractItemView.NoEditTriggers) # 더블클릭시에 에딧모드로 들어가지 않도록 함
        listView_day.setObjectName(listView)
        listView_day.setMinimumSize(scaleUI, 0)
        listView_day.installEventFilter(self.main_window)

        font_listView = QFont()
        font_listView.setPointSize(9)
        listView_day.setFont(font_listView)
        listViewLayout.addWidget(listView_day)
        parentLayout.addLayout(listViewLayout)

        return listView_day, listViewLayout

    def changeListViewUI_notTracking(self):
        """슬라이더 릴리즈 시 ListView UI 변경"""
        scaleUI = 300/(int(self.main_window.listViewNumLineEdit.text())/3)

        current_Listview_Num = self.main_window.dayUi.splitter.count()
        changed_ListView_Num = int(self.main_window.listViewNumLineEdit.text())
        number_add = changed_ListView_Num - current_Listview_Num

        if 300 < scaleUI < 800:
            fontScale = 12
        elif scaleUI <= 300:
            scaleUI = 300 # 리스트뷰의 최소크기
            fontScale = 12
        elif scaleUI >= 800:
            fontScale = 25

        if number_add > 0:
            self.main_window.addListView(number_add, current_Listview_Num, scaleUI)
        elif number_add < 0:
            self.removeListView(number_add, current_Listview_Num)

        mm = self.main_window.listViewScroll.horizontalScrollBar().maximum()
        self.main_window.listViewScroll.horizontalScrollBar().setValue(mm)

    def removeListView(self, removeNum, currentNum):
        """ListView 제거"""
        half_val = abs(int(removeNum/2)) # 추가되는 리스트뷰중 앞쪽 혹은 뒤쪽에 삭제할 리스트뷰의 개수(전체삭제되는 개수의 절반)
        half_existList = int(currentNum / 2) # 이미 존재하는 리스트뷰 개수기준으로 현재날짜기준 앞쪽 혹은 뒤쪽의 리스트뷰개수(전체개수의 절반)

        widgets_to_remove = []
        for i in range(abs(removeNum)):
            if  i < half_val:
                widgets_to_remove.append(self.main_window.dayUi.splitter.widget(i))

            if i >= half_val:
                numLayout = self.main_window.dayUi.splitter.count()
                widgets_to_remove.append(self.main_window.dayUi.splitter.widget((numLayout-1)-(i-half_val)))

        if widgets_to_remove:

            widgets_to_check = widgets_to_remove[:]
            for widget in widgets_to_remove:
                self.main_window._remove_layout(widget)

            QApplication.processEvents() # 삭제 이벤트 처리
            widgets_to_remove.clear() # 참조 제거

        newRangeEndDate = QDate(self.main_window.rangeEndDate.year(), self.main_window.rangeEndDate.month(), self.main_window.rangeEndDate.day()).addDays(-1*half_val)
        newRangeStartDate = QDate(newRangeEndDate.year(), newRangeEndDate.month(), newRangeEndDate.day()).addDays(-1*(removeNum+currentNum)+1)

        self.main_window.update_range_Label(newRangeStartDate, newRangeEndDate)
        self.main_window.rangeEndDate = newRangeEndDate

        self.main_window.ui_layout_manager.reset_splitter_size() # 스케쥴 리스트뷰의 스플리터 사이즈 리셋

    def changeListViewUI_(self, text):
        """LineEdit 텍스트 변경 시 ListView UI 변경"""
        self.main_window.listViewSlider.setValue(int(text))

        scaleUI = 300/(int(self.main_window.listViewNumLineEdit.text())/3)

        current_Listview_Num = self.main_window.dayUi.splitter.count()

        changed_ListView_Num = int(self.main_window.listViewNumLineEdit.text())
        number_add = changed_ListView_Num - current_Listview_Num

        if 300 < scaleUI < 800:
            fontScale = 12

        elif scaleUI <= 300:
            scaleUI = 300 # 리스트뷰의 최소크기
            fontScale = 12

        elif scaleUI >= 800:
            fontScale = 25


        if number_add > 0:
            self.main_window.addListView(number_add, current_Listview_Num, scaleUI)

        elif number_add < 0:
            self.removeListView(number_add, current_Listview_Num)

        max_scroll = self.main_window.listViewScroll.horizontalScrollBar().maximum()
        self.main_window.listViewScroll.horizontalScrollBar().setValue(max_scroll)

    def addListView(self, num, currentNum, scaleUI, active_jsonDate):
        """ListView 추가"""
        import sys
        sys.path.append('./class')
        import scheduleListview as lv

        half_val = int(num/2) # 추가되는 리스트뷰중 앞쪽 혹은 뒤쪽에 붙일 리스트뷰의 개수(전체추가되는 개수의 절반)
        half_existList = int(currentNum / 2) # 이미 존재하는 리스트뷰 개수기준으로 현자날짜기준 앞쪽 혹은 뒤쪽에 붙일 리스트뷰개수(전체개수의 절반)

        halfDay = QDate(self.main_window.rangeEndDate.year(), self.main_window.rangeEndDate.month(), self.main_window.rangeEndDate.day()).addDays(-1*half_existList)

        currentDay = halfDay.day()
        currentMonth = halfDay.month()
        currentYear = halfDay.year()

        num_all_listview = currentNum + num
        value_addDay = int((num_all_listview) / 2)

        for i in range(num):

            listViewName = "listView_" + str(i+currentNum)

            num_addDay = i- half_val
            dayNumber_add = 0

            if i < half_val:
                dayNumber_add = num_addDay-half_existList

            elif i >= half_val:
                dayNumber_add = num_addDay+half_existList+1

            weekDay = {1:'월', 2:'화', 3:'수', 4:'목', 5:'금', 6:'토', 7:'일'}
            label_year = QDate(int(currentYear), int(currentMonth), int(currentDay)).addDays(dayNumber_add).year()
            label_month = QDate(int(currentYear), int(currentMonth), int(currentDay)).addDays(dayNumber_add).month()
            label_day = QDate(int(currentYear), int(currentMonth), int(currentDay)).addDays(dayNumber_add).day()
            label_dow = QDate(int(currentYear), int(currentMonth), int(currentDay)).addDays(dayNumber_add).dayOfWeek()

            listview_labelName = str(label_month) + "/" + str(label_day) + " ( "+weekDay[label_dow]+" )"

            layout_parent = self.main_window.dayUi.splitter
            layout_child = listViewName + "_layout"

            newListview = lv.ScheduleListView(listview_labelName, listViewName, layout_parent, layout_child, scaleUI, self.main_window, self.main_window.manager, self.main_window.dayScheduleFrame, self.main_window)

            # 새로 생성한 리스트뷰에 드래그 드롭이 발생한경우, self.get_dropEvent 메서드를 실행시킴
            newListview.listView_day.itemsDropped.connect(self.main_window.get_dropEvent)

            # 리스트뷰내 아이템을 더블클릭하면 테스크 정보창이 생성
            newListview.listView_day.doubleClicked.connect(lambda index: self.main_window.openMedia(self.main_window.current_focused_list_view, index))

            # 리스트뷰에 컨텍스트 메뉴 연결
            newListview.listView_day.setContextMenuPolicy(Qt.CustomContextMenu)
            newListview.listView_day.customContextMenuRequested.connect(
                lambda pos, lv=newListview.listView_day: self.main_window.show_context_menu(lv, pos))

            # label_dow 가 토요일이나 일요일일경우 색깔변경
            if label_dow == 6 or label_dow == 7:
                newListview.listView_day.setStyleSheet("QListView { background-color: #232323; }")
            else:
                newListview.listView_day.setStyleSheet("QListView { background-color: #2a2a2a; }")

            # 스케쥴뷰의 리스트뷰의 갯수가 늘어날 경우 앞날짜의 리스트뷰와 뒷날짜의 리스트뷰가 늘어나게 되는데
            # 앞날짜의 리스트뷰와 뒷날짜의 리스트뷰가 모두 뒤로 붙지 않고 앞날짜는 앞에 뒷날짜는 뒤로 붙게 생성.
            if i < half_val:
                for j in range(currentNum):
                    widget = self.main_window.dayUi.splitter.widget(i)
                    exist_layout = widget.layout()

                    parentWidget = exist_layout.parentWidget()

                    self.main_window.dayUi.splitter.addWidget(parentWidget)

        newRangeEndDate = QDate(self.main_window.rangeEndDate.year(), self.main_window.rangeEndDate.month(), self.main_window.rangeEndDate.day()).addDays(half_val)
        newRangeStartDate = QDate(newRangeEndDate.year(), newRangeEndDate.month(), newRangeEndDate.day()).addDays(-1*(num+currentNum)+1)

        self.main_window.update_range_Label(newRangeStartDate, newRangeEndDate)
        self.main_window.rangeEndDate = newRangeEndDate

        listViewNum = self.main_window.dayUi.splitter.count()

        # 현재 ui에 표시되어있는 스케쥴 리스트뷰 가져오기(옮기기전)
        listViews=[]
        layouts = []
        for i in range(listViewNum):
            widget = self.main_window.dayUi.splitter.widget(i)
            layout = widget.layout()

            layouts.append(layout)

            if layout:
                frame = layout.itemAt(2).widget()
                frameLayout = frame.layout()
                listView = frameLayout.itemAt(0).widget()
                self.main_window.manager.Move_sideway_setContainer(frame, layout)


        self.main_window.refereshListViews(0, active_jsonDate)
        self.main_window.ui_layout_manager.update_splitter_size() # 생성된 리스트뷰들의 갯수의 합보다 scroll area 의 크기를 더크게 셋팅하여 splitter 작동되도록 함
        self.main_window.ui_layout_manager.reset_splitter_size() # 스케쥴 리스트뷰의 스플리터 사이즈 리셋

    def setUp_listViewUI(self, init_jsonData):
        """초기 ListView UI 설정"""
        import sys
        sys.path.append('./class')
        import scheduleListview as lv
        import pandas as pd

        userID = config.get_user_id()

        numberListView = int(self.main_window.listViewNumLineEdit.text())
        today = QDate.currentDate()
        monday = today.addDays(-today.dayOfWeek()+1)
        value_addDay = int(numberListView / 2)
        range_date = []

        for i in range(numberListView):
            currentValue_day = i - value_addDay
            weekDay = {1:'월', 2:'화', 3:'수', 4:'목', 5:'금', 6:'토', 7:'일'}

            if currentValue_day==0:
                listViewName = "listView_0"
            elif currentValue_day<0:
                listViewName = "listView_L_" + str(abs(currentValue_day))
            elif currentValue_day>0:
                listViewName = "listView_R_" + str(currentValue_day)

            date = monday.addDays(i)
            label_dow = date.dayOfWeek()
            labelName = str(date.month()) + "/" + str(date.day()) + " ( " + weekDay[label_dow] + " )"
            label_date = QDate(date.year(), date.month(), date.day())

            layout_parent = self.main_window.dayUi.splitter
            layout_child = listViewName + "_layout"

            # 리스트뷰 생성
            newListview = lv.ScheduleListView(labelName, listViewName, layout_parent, layout_child, 300, self.main_window, self.main_window.manager, self.main_window.dayScheduleFrame, self.main_window)

            # 새로 생성한 리스트뷰에 드래그 드롭이 발생한경우, self.get_dropEvent 메서드를 실행시킴
            newListview.listView_day.itemsDropped.connect(self.main_window.get_dropEvent)

            font = QFont()
            font.setPointSize(12)
            newListview.listView_day.setFont(font)

            if i==0:
                range_date.append(label_date)
            elif i==numberListView-1:
                range_date.append(label_date)

            # 리스트뷰내 아이템을 더블클릭하면 테스크 정보창이 생성
            newListview.listView_day.doubleClicked.connect(lambda index: self.main_window.openMedia(self.main_window.current_focused_list_view, index))

            # 초기 리스트뷰 생성에 컨텍스트 메뉴 연결
            newListview.listView_day.setContextMenuPolicy(Qt.CustomContextMenu)
            newListview.listView_day.customContextMenuRequested.connect(
                lambda pos, lv=newListview.listView_day: self.main_window.show_context_menu(lv, pos))

            # label_dow 가 토요일이나 일요일일경우 색깔변경
            if label_dow == 6 or label_dow == 7:
                newListview.listView_day.setStyleSheet("QListView { background-color: #232323; }")
            else:
                newListview.listView_day.setStyleSheet("QListView { background-color: #2a2a2a; }")

        self.main_window.update_range_Label(range_date[0], range_date[1])
        self.main_window.rangeEndDate = range_date[1] # ui 처음 생성시 전역변수 rangeEndDate에 enddate 저장

        # 처음 ui를 켰을때 현재 등록시킨 스케쥴을 표시하게 하기위해 현재기준 앞뒤 한주씩의 기간 설정
        today = QDate.currentDate()
        monday = today.addDays(-today.dayOfWeek()+1)
        friday = monday.addDays(4)
        lastWeek_monday = today.addDays(-7+(-today.dayOfWeek()+1))
        nextWeek_friday = today.addDays(11+(-today.dayOfWeek()+1))

        date = lastWeek_monday

        if init_jsonData != []:
            json_df = pd.DataFrame(init_jsonData) # init_jsonData 파일을 판다스 데이타프레임으로 변환
            artist_df = json_df.set_index('artist') # artist 열을 인덱스로 가지는 데이타프레임으로 변환
            user_df = artist_df.loc[artist_df.index == userID] # 아티스트 데이타프레임에서 현재 사용자의 데이타만 뽑은 데이타프레임으로 변환

            # 지난주 월요일부터 다음주 금요일까지의 어싸인된 스케쥴을 확인후 해당 프로젝트만 선택되게 하기
            dates = []
            while date <= nextWeek_friday:
                dateList = {}
                dateList["year"] = date.year()
                dateList["month"] = date.month()
                dateList["day"] = date.day()

                if dateList not in dates:
                    dates.append(dateList)

                date = date.addDays(1)

            betweenDate_df = pd.DataFrame(dates)
            columns_compare = ["year", "month", "day"] # 현재유저의 스케쥴어싸인 데이타프레임과 3주간의 날짜를 비교하여 일치하는것을 찾기위해 비교할 날짜 컬럼 리스트
            mask1 = betweenDate_df[columns_compare].apply(tuple, axis=1)
            mask2 = user_df[columns_compare].apply(tuple, axis=1)
            commonValues = set(mask1).intersection(set(mask2)) # 두마스크의 일치되는 것만 뽑아낸 set
            recentWork_df = user_df[mask2.isin(commonValues)] # 일치하는 날짜에 해당하는 스케쥴어싸인 데이타프레임
            userTasks = recentWork_df['tasks'] # task컬럼만 시리즈로 추출

            # init_jsonData 안의 현재 유저의 스케쥴 데이타들중 task부분만 추출하여 set연산자를 통해 현재 진행중인 프로젝트 이름만 추출
            projects = set()
            for task in userTasks: # 시리즈안의 프로젝트만 set 연산자를 통해 뽑아냄
                proj = set(task[0])
                projects = projects | proj

            # 추출된 프로젝트이름(코드)를 ui상 표시된 이름으로 변환하여 리스트에 저장
            projLong_list = []
            for projCode in projects:
                projName = self.main_window.projects[projCode][1]
                if projName not in projLong_list:
                    projLong_list.append(projName)

            # 뽑아낸 프로젝트 이름을 이용하여 UI상의 프로젝트 리스트뷰에서 해당 프로젝트를 선택
            proj_model = self.main_window.projListview.model()

            for row in range(proj_model.rowCount()):
                index = proj_model.index(row, 0)
                text_proj = proj_model.data(index)
                if text_proj in projLong_list:
                    self.main_window.projSelection_model.select(index, QItemSelectionModel.Select)

        # 현재 리스트뷰에서 오늘에 해당하는 날짜를 하이라이트 시키기
        numListview = self.main_window.listViewNumLineEdit.text()

        for i in range(int(numListview)):
            widget = self.main_window.dayUi.splitter.widget(i)
            layout = widget.layout()

            if layout:
                frame = layout.itemAt(2).widget()
                dateIndex = layout.itemAt(0).widget()
                date = dateIndex.text()
                dateSplit = date.split(" (")
                month = str(today.month())
                day = str(today.day())
                todayString = month + "/" + day

                if dateSplit[0] == todayString:
                    widget.setStyleSheet("background-color: #38613b;")
                    self.main_window.manager.set_active_container(frame, layout, False)

        self.main_window.ui_layout_manager.update_splitter_size() # 생성된 리스트뷰들의 갯수의 합보다 scroll area 의 크기를 더크게 셋팅하여 splitter 작동되도록 함