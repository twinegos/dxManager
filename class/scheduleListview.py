
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtUiTools import loadUiType

import dragDropListView as ddlv # ddlv : drag and drop listView


# 스케쥴 리스트뷰 셋업
class ScheduleListView(QWidget):      #, label, listView, parentLayout, childLayout, scaleUI):

    def __init__(self, label, listView, parentLayout, childLayout, scaleUI, main, manager, parent=None, mainLoop=None):
        super().__init__()

        self.manager = manager

        self.sort_order = Qt.AscendingOrder
        self.sort_column = 1

        self.label_day = QLabel(parent)
        self.label_day.setObjectName(label)
        self.label_day.setText(label)
        self.font_label = QFont()
        self.font_label.setPointSize(10)
        self.font_label.setBold(True)
        self.font_label.setWeight(75)
        self.label_day.setFont(self.font_label)


        self.splitter_layoutWidget = QWidget(parentLayout)
        self.splitter_layoutWidget.setObjectName(self.label_day.text() + "_layoutWidget")


        self.listViewLayout = QVBoxLayout(self.splitter_layoutWidget)
        self.listViewLayout.setSpacing(0)
        self.listViewLayout.setContentsMargins(3,0,3,0)        
        self.listViewLayout.setObjectName(childLayout)

        self.listViewLayout.addWidget(self.label_day, 0, Qt.AlignHCenter)

        # 소팅을 위한 버튼추가
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(label+ "_buttonLayout")
        self.listViewLayout.addLayout(self.buttonLayout)


        self.sortBtn_part = QPushButton(parent)
        self.sortBtn_part.setObjectName(label+"_sortBtn_part")
        #self.sortBtn_part.setMaximumSize(QSize(20, 17))
        partFont = QFont()
        partFont.setPointSize(7)
        self.sortBtn_part.setFont(partFont)
        self.sortBtn_part.setText("P")
        self.sortBtn_part.setStyleSheet("""
            QPushButton {
                border-radius: 0px; 
                border: 1px solid #333333;
                background-color: #444444;
            }""")
        self.buttonLayout.addWidget(self.sortBtn_part)



        self.sortBtn_name = QPushButton(parent)
        self.sortBtn_name.setObjectName(label+"_sortBtn_taskName")
        #self.sortBtn_name.setMaximumSize(QSize(16777215, 17))
        taskFont = QFont()
        taskFont.setPointSize(7)
        self.sortBtn_name.setFont(taskFont)
        self.sortBtn_name.setText("Task")
        self.sortBtn_name.setStyleSheet("""
            QPushButton {
                border-radius: 0px; 
                border: 1px solid #333333;
                background-color: #444444;
            }""")
        self.buttonLayout.addWidget(self.sortBtn_name)



        self.sortBtn_proj = QPushButton(parent)
        self.sortBtn_proj.setObjectName(label+"_sortBtn_project")
        #self.sortBtn_name.setMaximumSize(QSize(16777215, 17))
        projFont = QFont()
        projFont.setPointSize(7)
        self.sortBtn_proj.setFont(projFont)
        self.sortBtn_proj.setText("proj")
        self.sortBtn_proj.setStyleSheet("""
            QPushButton {
                border-radius: 0px; 
                border: 1px solid #333333;
                background-color: #444444;
            }""")
        self.buttonLayout.addWidget(self.sortBtn_proj)




        self.sortBtn_status = QPushButton(parent)
        self.sortBtn_status.setObjectName(label+"_sortBtn_status")
        #self.sortBtn_status.setMaximumSize(QSize(135, 17))
        statusFont = QFont()
        statusFont.setPointSize(7)
        self.sortBtn_status.setFont(statusFont)
        self.sortBtn_status.setText("Status")
        self.sortBtn_status.setStyleSheet("""
            QPushButton {
                border-radius: 0px; 
                border: 1px solid #333333;
                background-color: #444444;
            }""")        
        self.buttonLayout.addWidget(self.sortBtn_status)



        # 생성한 버튼의 각각의 크기비율설정
        self.buttonLayout.setStretch(0,1)
        self.buttonLayout.setStretch(1,12)
        self.buttonLayout.setStretch(2,3)
        self.buttonLayout.setStretch(3,6)

        # 리스트뷰 하이라이트 셋업을 위한 프레임위젯 셋팅
        self.listviewFrame = QFrame()
        self.listviewFrame.setObjectName(label+"_listviewFrame")        
        self.listviewFrame.setMinimumSize(260, 0)
        #self.listviewFrame.setMaximumSize(310, 0)        
        self.listviewFrame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #self.listviewFrame.setMinimumSize(scaleUI, 0)
        self.focusLayout = QHBoxLayout(self.listviewFrame) # 리스트뷰의 셀렉팅용의 레이아웃
        self.focusLayout.setObjectName(label+"_focusLayout")        
        self.listViewLayout.addWidget(self.listviewFrame)
        self.focusLayout.setSpacing(0)
        self.focusLayout.setContentsMargins(0,0,0,0)

        # 리스트뷰
        self.listView_day = ddlv.DropListView(self.manager, self.listviewFrame, self.listViewLayout, mainLoop)#, self.listviewFrame)
        self.listView_day.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.listView_day.setEditTriggers(QAbstractItemView.NoEditTriggers) # 더블클릭시에 에딧모드로 들어가지 않도록 함
        self.listView_day.setObjectName(listView)
        #listView_day.setMaximumSize(800, 10000)
        #self.listView_day.setMinimumSize(scaleUI, 0)

        self.listView_day.setMinimumSize(250, 0)
        #self.listView_day.setMaximumSize(300, 0)
        self.listView_day.installEventFilter(main)

        self.font_listView = QFont()
        self.font_listView.setPointSize(12)
        self.listView_day.setFont(self.font_listView)

        self.focusLayout.addWidget(self.listView_day)


        parentLayout.addWidget(self.splitter_layoutWidget)
        


        #return self.listView_day, self.listViewLayout

        self.model = self.listView_day.model()

        self.sortBtn_name.clicked.connect(lambda: main.sort_manager.sort_sch_listView_task(self, self.listView_day, self.label_day))
        self.sortBtn_status.clicked.connect(lambda: main.sort_manager.sort_sch_listView_status(self, self.listView_day, self.label_day))
        self.sortBtn_part.clicked.connect(lambda: main.sort_manager.sort_sch_listView_part(self, self.listView_day, self.label_day))
        self.sortBtn_proj.clicked.connect(lambda: main.sort_manager.sort_sch_listView_proj(self, self.listView_day, self.label_day))                


    def __del__(self):
        try:
            self.manager.clear_active_container(self)

        except RuntimeError:
            pass #  삭제된 객체 접근시 무시            




# 선택된 리스트뷰를 관리하는 클래스
class ActiveListviewManager:
    def __init__(self):
        self.current_active = None
        self.date = None
        self.listview = None
        self.active_containers = set() # 다중선택을 위한 집합
        #self.activeDic = {}
        self.activeDate = []

    def set_active_container(self, container, parentLayout, multi_select=False, ctrl_select=False, click_item=False, **kwargs):

        self.date = parentLayout.itemAt(0).widget().text()
        frame = parentLayout.itemAt(2).widget()
        self.listview = frame.findChild(QListView)
        
        selected_indexes = self.listview.selectionModel().selectedIndexes()
        
        
        # 컨트롤 마우스 클릭 또는 시프트 마우스클릭 / 빈공간 클릭
        if (ctrl_select==True and not click_item) or (multi_select==True and not click_item):

            # 이미 선택이 되어있는경우 선택을 해제
            if container in self.active_containers:
                container.setStyleSheet("")
                self.active_containers.remove(container)

                if self.date in self.activeDate:
                    self.activeDate.remove(self.date)

            # 새로 선택
            else:
                self.active_containers.add(container)
                if self.date not in self.activeDate:
                    self.activeDate.append(self.date)
                container.setStyleSheet("border: 2px solid #435276;")



        # 컨트롤 마우스 클릭 또는 시프트 마우스 클릭 / 아이템 클릭
        elif (ctrl_select and click_item) or (multi_select and click_item):

            if container not in self.active_containers:
                self.active_containers.add(container)
                if self.date not in self.activeDate:
                    self.activeDate.append(self.date)
                container.setStyleSheet("border: 2px solid #435276;")





        # 단일선택, 빈공간 클릭: 기존 선택 모두 초기화
        elif not multi_select and not click_item:
            for active in self.active_containers:
                try:
                    active.setStyleSheet("")

                except RuntimeError:
                    pass



            self.activeDate = [] # 현재 싱글 셀렉션이므로 기존에 선택되어 있던 날짜 모두 초기화

            if "mainProcess" in kwargs:

                mainProcess = kwargs["mainProcess"]
                mainProcess.clear_selection()

            self.active_containers.clear()
            self.active_containers.add(container)   
            self.activeDate.append(self.date)
            container.setStyleSheet("border: 2px solid #435276;")



        # 단일선택, 아이템 클릭: 
        elif not multi_select and click_item:
            for active in self.active_containers:
                try:
                    active.setStyleSheet("")

                except RuntimeError:
                    pass

            self.activeDate = [] # 현재 싱글 셀렉션이므로 기존에 선택되어 있던 날짜 모두 초기화
            self.active_containers.clear()
            self.active_containers.add(container)   
            self.activeDate.append(self.date)

            container.setStyleSheet("border: 2px solid #435276;")



    # 스케쥴 리스트뷰 한칸 이동을 하는경우 선택된 하이라이트도 함게 이동하게 하기
    def Move_sideway_setContainer(self, container, layout):
        self.active_containers.add(container)

        dateIndex = layout.itemAt(0).widget()
        date = dateIndex.text()

        if date in self.activeDate:
            #print (date)
            #print (self.activeDate)
            container.setStyleSheet("border: 2px solid #435276;")

        else:
            self.clear_active_container(container)            


    # 스케쥴 리스트뷰를 더하거나 지우는 경우에 이전에 하이라이트되었던 상태가 유지되게 하기
    #def keep_setContainer(self, container, layout)


    def clear_active_container(self, container):

        if container in self.active_containers:
            container.setStyleSheet("")
            self.active_containers.remove(container)
            #del self.activeDic[container]





