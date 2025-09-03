# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leadMainWindowwCSkwB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


currentPath = os.path.dirname(os.path.abspath(__file__))
ListViewPath = os.path.dirname(currentPath) + "/class"

sys.path.append(ListViewPath)
import dragDropListView as DD


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1166, 993)
        self.actionEdit_member = QAction(MainWindow)
        self.actionEdit_member.setObjectName(u"actionEdit_member")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category_frm = QFrame(self.centralwidget)
        self.category_frm.setObjectName(u"category_frm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.category_frm.sizePolicy().hasHeightForWidth())
        self.category_frm.setSizePolicy(sizePolicy1)
        self.category_frm.setMinimumSize(QSize(200, 0))
        self.category_frm.setMaximumSize(QSize(200, 16777215))
        self.category_frm.setBaseSize(QSize(0, 0))
        self.category_frm.setFrameShape(QFrame.StyledPanel)
        self.category_frm.setFrameShadow(QFrame.Sunken)
        self.category_frm.setLineWidth(5)
        self.category_frm.setMidLineWidth(5)
        self.verticalLayout_2 = QVBoxLayout(self.category_frm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teamLabel = QLabel(self.category_frm)
        self.teamLabel.setObjectName(u"teamLabel")
        self.teamLabel.setMinimumSize(QSize(0, 25))
        self.teamLabel.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(13)
        self.teamLabel.setFont(font)
        self.teamLabel.setMargin(6)
        self.teamLabel.setIndent(6)

        self.verticalLayout_2.addWidget(self.teamLabel)

        self.frame_2 = QFrame(self.category_frm)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(1677215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 6, -1, -1)
        self.artistNameLabel = QLabel(self.frame_2)
        self.artistNameLabel.setObjectName(u"artistNameLabel")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setKerning(True)
        self.artistNameLabel.setFont(font1)
        self.artistNameLabel.setLayoutDirection(Qt.LeftToRight)
        self.artistNameLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.artistNameLabel)

        self.artistNameLabel_EN = QLabel(self.frame_2)
        self.artistNameLabel_EN.setObjectName(u"artistNameLabel_EN")

        self.horizontalLayout_6.addWidget(self.artistNameLabel_EN, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.scheduleView_btn = QPushButton(self.category_frm)
        self.scheduleView_btn.setObjectName(u"scheduleView_btn")

        self.verticalLayout_2.addWidget(self.scheduleView_btn)

        self.dashboard_btn = QPushButton(self.category_frm)
        self.dashboard_btn.setObjectName(u"dashboard_btn")

        self.verticalLayout_2.addWidget(self.dashboard_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.showAllTask_checkBox = QCheckBox(self.category_frm)
        self.showAllTask_checkBox.setObjectName(u"showAllTask_checkBox")
        self.showAllTask_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.showAllTask_checkBox)

        self.sel_allProj_checkBox = QCheckBox(self.category_frm)
        self.sel_allProj_checkBox.setObjectName(u"sel_allProj_checkBox")
        self.sel_allProj_checkBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.sel_allProj_checkBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.team_treeView = QTreeView(self.category_frm)
        self.team_treeView.setObjectName(u"team_treeView")
        self.team_treeView.setMinimumSize(QSize(0, 0))
        self.team_treeView.setSelectionMode(QAbstractItemView.NoSelection)
        self.team_treeView.setRootIsDecorated(True)
        self.team_treeView.setUniformRowHeights(False)
        self.team_treeView.header().setVisible(True)

        self.verticalLayout_2.addWidget(self.team_treeView)


        self.horizontalLayout.addWidget(self.category_frm)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.leftSide_QVBoxLayout = QVBoxLayout(self.layoutWidget)
        self.leftSide_QVBoxLayout.setSpacing(0)
        self.leftSide_QVBoxLayout.setObjectName(u"leftSide_QVBoxLayout")
        self.leftSide_QVBoxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.leftSide_QVBoxLayout.setContentsMargins(1, 0, 0, 0)
        self.leftSide_frame = QFrame(self.layoutWidget)
        self.leftSide_frame.setObjectName(u"leftSide_frame")
        sizePolicy.setHeightForWidth(self.leftSide_frame.sizePolicy().hasHeightForWidth())
        self.leftSide_frame.setSizePolicy(sizePolicy)
        self.leftSide_frame.setMinimumSize(QSize(0, 0))
        self.leftSide_frame.setMaximumSize(QSize(16777215, 16777215))
        self.leftSide_frame.setBaseSize(QSize(0, 0))
        self.leftSide_frame.setFocusPolicy(Qt.NoFocus)
        self.leftSide_frame.setFrameShape(QFrame.StyledPanel)
        self.leftSide_frame.setFrameShadow(QFrame.Sunken)
        self.leftSide_frame.setLineWidth(5)
        self.leftSide_frame.setMidLineWidth(5)
        self.verticalLayout_5 = QVBoxLayout(self.leftSide_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter_2 = QSplitter(self.leftSide_frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.verticalLayoutWidget = QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_show = QLabel(self.verticalLayoutWidget)
        self.label_show.setObjectName(u"label_show")
        font2 = QFont()
        font2.setFamily(u"Cantarell")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_show.setFont(font2)
        self.label_show.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_show.setIndent(1)

        self.verticalLayout.addWidget(self.label_show)

        self.projectListView = QListView(self.verticalLayoutWidget)
        self.projectListView.setObjectName(u"projectListView")
        sizePolicy.setHeightForWidth(self.projectListView.sizePolicy().hasHeightForWidth())
        self.projectListView.setSizePolicy(sizePolicy)
        self.projectListView.setFrameShape(QFrame.StyledPanel)
        self.projectListView.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout.addWidget(self.projectListView)

        self.verticalSpacer_2 = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.splitter_2.addWidget(self.verticalLayoutWidget)
        self.layoutWidget1 = QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label)

        self.reload_Button = QPushButton(self.layoutWidget1)
        self.reload_Button.setObjectName(u"reload_Button")
        self.reload_Button.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_9.addWidget(self.reload_Button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sortBtn_part = QPushButton(self.layoutWidget1)
        self.sortBtn_part.setObjectName(u"sortBtn_part")
        self.sortBtn_part.setMaximumSize(QSize(24, 25))
        font4 = QFont()
        font4.setPointSize(9)
        self.sortBtn_part.setFont(font4)

        self.horizontalLayout_3.addWidget(self.sortBtn_part)

        self.sortBtn_name = QPushButton(self.layoutWidget1)
        self.sortBtn_name.setObjectName(u"sortBtn_name")
        self.sortBtn_name.setMinimumSize(QSize(150, 0))
        self.sortBtn_name.setMaximumSize(QSize(500, 25))
        self.sortBtn_name.setFont(font4)

        self.horizontalLayout_3.addWidget(self.sortBtn_name)

        self.sortBtn_proj = QPushButton(self.layoutWidget1)
        self.sortBtn_proj.setObjectName(u"sortBtn_proj")
        self.sortBtn_proj.setMaximumSize(QSize(500, 25))
        self.sortBtn_proj.setFont(font4)

        self.horizontalLayout_3.addWidget(self.sortBtn_proj)

        self.sortBtn_status = QPushButton(self.layoutWidget1)
        self.sortBtn_status.setObjectName(u"sortBtn_status")
        self.sortBtn_status.setMaximumSize(QSize(500, 25))
        self.sortBtn_status.setFont(font4)

        self.horizontalLayout_3.addWidget(self.sortBtn_status)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 7)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 4)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.shotListView = DD.DragListView(self.leftSide_frame)
        self.shotListView.setObjectName(u"shotListView")
        sizePolicy.setHeightForWidth(self.shotListView.sizePolicy().hasHeightForWidth())
        self.shotListView.setSizePolicy(sizePolicy)
        self.shotListView.setMinimumSize(QSize(0, 0))
        self.shotListView.setMaximumSize(QSize(16777215, 16777215))
        self.shotListView.setBaseSize(QSize(0, 0))
        self.shotListView.setDragEnabled(True)
        self.shotListView.setDragDropOverwriteMode(True)
        self.shotListView.setDragDropMode(QAbstractItemView.DragDrop)
        self.shotListView.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.shotListView)

        self.splitter_2.addWidget(self.layoutWidget1)

        self.verticalLayout_5.addWidget(self.splitter_2)


        self.leftSide_QVBoxLayout.addWidget(self.leftSide_frame)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.schedule_layout = QVBoxLayout(self.layoutWidget2)
        self.schedule_layout.setSpacing(0)
        self.schedule_layout.setObjectName(u"schedule_layout")
        self.schedule_layout.setContentsMargins(0, 0, 0, 0)
        self.mainInfo_layout = QVBoxLayout()
        self.mainInfo_layout.setObjectName(u"mainInfo_layout")

        self.schedule_layout.addLayout(self.mainInfo_layout)

        self.splitter.addWidget(self.layoutWidget2)

        self.horizontalLayout.addWidget(self.splitter)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.saveBtn_layout = QHBoxLayout()
        self.saveBtn_layout.setSpacing(6)
        self.saveBtn_layout.setObjectName(u"saveBtn_layout")
        self.saveBtn_layout.setContentsMargins(-1, -1, 10, -1)
        self.saveBtn_spc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.saveBtn_layout.addItem(self.saveBtn_spc)

        self.deadlineButton = QPushButton(self.centralwidget)
        self.deadlineButton.setObjectName(u"deadlineButton")
        self.deadlineButton.setMinimumSize(QSize(120, 50))

        self.saveBtn_layout.addWidget(self.deadlineButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy3)
        self.saveButton.setMinimumSize(QSize(0, 50))
        self.saveButton.setMaximumSize(QSize(16777215, 70))

        self.saveBtn_layout.addWidget(self.saveButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 70))

        self.saveBtn_layout.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.saveBtn_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1166, 33))
        self.menuPreferences = QMenu(self.menubar)
        self.menuPreferences.setObjectName(u"menuPreferences")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menuPreferences.addAction(self.actionEdit_member)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionEdit_member.setText(QCoreApplication.translate("MainWindow", u"Edit member", None))
        self.teamLabel.setText(QCoreApplication.translate("MainWindow", u"team", None))
        self.artistNameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.artistNameLabel_EN.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.scheduleView_btn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.showAllTask_checkBox.setText(QCoreApplication.translate("MainWindow", u"Show All Tasks", None))
        self.sel_allProj_checkBox.setText(QCoreApplication.translate("MainWindow", u"Assigned Project", None))
        self.label_show.setText(QCoreApplication.translate("MainWindow", u"SHOW", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TASK", None))
        self.reload_Button.setText("")
        self.sortBtn_part.setText(QCoreApplication.translate("MainWindow", u"\ud300", None))
        self.sortBtn_name.setText(QCoreApplication.translate("MainWindow", u"\ud0dc\uc2a4\ud06c", None))
        self.sortBtn_proj.setText(QCoreApplication.translate("MainWindow", u"\ud504\ub85c\uc81d\ud2b8", None))
        self.sortBtn_status.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None))
        self.deadlineButton.setText(QCoreApplication.translate("MainWindow", u"This Week", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuPreferences.setTitle(QCoreApplication.translate("MainWindow", u"Preferences", None))
    # retranslateUi