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
        MainWindow.resize(889, 975)
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
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.category_frm = QFrame(self.centralwidget)
        self.category_frm.setObjectName(u"category_frm")
        self.category_frm.setMinimumSize(QSize(220, 0))
        self.category_frm.setMaximumSize(QSize(170, 16777215))
        self.category_frm.setFrameShape(QFrame.StyledPanel)
        self.category_frm.setFrameShadow(QFrame.Sunken)
        self.category_frm.setLineWidth(5)
        self.category_frm.setMidLineWidth(5)
        self.verticalLayout_2 = QVBoxLayout(self.category_frm)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(150, 16777215))
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

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.scheduleView_btn = QPushButton(self.category_frm)
        self.scheduleView_btn.setObjectName(u"scheduleView_btn")

        self.verticalLayout_2.addWidget(self.scheduleView_btn)

        self.dashboard_btn = QPushButton(self.category_frm)
        self.dashboard_btn.setObjectName(u"dashboard_btn")

        self.verticalLayout_2.addWidget(self.dashboard_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.team_treeView = QTreeView(self.category_frm)
        self.team_treeView.setObjectName(u"team_treeView")
        self.team_treeView.setMinimumSize(QSize(0, 640))
        self.team_treeView.setSelectionMode(QAbstractItemView.NoSelection)
        self.team_treeView.setRootIsDecorated(True)
        self.team_treeView.setUniformRowHeights(False)
        self.team_treeView.header().setVisible(True)

        self.verticalLayout_2.addWidget(self.team_treeView)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.verticalLayout.addWidget(self.category_frm)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.leftSide_QVBoxLayout = QVBoxLayout()
        self.leftSide_QVBoxLayout.setSpacing(0)
        self.leftSide_QVBoxLayout.setObjectName(u"leftSide_QVBoxLayout")
        self.leftSide_QVBoxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.leftSide_QVBoxLayout.setContentsMargins(1, 0, 0, -1)
        self.leftSide_frame = QFrame(self.centralwidget)
        self.leftSide_frame.setObjectName(u"leftSide_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftSide_frame.sizePolicy().hasHeightForWidth())
        self.leftSide_frame.setSizePolicy(sizePolicy2)
        self.leftSide_frame.setMinimumSize(QSize(340, 0))
        self.leftSide_frame.setMaximumSize(QSize(300, 16777215))
        self.leftSide_frame.setFocusPolicy(Qt.NoFocus)
        self.leftSide_frame.setFrameShape(QFrame.StyledPanel)
        self.leftSide_frame.setFrameShadow(QFrame.Sunken)
        self.leftSide_frame.setLineWidth(5)
        self.leftSide_frame.setMidLineWidth(5)
        self.verticalLayout_9 = QVBoxLayout(self.leftSide_frame)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_show = QLabel(self.leftSide_frame)
        self.label_show.setObjectName(u"label_show")
        font2 = QFont()
        font2.setFamily(u"Cantarell")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_show.setFont(font2)
        self.label_show.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_show.setIndent(1)

        self.verticalLayout_9.addWidget(self.label_show)

        self.projectListView = QListView(self.leftSide_frame)
        self.projectListView.setObjectName(u"projectListView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.projectListView.sizePolicy().hasHeightForWidth())
        self.projectListView.setSizePolicy(sizePolicy3)
        self.projectListView.setFrameShape(QFrame.StyledPanel)
        self.projectListView.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_9.addWidget(self.projectListView)

        self.verticalSpacer_2 = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.leftSide_frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.verticalLayout_9.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sortBtn_part = QPushButton(self.leftSide_frame)
        self.sortBtn_part.setObjectName(u"sortBtn_part")
        self.sortBtn_part.setMaximumSize(QSize(24, 25))
        font4 = QFont()
        font4.setPointSize(9)
        self.sortBtn_part.setFont(font4)

        self.horizontalLayout_3.addWidget(self.sortBtn_part)

        self.sortBtn_name = QPushButton(self.leftSide_frame)
        self.sortBtn_name.setObjectName(u"sortBtn_name")
        self.sortBtn_name.setMaximumSize(QSize(16777215, 25))
        self.sortBtn_name.setFont(font4)

        self.horizontalLayout_3.addWidget(self.sortBtn_name)

        self.sortBtn_status = QPushButton(self.leftSide_frame)
        self.sortBtn_status.setObjectName(u"sortBtn_status")
        self.sortBtn_status.setMaximumSize(QSize(125, 25))
        self.sortBtn_status.setFont(font4)

        self.horizontalLayout_3.addWidget(self.sortBtn_status)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.shotListView = DD.DragListView(self.leftSide_frame)
        self.shotListView.setObjectName(u"shotListView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.shotListView.sizePolicy().hasHeightForWidth())
        self.shotListView.setSizePolicy(sizePolicy4)
        self.shotListView.setMinimumSize(QSize(0, 200))
        self.shotListView.setMaximumSize(QSize(16777209, 16777215))
        self.shotListView.setDragEnabled(True)
        self.shotListView.setDragDropOverwriteMode(True)
        self.shotListView.setDragDropMode(QAbstractItemView.DragDrop)
        self.shotListView.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.shotListView)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.leftSide_QVBoxLayout.addWidget(self.leftSide_frame)


        self.horizontalLayout.addLayout(self.leftSide_QVBoxLayout)

        self.schedule_layout = QVBoxLayout()
        self.schedule_layout.setSpacing(0)
        self.schedule_layout.setObjectName(u"schedule_layout")
        self.mainInfo_layout = QVBoxLayout()
        self.mainInfo_layout.setObjectName(u"mainInfo_layout")

        self.schedule_layout.addLayout(self.mainInfo_layout)


        self.horizontalLayout.addLayout(self.schedule_layout)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.saveBtn_layout = QHBoxLayout()
        self.saveBtn_layout.setSpacing(6)
        self.saveBtn_layout.setObjectName(u"saveBtn_layout")
        self.saveBtn_layout.setContentsMargins(-1, -1, 10, -1)
        self.saveBtn_spc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.saveBtn_layout.addItem(self.saveBtn_spc)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy5)
        self.saveButton.setMaximumSize(QSize(16777215, 70))

        self.saveBtn_layout.addWidget(self.saveButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 70))

        self.saveBtn_layout.addWidget(self.pushButton_3)


        self.verticalLayout_8.addLayout(self.saveBtn_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 889, 33))
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
        self.label_show.setText(QCoreApplication.translate("MainWindow", u"SHOW", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TASK", None))
        self.sortBtn_part.setText(QCoreApplication.translate("MainWindow", u"\ud300", None))
        self.sortBtn_name.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984", None))
        self.sortBtn_status.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuPreferences.setTitle(QCoreApplication.translate("MainWindow", u"Preferences", None))
    # retranslateUi

