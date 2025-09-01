# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dayScheduleDynJuGQhm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_daySchedule_frame(object):
    def setupUi(self, daySchedule_frame):
        if not daySchedule_frame.objectName():
            daySchedule_frame.setObjectName(u"daySchedule_frame")
        daySchedule_frame.resize(1114, 836)
        daySchedule_frame.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(daySchedule_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.daySchedule_rootLayout = QVBoxLayout()
        self.daySchedule_rootLayout.setSpacing(0)
        self.daySchedule_rootLayout.setObjectName(u"daySchedule_rootLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(daySchedule_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(500, 0))
        self.frame_2.setMaximumSize(QSize(500, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_year = QComboBox(self.frame_2)
        self.comboBox_year.setObjectName(u"comboBox_year")
        self.comboBox_year.setMaximumSize(QSize(250, 16777215))
        self.comboBox_year.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_3.addWidget(self.comboBox_year)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.daySchedule_rootLayout.addLayout(self.horizontalLayout_5)

        self.Date_display_layout = QHBoxLayout()
        self.Date_display_layout.setObjectName(u"Date_display_layout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backwardDayButton = QPushButton(daySchedule_frame)
        self.backwardDayButton.setObjectName(u"backwardDayButton")
        self.backwardDayButton.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_2.addWidget(self.backwardDayButton)


        self.Date_display_layout.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(daySchedule_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(500, 0))
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.start_month = QLabel(self.frame)
        self.start_month.setObjectName(u"start_month")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.start_month.setFont(font)

        self.horizontalLayout_7.addWidget(self.start_month)

        self.startDate_dot = QLabel(self.frame)
        self.startDate_dot.setObjectName(u"startDate_dot")
        self.startDate_dot.setFont(font)

        self.horizontalLayout_7.addWidget(self.startDate_dot)

        self.start_day = QLabel(self.frame)
        self.start_day.setObjectName(u"start_day")
        self.start_day.setFont(font)

        self.horizontalLayout_7.addWidget(self.start_day)

        self.startDate_wave = QLabel(self.frame)
        self.startDate_wave.setObjectName(u"startDate_wave")
        self.startDate_wave.setFont(font)

        self.horizontalLayout_7.addWidget(self.startDate_wave)

        self.comboBox_month = QComboBox(self.frame)
        self.comboBox_month.setObjectName(u"comboBox_month")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_month.sizePolicy().hasHeightForWidth())
        self.comboBox_month.setSizePolicy(sizePolicy1)
        self.comboBox_month.setMinimumSize(QSize(100, 80))
        self.comboBox_month.setFont(font)

        self.horizontalLayout_7.addWidget(self.comboBox_month)

        self.comboBox_day = QComboBox(self.frame)
        self.comboBox_day.setObjectName(u"comboBox_day")
        self.comboBox_day.setMinimumSize(QSize(150, 80))
        self.comboBox_day.setFont(font)

        self.horizontalLayout_7.addWidget(self.comboBox_day)


        self.Date_display_layout.addWidget(self.frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.forwardDayButton = QPushButton(daySchedule_frame)
        self.forwardDayButton.setObjectName(u"forwardDayButton")
        self.forwardDayButton.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_6.addWidget(self.forwardDayButton)


        self.Date_display_layout.addLayout(self.horizontalLayout_6)


        self.daySchedule_rootLayout.addLayout(self.Date_display_layout)

        self.verticalSpacer_3 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.daySchedule_rootLayout.addItem(self.verticalSpacer_3)

        self.status_layout = QHBoxLayout()
        self.status_layout.setObjectName(u"status_layout")

        self.daySchedule_rootLayout.addLayout(self.status_layout)

        self.listViewNum_layout = QHBoxLayout()
        self.listViewNum_layout.setSpacing(6)
        self.listViewNum_layout.setObjectName(u"listViewNum_layout")
        self.listViewNum_layout.setContentsMargins(-1, 0, -1, 5)
        self.listViewNumSlider = QSlider(daySchedule_frame)
        self.listViewNumSlider.setObjectName(u"listViewNumSlider")
        self.listViewNumSlider.setMinimumSize(QSize(250, 0))
        self.listViewNumSlider.setMaximumSize(QSize(16777215, 16777215))
        self.listViewNumSlider.setMinimum(1)
        self.listViewNumSlider.setMaximum(31)
        self.listViewNumSlider.setSingleStep(1)
        self.listViewNumSlider.setPageStep(10)
        self.listViewNumSlider.setValue(5)
        self.listViewNumSlider.setOrientation(Qt.Horizontal)
        self.listViewNumSlider.setTickPosition(QSlider.NoTicks)

        self.listViewNum_layout.addWidget(self.listViewNumSlider)

        self.listViewNum_lineEdit = QLineEdit(daySchedule_frame)
        self.listViewNum_lineEdit.setObjectName(u"listViewNum_lineEdit")
        self.listViewNum_lineEdit.setMaximumSize(QSize(50, 16777215))
        self.listViewNum_lineEdit.setMaxLength(31)
        self.listViewNum_lineEdit.setAlignment(Qt.AlignCenter)

        self.listViewNum_layout.addWidget(self.listViewNum_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.listViewNum_layout.addItem(self.horizontalSpacer_3)

        self.checkBox_ready_v = QCheckBox(daySchedule_frame)
        self.checkBox_ready_v.setObjectName(u"checkBox_ready_v")
        font1 = QFont()
        font1.setPointSize(9)
        self.checkBox_ready_v.setFont(font1)
        self.checkBox_ready_v.setChecked(True)

        self.listViewNum_layout.addWidget(self.checkBox_ready_v)

        self.checkBox_inprogress_v = QCheckBox(daySchedule_frame)
        self.checkBox_inprogress_v.setObjectName(u"checkBox_inprogress_v")
        self.checkBox_inprogress_v.setFont(font1)
        self.checkBox_inprogress_v.setChecked(True)

        self.listViewNum_layout.addWidget(self.checkBox_inprogress_v)

        self.checkBox_ok_v = QCheckBox(daySchedule_frame)
        self.checkBox_ok_v.setObjectName(u"checkBox_ok_v")
        self.checkBox_ok_v.setFont(font1)
        self.checkBox_ok_v.setChecked(True)

        self.listViewNum_layout.addWidget(self.checkBox_ok_v)

        self.checkBox_review_v = QCheckBox(daySchedule_frame)
        self.checkBox_review_v.setObjectName(u"checkBox_review_v")
        self.checkBox_review_v.setFont(font1)
        self.checkBox_review_v.setChecked(True)

        self.listViewNum_layout.addWidget(self.checkBox_review_v)

        self.checkBox_approved_v = QCheckBox(daySchedule_frame)
        self.checkBox_approved_v.setObjectName(u"checkBox_approved_v")
        self.checkBox_approved_v.setFont(font1)
        self.checkBox_approved_v.setChecked(True)

        self.listViewNum_layout.addWidget(self.checkBox_approved_v)

        self.checkBox_retake_v = QCheckBox(daySchedule_frame)
        self.checkBox_retake_v.setObjectName(u"checkBox_retake_v")
        self.checkBox_retake_v.setFont(font1)
        self.checkBox_retake_v.setChecked(True)
        self.checkBox_retake_v.setTristate(False)

        self.listViewNum_layout.addWidget(self.checkBox_retake_v)

        self.checkBox_hold_v = QCheckBox(daySchedule_frame)
        self.checkBox_hold_v.setObjectName(u"checkBox_hold_v")
        self.checkBox_hold_v.setFont(font1)
        self.checkBox_hold_v.setChecked(True)

        self.listViewNum_layout.addWidget(self.checkBox_hold_v)

        self.checkBox_wait_v = QCheckBox(daySchedule_frame)
        self.checkBox_wait_v.setObjectName(u"checkBox_wait_v")
        self.checkBox_wait_v.setFont(font1)
        self.checkBox_wait_v.setChecked(True)

        self.listViewNum_layout.addWidget(self.checkBox_wait_v)

        self.checkBox_omit_v = QCheckBox(daySchedule_frame)
        self.checkBox_omit_v.setObjectName(u"checkBox_omit_v")
        self.checkBox_omit_v.setFont(font1)

        self.listViewNum_layout.addWidget(self.checkBox_omit_v)

        self.listViewNumSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.listViewNum_layout.addItem(self.listViewNumSpacer)

        self.Button_today = QPushButton(daySchedule_frame)
        self.Button_today.setObjectName(u"Button_today")
        self.Button_today.setMinimumSize(QSize(100, 0))

        self.listViewNum_layout.addWidget(self.Button_today)


        self.daySchedule_rootLayout.addLayout(self.listViewNum_layout)

        self.scrollArea = QScrollArea(daySchedule_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setSizeIncrement(QSize(0, 0))
        self.scrollArea.setBaseSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaLayout = QWidget()
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.scrollAreaLayout.setGeometry(QRect(0, 0, 1096, 586))
        self.scrollAreaLayout.setBaseSize(QSize(1390, 555))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaLayout)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.splitter = QSplitter(self.scrollAreaLayout)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.splitter)

        self.scrollArea.setWidget(self.scrollAreaLayout)

        self.daySchedule_rootLayout.addWidget(self.scrollArea)


        self.horizontalLayout.addLayout(self.daySchedule_rootLayout)


        self.retranslateUi(daySchedule_frame)

        QMetaObject.connectSlotsByName(daySchedule_frame)
    # setupUi

    def retranslateUi(self, daySchedule_frame):
        daySchedule_frame.setWindowTitle(QCoreApplication.translate("daySchedule_frame", u"Frame", None))
        self.backwardDayButton.setText(QCoreApplication.translate("daySchedule_frame", u"<", None))
        self.start_month.setText(QCoreApplication.translate("daySchedule_frame", u"1", None))
        self.startDate_dot.setText(QCoreApplication.translate("daySchedule_frame", u".  ", None))
        self.start_day.setText(QCoreApplication.translate("daySchedule_frame", u"1", None))
        self.startDate_wave.setText(QCoreApplication.translate("daySchedule_frame", u"   ~   ", None))
        self.forwardDayButton.setText(QCoreApplication.translate("daySchedule_frame", u">", None))
        self.checkBox_ready_v.setText(QCoreApplication.translate("daySchedule_frame", u"Ready", None))
        self.checkBox_inprogress_v.setText(QCoreApplication.translate("daySchedule_frame", u"In-progress", None))
        self.checkBox_ok_v.setText(QCoreApplication.translate("daySchedule_frame", u"Ok", None))
        self.checkBox_review_v.setText(QCoreApplication.translate("daySchedule_frame", u"Review", None))
        self.checkBox_approved_v.setText(QCoreApplication.translate("daySchedule_frame", u"Approved", None))
        self.checkBox_retake_v.setText(QCoreApplication.translate("daySchedule_frame", u"Retake", None))
        self.checkBox_hold_v.setText(QCoreApplication.translate("daySchedule_frame", u"Hold", None))
        self.checkBox_wait_v.setText(QCoreApplication.translate("daySchedule_frame", u"Waiting", None))
        self.checkBox_omit_v.setText(QCoreApplication.translate("daySchedule_frame", u"Omit", None))
        self.Button_today.setText(QCoreApplication.translate("daySchedule_frame", u"Today", None))
    # retranslateUi

