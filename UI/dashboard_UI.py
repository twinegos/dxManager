# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'performance_deshboardsZeDNv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dashboard_frm(object):
    def __init__(self):

        self.dashboard_frm = QFrame()
        self.dashboard_frm.resize(1286, 788)
        self.dashboard_frm.setFrameShape(QFrame.StyledPanel)
        self.dashboard_frm.setFrameShadow(QFrame.Sunken)
        self.dashboard_frm.setLineWidth(5)
        self.dashboard_frm.setMidLineWidth(5)
        self.horizontalLayout = QHBoxLayout(self.dashboard_frm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.totalData_frm = QFrame(self.dashboard_frm)
        self.totalData_frm.setObjectName(u"totalData_frm")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalData_frm.sizePolicy().hasHeightForWidth())
        self.totalData_frm.setSizePolicy(sizePolicy)
        self.totalData_frm.setMinimumSize(QSize(200, 0))
        self.totalData_frm.setFrameShape(QFrame.NoFrame)
        self.totalData_frm.setFrameShadow(QFrame.Sunken)
        self.totalData_frm.setLineWidth(5)
        self.totalData_frm.setMidLineWidth(5)
        self.verticalLayout = QVBoxLayout(self.totalData_frm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.sideBoxTitle = QLabel(self.totalData_frm)
        self.sideBoxTitle.setObjectName(u"sideBoxTitle")
        font = QFont()
        font.setPointSize(20)
        self.sideBoxTitle.setFont(font)

        self.verticalLayout.addWidget(self.sideBoxTitle, 0, Qt.AlignRight)

        self.tasks_layout = QHBoxLayout()
        self.tasks_layout.setObjectName(u"tasks_layout")
        self.tasks_label = QLabel(self.totalData_frm)
        self.tasks_label.setObjectName(u"tasks_label")

        self.tasks_layout.addWidget(self.tasks_label, 0, Qt.AlignHCenter)

        self.tasks_lineEdit = QLineEdit(self.totalData_frm)
        self.tasks_lineEdit.setObjectName(u"tasks_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tasks_lineEdit.sizePolicy().hasHeightForWidth())
        self.tasks_lineEdit.setSizePolicy(sizePolicy1)
        self.tasks_lineEdit.setMinimumSize(QSize(0, 50))
        self.tasks_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.tasks_layout.addWidget(self.tasks_lineEdit, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.tasks_layout)

        self.manday_layout = QHBoxLayout()
        self.manday_layout.setObjectName(u"manday_layout")
        self.manday_label = QLabel(self.totalData_frm)
        self.manday_label.setObjectName(u"manday_label")

        self.manday_layout.addWidget(self.manday_label, 0, Qt.AlignHCenter)

        self.manday_lineEdit = QLineEdit(self.totalData_frm)
        self.manday_lineEdit.setObjectName(u"manday_lineEdit")
        self.manday_lineEdit.setMinimumSize(QSize(0, 50))
        self.manday_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.manday_layout.addWidget(self.manday_lineEdit)


        self.verticalLayout.addLayout(self.manday_layout)

        self.actManday_layout = QHBoxLayout()
        self.actManday_layout.setObjectName(u"actManday_layout")
        self.actManday_label = QLabel(self.totalData_frm)
        self.actManday_label.setObjectName(u"actManday_label")

        self.actManday_layout.addWidget(self.actManday_label)

        self.actManday_lineEdit = QLineEdit(self.totalData_frm)
        self.actManday_lineEdit.setObjectName(u"actManday_lineEdit")
        self.actManday_lineEdit.setMinimumSize(QSize(0, 50))
        self.actManday_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.actManday_layout.addWidget(self.actManday_lineEdit)


        self.verticalLayout.addLayout(self.actManday_layout)

        self.achieve_frm = QFrame(self.totalData_frm)
        self.achieve_frm.setObjectName(u"achieve_frm")
        self.achieve_frm.setFrameShape(QFrame.StyledPanel)
        self.achieve_frm.setFrameShadow(QFrame.Sunken)
        self.achieve_frm.setLineWidth(5)
        self.achieve_frm.setMidLineWidth(5)
        self.horizontalLayout_5 = QHBoxLayout(self.achieve_frm)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.achieve_label = QLabel(self.achieve_frm)
        self.achieve_label.setObjectName(u"achieve_label")
        font1 = QFont()
        font1.setPointSize(11)
        self.achieve_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.achieve_label)

        self.achieve_ratio = QLabel(self.achieve_frm)
        self.achieve_ratio.setObjectName(u"achieve_ratio")
        font2 = QFont()
        font2.setPointSize(19)
        self.achieve_ratio.setFont(font2)

        self.horizontalLayout_5.addWidget(self.achieve_ratio, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.achieve_frm)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.difficulty_layout = QHBoxLayout()
        self.difficulty_layout.setObjectName(u"difficulty_layout")
        self.difficulty_label = QLabel(self.totalData_frm)
        self.difficulty_label.setObjectName(u"difficulty_label")

        self.difficulty_layout.addWidget(self.difficulty_label)

        self.difficulty_lineEdit = QLineEdit(self.totalData_frm)
        self.difficulty_lineEdit.setObjectName(u"difficulty_lineEdit")
        self.difficulty_lineEdit.setMinimumSize(QSize(0, 50))
        self.difficulty_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.difficulty_layout.addWidget(self.difficulty_lineEdit)


        self.verticalLayout.addLayout(self.difficulty_layout)

        self.evaluation_frm = QFrame(self.totalData_frm)
        self.evaluation_frm.setObjectName(u"evaluation_frm")
        self.evaluation_frm.setFrameShape(QFrame.StyledPanel)
        self.evaluation_frm.setFrameShadow(QFrame.Sunken)
        self.evaluation_frm.setLineWidth(5)
        self.evaluation_frm.setMidLineWidth(5)
        self.horizontalLayout_7 = QHBoxLayout(self.evaluation_frm)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.evaluation_label = QLabel(self.evaluation_frm)
        self.evaluation_label.setObjectName(u"evaluation_label")

        self.horizontalLayout_7.addWidget(self.evaluation_label)

        self.evaluation_value = QLabel(self.evaluation_frm)
        self.evaluation_value.setObjectName(u"evaluation_value")
        self.evaluation_value.setFont(font2)

        self.horizontalLayout_7.addWidget(self.evaluation_value, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.evaluation_frm)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.totalData_frm)

        self.memberData_frm = QFrame(self.dashboard_frm)
        self.memberData_frm.setObjectName(u"memberData_frm")
        self.memberData_frm.setFrameShape(QFrame.NoFrame)
        self.memberData_frm.setFrameShadow(QFrame.Sunken)
        self.memberData_frm.setLineWidth(5)
        self.memberData_frm.setMidLineWidth(1)
        self.horizontalLayout_8 = QHBoxLayout(self.memberData_frm)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.memberData_scroll = QScrollArea(self.memberData_frm)
        self.memberData_scroll.setObjectName(u"memberData_scroll")
        self.memberData_scroll.setAutoFillBackground(False)
        self.memberData_scroll.setStyleSheet(u"background-color: rgb(136, 138, 133);")        
        self.memberData_scroll.setWidgetResizable(True)
        self.memberData_contents = QWidget()
        self.memberData_contents.setObjectName(u"memberData_contents")
        self.memberData_contents.setGeometry(QRect(0, 0, 1022, 752))
        self.scrollContents_layout = QVBoxLayout(self.memberData_contents)
        self.scrollContents_layout.setObjectName(u"scrollContents_layout")
        self.memberData_scroll.setWidget(self.memberData_contents)

        self.horizontalLayout_8.addWidget(self.memberData_scroll)


        self.horizontalLayout.addWidget(self.memberData_frm)



        #dashboard_frm.setWindowTitle(QCoreApplication.translate("dashboard_frm", u"Frame", None))
        self.sideBoxTitle.setText("Total")
        self.tasks_label.setText("Tasks")
        self.tasks_lineEdit.setText("0")
        self.manday_label.setText("Manday")
        self.manday_lineEdit.setText("0")
        self.actManday_label.setText("Act Manday")
        self.actManday_lineEdit.setText("0")
        self.achieve_label.setText("Achievement R")
        self.achieve_ratio.setText("0 %")
        self.difficulty_label.setText("Difficulty Lv.")
        self.difficulty_lineEdit.setText("0")
        self.evaluation_label.setText("Evaluation")
        self.evaluation_value.setText("0")


        #QMetaObject.connectSlotsByName(self.dashboard_frm )


'''
 




    def __init__(self):
        self.dashboard_frm = QFrame()
        self.dashboard_frm.resize(1286, 788)

        self.verticalLayout = QVBoxLayout(self.dashboard_frm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.dashboard_frm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 330, 100, 36))

        self.verticalLayout.addWidget(self.pushButton)
'''




