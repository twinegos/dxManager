


from PySide2 import QtCore

from PySide2.QtCore import  *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import struct
import json
import os

currentPath = os.path.dirname(os.path.abspath(__file__))
#userID = os.popen("logname").read().strip()


"""
class CustomSortProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
"""



class DragDropModel(QAbstractListModel):

    def __init__(self, data=None, parent=None, sortColumn=None):
        super(DragDropModel, self).__init__()
        self._data = data or []
        self._background_colors = {}
        self._sort_order = Qt.AscendingOrder
        self._sort_column = sortColumn



    def setRowHidden(self, row, hide):
        if 0 <= row < len(self._data):
            if hide:
                self._hidden_rows.add(row)

            else:
                self._hidden_rows.discard(row)                
            index=self.index(row,0)
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True
        return False



    def isRowHidden(self, row):
        return row in self._hidden_rows




    def rowCount(self, parent=QModelIndex()):
        return len(self._data)


    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsEditable




    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row = index.row()

        if role == Qt.DisplayRole or role == Qt.UserRole:
            return self._data[row]

        if role == Qt.BackgroundRole:
            return self._background_colors.get(index.row())

        return None


    """
    def sort(self, column, order):
        if column == 1:

            self.beginResetModel()
            self._data.sort(key=lambda task: task[1], reverse = order == Qt.DescendingOrder)
            self._sort_order = order
            self.endResetModel()
    """

    def sort(self, column, order):

        if column != None and order != None:
            self.beginResetModel()
            self._sort_column = column
            self._data.sort(key=lambda task: task[self._sort_column], reverse = order == Qt.DescendingOrder)
            self._sort_order = order
            self.endResetModel()


    def setSortOrder(self, order):

        if self._sort_order != order:
            self._sort_order = order
            self.sort(self._sort_column, order)


    def getSortOrder(self):
        return self._sort_order
    

    def refereshModel(self, new_data):
        # 모델 리프레시 시 정렬상태 유지
        self.beginResetModel()
        self._data = new_data.copy()

        # 원래 정렬상태로 다시 정렬
        self._data.sort(key=lambda task: task[self._sort_column], reverse=self._sort_order == Qt.DescendingOrder)

        self.endResetModel()



    #(grade, text, progress, status, part)

    #def set_background_color(self, row, color):
    #    self.setData(index, color, Qt.BackgroundRole)


    def setData(self, index, value, role=Qt.EditRole):

        if role == Qt.BackgroundRole:
            self._background_colors[index.row()] = value

        #if not index.isValid() or role != Qt.EditRole:
        #    return False

        if role == Qt.EditRole:
            row = index.row()
            self._data[row][1] = value

        self.dataChanged.emit(index, index, [role])
        return True


    def set_background_color(self, row, color):
        index = self.index(row, 0)
        self.setData(index, color, Qt.BackgroundRole)


    def supportedDropActions(self):
        return Qt.MoveAction


    def mimeTypes(self):
        return ['application/x-qabstractitemmodeldatalist']


    def mimeData(self, indexes):
        mimeData = QMimeData()
        encodedData = QByteArray()
        stream = QDataStream(encodedData, QIODevice.WriteOnly)

        for index in indexes:
            if index.isValid():
                grade,text, progress, status, part = self.data(index, Qt.DisplayRole)
                stream.writeInt(index.row())
                stream.writeQString(grade)
                stream.writeQString(text)
                #stream.writeFloat(round(progress,2))
                stream.writeQString(progress)
                stream.writeQString(status)
                stream.writeQString(part)

        mimeData.setData('application/x-qabstractitemmodeldatalist', encodedData)
        return mimeData


    def dropMimeData(self, data, action, row, column, parent):
        if action == Qt.IgnoreAction:
            return True
        if not data.hasFormat('application/x-qabstractitemmodeldatalist'):
            return False
        if column > 0:
            return False


        encodedData = data.data('application/x-qabstractitemmodeldatalist')
        stream = QDataStream(encodedData, QIODevice.ReadOnly)
        newItems=[]
        while not stream.atEnd():
            source_row = stream.readInt32()
            grade = stream.readQString()
            text = stream.readQString()
            #progress = stream.readInt()
            progress = stream.readQString()
            status = stream.readQString()
            part = stream.readQString()            
            newItems.append((grade, text, progress, status, part))

        

        self.beginInsertRows(QModelIndex(), row, row + len(newItems) -1)
        for grade, text, progress, status, part in newItems:
            self._data.insert(row,(grade, text, progress, status, part))
            row += 1
        self.endInsertRows()
        return True



    def removeRows(self, row, count, parent):
        self.beginRemoveRows(parent, row, row + count - 1)
        del self._data[row:row+count]
        self.endRemoveRows()
        return True



    def insertRows(self, row, count, parent=QModelIndex(), items=[]):
        self.beginInsertRows(parent, row, row + count - 1)

        for item in items:
            self._data.insert(row, item)
            row += 1

        self.endInsertRows()
        return True









class ProgressDelegate(QStyledItemDelegate):

    def __init__(self, containDic=None, parent=None):
        super(ProgressDelegate, self).__init__()
        self._containDic = containDic



    def paint(self, painter, option, index):

        if not index.isValid():
            return

        data = index.data(Qt.DisplayRole)
        if data is None:
            return

        grade,text, progress, status, part = data

        # 선택했을때 아이템 전체 영역이 하이라이트 되도록 함
        # option.state => 선택됨/선택안됌, 포커스, 활성화상태등의 현재상태를 확인가능
        # option.rect => 아이템의 그려질 영역정보를 얻을수 있다
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, option.palette.highlight())

        # 지정된 백그라운드 색을 가져옴
        background = index.data(Qt.BackgroundRole)

        # 지정된 백그라운드 색이 있을 경우 아이템의 배경색을 지정된 색으로 변경
        if background:
            painter.fillRect(option.rect, background)        


        # Draw part ##########################################################################################
        partOption = QStyleOptionViewItem(option)
        self.initStyleOption(partOption, index)

        partRect = option.rect

        partOption.rect = partRect
        partOption.text = part

        partRect.setLeft(option.rect.left()) #int(option.rect.width()*0.2))#option.rect.left() + 10)

        QApplication.style().drawControl(QStyle.CE_ItemViewItem, partOption, painter)
        #######################################################################################################


        """
        # Draw grade ###############################################################################
        gradeOption = QStyleOptionViewItem(option)
        self.initStyleOption(gradeOption, index)
        gradeRect = option.rect

        gradeRect.setLeft(int(option.rect.width()*0.07))       
        gradeRect.setRight(option.rect.left() + int(option.rect.width()*1.75/3))

        gradeOption.rect = gradeRect
        gradeOption.text = grade
        QApplication.style().drawControl(QStyle.CE_ItemViewItem, gradeOption, painter)
        ###############################################################################################
        """





        # Draw text ###########################################################################################
        textOption = QStyleOptionViewItem(option)
        self.initStyleOption(textOption, index)
        textRect = option.rect

        textRect.setLeft(int(option.rect.width()*0.07))
        textRect.setRight(option.rect.left() + int(option.rect.width()*1.75/3))


        #textRect.setRight(option.rect.right() - 150)
        #textRect.setLeft(gradeRect.right())                
        #textRect.setRight(option.rect.left() + 30)        
        textOption.rect = textRect

        #if background:
        #    painter.fillRect(textOption.rect, background)
        textOption.text = text


        # Set the font and change the font size
        #font = option.font
        #font.setPointSize(10)
        #painter.setFont(font)


        # Change the text color for the main text

        #print (self._containDic)

        if self._containDic != None:
            if data in self._containDic:
                textOption.palette.setColor(QPalette.Text, QColor(100,100,100))
                #contain = self._containDic[data]

                #if contain == 1:
                #    textOption.palette.setColor(QPalette.Text, QColor(170,170,170))

        QApplication.style().drawControl(QStyle.CE_ItemViewItem, textOption, painter)
        ############################################################################################





        # Draw grade ###############################################################################
        gradeOption = QStyleOptionViewItem(option)
        self.initStyleOption(gradeOption, index)
        gradeRect = option.rect


        #gradeRect.setLeft(option.rect.left()) + int(textOption.rect.width()))        
        #gradeRect.setRight(textRect.right() + int(textOption.rect.width()*1/7))        

        gradeRect.setLeft(option.rect.right())# + int(textOption.rect.width()))        
        #gradeRect.setRight(textRect.right() + int(textOption.rect.width()*1/7))      
        gradeRect.setRight(option.rect.right()+50)      

        # Set the font and change the font size
        gradeFont = option.font
        gradeFont.setPointSize(8)
        gradeOption.font = gradeFont

        gradeOption.rect = gradeRect
        gradeOption.text = grade
        QApplication.style().drawControl(QStyle.CE_ItemViewItem, gradeOption, painter)
        ###############################################################################################




        # Draw progress bar ###########################################################################
        progressBarOption = QStyleOptionProgressBar()
        progressHeight = 15


        # 맨데이 프로그레스 바 영역 지정
        progressBarRect = QRect(
            textRect.right(), option.rect.top() + (option.rect.height() - progressHeight) // 2,
            int(textOption.rect.width()/5), 
            progressHeight
        )

        progressBarOption.rect = progressBarRect
        progressBarOption.minimum = 0
        progressBarOption.maximum = 100

        mandays = progress.split('/')
        act_manday = mandays[0]
        bd_manday = mandays[1]

        if act_manday == "None" or bd_manday == "None":
            progressRate = 0

        elif float(act_manday) == 0 or float(bd_manday) ==0:
            progressRate = 0

        elif float(bd_manday) != 0 and float(act_manday) != 0:
            progressRate = round((float(act_manday) / float(bd_manday))*100, 2)

        if progressRate > 100:
            progressRate = 100                     

        #progressBarOption.progress = progress
        progressBarOption.progress = progressRate
        progressBarOption.textVisible = True

        if act_manday != "None" and bd_manday != "None" :
            if float(act_manday) > float(bd_manday):
                progressBarOption.palette.setColor(QPalette.Highlight, QColor(94,29,35)) 

            else:
                progressBarOption.palette.setColor(QPalette.Highlight, QColor('#5d5d6d')) 

        QApplication.style().drawControl(QStyle.CE_ProgressBar, progressBarOption, painter)
        ####################################################################################################            




        #Draw status text
        statusOption = QStyleOptionViewItem(option)
        self.initStyleOption(statusOption, index)
        statusRect = option.rect
        statusRect.setLeft(progressBarRect.right() + 2)
        statusRect.setRight(progressBarRect.right() + 100)        

        statusOption.rect = statusRect
        statusOption.text = status

        # Set the font and change the font size for the status text
        statusFont = option.font
        statusFont.setPointSize(8)
        statusOption.font = statusFont


        # Change the text color for the status text
        if status == "Approved":
            statusOption.palette.setColor(QPalette.Text, QColor(105,51,193))

        elif status == "Ready":            
            statusOption.palette.setColor(QPalette.Text, QColor(208,208,114))

        elif status == "Retake":            
            statusOption.palette.setColor(QPalette.Text, QColor(201,33,30))            

        elif status == "In-Progress":            
            statusOption.palette.setColor(QPalette.Text, QColor(80, 245, 13))

        elif status == "OK":            
            statusOption.palette.setColor(QPalette.Text, QColor(129,182,239))    

        elif status == "Waiting":            
            statusOption.palette.setColor(QPalette.Text, QColor(153,153,153))    

        elif status == "Hold":            
            statusOption.palette.setColor(QPalette.Text, QColor(120,120,120))    

        elif status == "Omit":            
            statusOption.palette.setColor(QPalette.Text, QColor(100,100,100))    


        painter.setFont(statusOption.font)
        painter.setPen(statusOption.palette.color(QPalette.Text))

        QApplication.style().drawControl(QStyle.CE_ItemViewItem, statusOption, painter)
        
        #statusRect = QRect(progressBarRect.right(), option.rect.top(), )






    ##########################################################################################################
    ###################### 글자 폰트 크기를 가져와서 그 크기에따라 전체 넓이 조정 ################################
    ##########################################################################################################
    def sizeHint(self, option, index):
        size = super(ProgressDelegate, self).sizeHint(option, index)
        return QSize(size.width(), size.height())



class DragListView(QListView):
    def __init__(self, parent=None):
        super(DragListView, self).__init__(parent)
        self.setDragEnabled(True)
        self.setSelectionMode(QListView.ExtendedSelection)        
        #self.setStyleSheet("QListView { background-color: lightblue; }")
        self.setFocusPolicy(Qt.NoFocus) # 포커스 기능 없앰

        #header = self.header()
        #header.setSectionsClickable(True)
        #header.sectionClicked.connect(self.handle_sort)
        #self.setSortingEnabled(True)

    def startDrag(self, supported_actions):
        indexes = self.selectedIndexes()
        if not indexes:
            return

        mime_data = QMimeData()
        encoded_data = QByteArray()
        stream = QDataStream(encoded_data, QIODevice.WriteOnly)

        #dragged_items = [self.model().data(index, Qt.DisplayRole) for index in indexes]

        for index in indexes:
            if index.isValid():
                grade, text, progress, status, part = self.model().data(index, Qt.DisplayRole)
                stream.writeInt32(index.row())
                stream.writeQString(grade)
                stream.writeQString(text)
                #stream.writeInt32(progress)
                stream.writeQString(progress)
                stream.writeQString(status)
                stream.writeQString(part)                

        mime_data.setData("application/x-qabstractitemmodeldatalist", encoded_data)

        drag = QDrag(self)
        drag.setMimeData(mime_data)
        result = drag.exec_(supported_actions)#, items=dragged_items)
        print (result)


    """
    def setup_sorting(self):
        self.proxy_model = CustomSortProxyModel()
        listviewModel = self.model()
        self.proxy_model.setSourceModel(listviewModel)
        self.setModel(self.proxy_model)


    def sort_by_second_column(self):
        self.proxy_model.sort(1, Qt.DescendingOrder)
        print ("ddd")
    """










class DropListView(QListView):

    itemsDropped = Signal(list, str)

    #def __init__(self, model=None):
    def __init__(self, manager, container, parentLayout, mainLoop):#, model=None):
        super(DropListView, self).__init__()

        self.mainLoop = mainLoop
        self.manager = manager
        self.container = container
        self.parentLayout = parentLayout

        self.setAcceptDrops(True)
        self.setSelectionMode(QListView.ExtendedSelection)
        #self.setStyleSheet("QListView { background-color: lightblue; }")
        self.setMinimumSize(QSize(200,0))

        model = DragDropModel()
        self.setModel(model)
        delegate = ProgressDelegate()
        self.setItemDelegate(delegate)

        self.dropped_items = [] # 드랍된 아이템들을 저장하기 위한 변수
        #self.setFocusPolicy(Qt.NoFocus) # 포커스 기능 없앰




    def mousePressEvent(self, event):

        # 클릭 위치를 좌표계로 변환
        pos = self.mapFromParent(event.pos())

        # 해당 위치의 인덱스 확인
        index = self.indexAt(pos)
        click_item = index.isValid()
        

        #shift키, ctrl키 확인
        multi_select = bool(event.modifiers() & Qt.ShiftModifier)
        ctrl_select = bool(event.modifiers() & Qt.ControlModifier)

       
        self.manager.set_active_container(self.container, self.parentLayout, multi_select, ctrl_select, click_item, mainProcess=self.mainLoop)
        super().mousePressEvent(event)

        """
        if event.button() == Qt.LeftButton:
            self.manager.set_active_container(self.container)
        super().mousePressEvent(event)
        """





    def dropEvent(self, event):

        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            encoded_data = event.mimeData().data("application/x-qabstractitemmodeldatalist")            
            stream = QDataStream(encoded_data, QIODevice.ReadOnly)

            target_model = self.model()
            all_indexes = [target_model.index(row) for row in range(target_model.rowCount(QModelIndex()))]
            currItems = [target_model.data(index, Qt.DisplayRole) for index in all_indexes]

            self.dropped_items.clear()
            while not stream.atEnd():
                row = stream.readInt32()
                grade = stream.readQString()
                text = stream.readQString()
                #progress = stream.readInt32()
                progress = stream.readQString()
                status = stream.readQString()
                part = stream.readQString()
                data = (grade, text, progress, status, part)

                if data not in currItems:
                    self.dropped_items.append(data)

            row = self.model().rowCount(QModelIndex())
            self.model().dropMimeData(
                event.mimeData(),
                Qt.MoveAction,
                row,
                0,
                QModelIndex()
            )

            self.itemsDropped.emit(self.dropped_items, self.objectName())

            event.accept()

        else:
            event.ignore()
















    """
    def dropEvent(self, event):

        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            encoded_data = event.mimeData().data("application/x-qabstractitemmodeldatalist")
            stream = QDataStream(encoded_data, QIODevice.ReadOnly)

            #stream = QDataStream(encoded_data)

            target_model = self.model()
            all_indexes = [target_model.index(row) for row in range(target_model.rowCount(QModelIndex()))]
            currItems = [target_model.data(index, Qt.DisplayRole) for index in all_indexes]

            self.dropped_items.clear()
            while not stream.atEnd():
                row = stream.readInt32()
                grade = stream.readQString()
                text = stream.readQString()
                #progress = stream.readInt32()
                progress = stream.readQString()
                status = stream.readQString()
                part = stream.readQString()
                data = (grade, text, progress, status, part)

                if data not in currItems:
                    self.dropped_items.append(data)


            if self.dropped_items:
                target_model.insertRows(target_model.rowCount(QModelIndex()), len(self.dropped_items), QModelIndex(), items=self.dropped_items)

                '''
                if data not in currItems:
                    # Insert the data into the target model
                    target_model.insertRows(target_model.rowCount(QModelIndex()), 1, QModelIndex(), items=dropped_items)
                    target_model.setData(target_model.index(target_model.rowCount(QModelIndex()) - 1, 0), data)
                    self.dropped_items.append(data)
                '''
            self.itemsDropped.emit(self.dropped_items, self.objectName())


            event.accept()

        else:
            event.ignore()
    """












