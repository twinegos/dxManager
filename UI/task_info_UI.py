# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskInfo_dialogiiHZmV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(541, 248)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(16777215, 248))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.h_Layout_taskName = QHBoxLayout()
        self.h_Layout_taskName.setObjectName(u"h_Layout_taskName")
        self.h_Layout_taskName.setContentsMargins(31, 0, 0, 0)
        self.label_taskName = QLabel(Form)
        self.label_taskName.setObjectName(u"label_taskName")
        self.label_taskName.setMinimumSize(QSize(0, 45))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_taskName.setFont(font)

        self.h_Layout_taskName.addWidget(self.label_taskName, 0, Qt.AlignHCenter)

        self.v_Layout_status = QVBoxLayout()
        self.v_Layout_status.setObjectName(u"v_Layout_status")
        self.v_Layout_status.setContentsMargins(0, 10, 10, 10)
        self.frame_status = QFrame(Form)
        self.frame_status.setObjectName(u"frame_status")
        self.frame_status.setMinimumSize(QSize(80, 0))
        self.frame_status.setMaximumSize(QSize(16777215, 16))
        self.frame_status.setStyleSheet(u"background-color: rgb(52, 101, 164);")
        self.frame_status.setFrameShape(QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_status)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_status = QLabel(self.frame_status)
        self.label_status.setObjectName(u"label_status")
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        self.label_status.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_status, 0, Qt.AlignHCenter)


        self.v_Layout_status.addWidget(self.frame_status, 0, Qt.AlignHCenter)


        self.h_Layout_taskName.addLayout(self.v_Layout_status)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_Layout_taskName.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 7, -1)
        self.label_projectName = QLabel(Form)
        self.label_projectName.setObjectName(u"label_projectName")

        self.verticalLayout_3.addWidget(self.label_projectName)

        self.label_artistName = QLabel(Form)
        self.label_artistName.setObjectName(u"label_artistName")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_artistName.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_artistName, 0, Qt.AlignLeft)


        self.h_Layout_taskName.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.h_Layout_taskName)

        self.h_Layout_startEnd = QHBoxLayout()
        self.h_Layout_startEnd.setObjectName(u"h_Layout_startEnd")
        self.h_Spacer_startEnd = QSpacerItem(32, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.h_Layout_startEnd.addItem(self.h_Spacer_startEnd)

        self.label_startEndDate = QLabel(Form)
        self.label_startEndDate.setObjectName(u"label_startEndDate")
        self.label_startEndDate.setFont(font1)

        self.h_Layout_startEnd.addWidget(self.label_startEndDate)

        self.label_startDate = QLabel(Form)
        self.label_startDate.setObjectName(u"label_startDate")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_startDate.setFont(font3)

        self.h_Layout_startEnd.addWidget(self.label_startDate)

        self.label_startEndHyphen = QLabel(Form)
        self.label_startEndHyphen.setObjectName(u"label_startEndHyphen")

        self.h_Layout_startEnd.addWidget(self.label_startEndHyphen)

        self.label_endDate = QLabel(Form)
        self.label_endDate.setObjectName(u"label_endDate")
        self.label_endDate.setFont(font3)

        self.h_Layout_startEnd.addWidget(self.label_endDate)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_Layout_startEnd.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.h_Layout_startEnd)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.h_Layout_shotManday = QHBoxLayout()
        self.h_Layout_shotManday.setObjectName(u"h_Layout_shotManday")
        self.h_Layout_shotManday.setContentsMargins(31, -1, -1, -1)
        self.label_shotManday = QLabel(Form)
        self.label_shotManday.setObjectName(u"label_shotManday")
        self.label_shotManday.setMinimumSize(QSize(60, 0))
        self.label_shotManday.setMaximumSize(QSize(70, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_shotManday.setFont(font4)

        self.h_Layout_shotManday.addWidget(self.label_shotManday)

        self.progressBar_shotManday = QProgressBar(Form)
        self.progressBar_shotManday.setObjectName(u"progressBar_shotManday")
        self.progressBar_shotManday.setValue(24)

        self.h_Layout_shotManday.addWidget(self.progressBar_shotManday)

        self.shot_act_bid = QLabel(Form)
        self.shot_act_bid.setObjectName(u"shot_act_bid")
        self.shot_act_bid.setMinimumSize(QSize(60, 0))
        font5 = QFont()
        font5.setPointSize(10)
        self.shot_act_bid.setFont(font5)

        self.h_Layout_shotManday.addWidget(self.shot_act_bid)

        self.frame_grade = QFrame(Form)
        self.frame_grade.setObjectName(u"frame_grade")
        self.frame_grade.setFrameShape(QFrame.StyledPanel)
        self.frame_grade.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_grade)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_grade = QLabel(self.frame_grade)
        self.label_grade.setObjectName(u"label_grade")
        font6 = QFont()
        font6.setPointSize(15)
        self.label_grade.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label_grade)


        self.h_Layout_shotManday.addWidget(self.frame_grade)

        self.frame_value = QFrame(Form)
        self.frame_value.setObjectName(u"frame_value")
        self.frame_value.setFrameShape(QFrame.StyledPanel)
        self.frame_value.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_value)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.combo_evaluation = QComboBox(self.frame_value)
        self.combo_evaluation.setObjectName(u"combo_evaluation")
        self.combo_evaluation.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.combo_evaluation)


        self.h_Layout_shotManday.addWidget(self.frame_value)


        self.verticalLayout.addLayout(self.h_Layout_shotManday)

        self.v_Layout_taskInfo = QVBoxLayout()
        self.v_Layout_taskInfo.setSpacing(6)
        self.v_Layout_taskInfo.setObjectName(u"v_Layout_taskInfo")
        self.frame_taskInfo = QFrame(Form)
        self.frame_taskInfo.setObjectName(u"frame_taskInfo")
        self.frame_taskInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_taskInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_taskInfo)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.h_Layout_projManday = QHBoxLayout()
        self.h_Layout_projManday.setSpacing(13)
        self.h_Layout_projManday.setObjectName(u"h_Layout_projManday")
        self.h_Layout_projManday.setContentsMargins(0, -1, -1, -1)
        self.label_projManday = QLabel(self.frame_taskInfo)
        self.label_projManday.setObjectName(u"label_projManday")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_projManday.sizePolicy().hasHeightForWidth())
        self.label_projManday.setSizePolicy(sizePolicy1)
        self.label_projManday.setMinimumSize(QSize(110, 20))
        self.label_projManday.setFont(font5)
        self.label_projManday.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.h_Layout_projManday.addWidget(self.label_projManday)

        self.progressBar_projManday = QProgressBar(self.frame_taskInfo)
        self.progressBar_projManday.setObjectName(u"progressBar_projManday")
        self.progressBar_projManday.setMinimumSize(QSize(0, 10))
        self.progressBar_projManday.setMaximumSize(QSize(10000, 10))
        self.progressBar_projManday.setBaseSize(QSize(0, 10))
        self.progressBar_projManday.setValue(24)

        self.h_Layout_projManday.addWidget(self.progressBar_projManday)

        self.proj_act_bid = QLabel(self.frame_taskInfo)
        self.proj_act_bid.setObjectName(u"proj_act_bid")
        sizePolicy1.setHeightForWidth(self.proj_act_bid.sizePolicy().hasHeightForWidth())
        self.proj_act_bid.setSizePolicy(sizePolicy1)
        self.proj_act_bid.setMinimumSize(QSize(60, 0))
        self.proj_act_bid.setFont(font5)

        self.h_Layout_projManday.addWidget(self.proj_act_bid)

        self.h_Layout_projManday.setStretch(0, 3)
        self.h_Layout_projManday.setStretch(1, 8)
        self.h_Layout_projManday.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.h_Layout_projManday)

        self.h_Layout_projShot = QHBoxLayout()
        self.h_Layout_projShot.setSpacing(13)
        self.h_Layout_projShot.setObjectName(u"h_Layout_projShot")
        self.label_shots = QLabel(self.frame_taskInfo)
        self.label_shots.setObjectName(u"label_shots")
        sizePolicy1.setHeightForWidth(self.label_shots.sizePolicy().hasHeightForWidth())
        self.label_shots.setSizePolicy(sizePolicy1)
        self.label_shots.setMinimumSize(QSize(110, 20))
        self.label_shots.setFont(font5)
        self.label_shots.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.h_Layout_projShot.addWidget(self.label_shots)

        self.progressBar_projShots = QProgressBar(self.frame_taskInfo)
        self.progressBar_projShots.setObjectName(u"progressBar_projShots")
        self.progressBar_projShots.setMinimumSize(QSize(0, 10))
        self.progressBar_projShots.setMaximumSize(QSize(10000, 10))
        self.progressBar_projShots.setValue(24)

        self.h_Layout_projShot.addWidget(self.progressBar_projShots)

        self.proj_app_all = QLabel(self.frame_taskInfo)
        self.proj_app_all.setObjectName(u"proj_app_all")
        sizePolicy1.setHeightForWidth(self.proj_app_all.sizePolicy().hasHeightForWidth())
        self.proj_app_all.setSizePolicy(sizePolicy1)
        self.proj_app_all.setMinimumSize(QSize(60, 0))
        self.proj_app_all.setFont(font5)

        self.h_Layout_projShot.addWidget(self.proj_app_all)

        self.h_Layout_projShot.setStretch(0, 3)
        self.h_Layout_projShot.setStretch(1, 8)
        self.h_Layout_projShot.setStretch(2, 2)

        self.verticalLayout_2.addLayout(self.h_Layout_projShot)


        self.v_Layout_taskInfo.addWidget(self.frame_taskInfo)


        self.verticalLayout.addLayout(self.v_Layout_taskInfo)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_taskName.setText(QCoreApplication.translate("Form", u"TASK_NAME", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"status", None))
        self.label_projectName.setText(QCoreApplication.translate("Form", u"Project", None))
        self.label_artistName.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_startEndDate.setText(QCoreApplication.translate("Form", u"Start/End :", None))
        self.label_startDate.setText(QCoreApplication.translate("Form", u"start", None))
        self.label_startEndHyphen.setText(QCoreApplication.translate("Form", u"    -    ", None))
        self.label_endDate.setText(QCoreApplication.translate("Form", u"end", None))
        self.label_shotManday.setText(QCoreApplication.translate("Form", u"Manday", None))
        self.shot_act_bid.setText(QCoreApplication.translate("Form", u"act / bid", None))
        self.label_grade.setText(QCoreApplication.translate("Form", u"G", None))
        self.label_projManday.setText(QCoreApplication.translate("Form", u"\ud504\ub85c\uc81d\ud2b8 \ub9e8\ub370\uc774 :", None))
        self.proj_act_bid.setText(QCoreApplication.translate("Form", u"act / bid", None))
        self.label_shots.setText(QCoreApplication.translate("Form", u"\uc804\uccb4 \uc9c4\ud589\ub960 :", None))
        self.proj_app_all.setText(QCoreApplication.translate("Form", u"app / all", None))
    # retranslateUi

