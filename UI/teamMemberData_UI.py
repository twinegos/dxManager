# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teamMemberDataXeMpbl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_memberData_frm(object):
    def __init__(self):

        self.memberData_frm = QFrame()
        self.memberData_frm.resize(934, 205)
        self.memberData_frm.setMinimumSize(QSize(934, 205))
        self.memberData_frm.setMaximumSize(QSize(934, 205))        
        self.memberData_frm.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.memberData_frm.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.memberData_frm.setFrameShape(QFrame.StyledPanel)
        self.memberData_frm.setFrameShadow(QFrame.Sunken)

        self.verticalLayout = QVBoxLayout(self.memberData_frm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.memberData_layout = QHBoxLayout()
        self.memberData_layout.setObjectName(u"memberData_layout")
        self.nameBox_frm = QFrame(self.memberData_frm)
        self.nameBox_frm.setObjectName(u"nameBox_frm")
        self.nameBox_frm.setFrameShape(QFrame.NoFrame)
        self.nameBox_frm.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.nameBox_frm)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.time_layout = QHBoxLayout()
        self.time_layout.setObjectName(u"time_layout")
        self.timeBox_spc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.time_layout.addItem(self.timeBox_spc)

        self.year_combo = QComboBox(self.nameBox_frm)
        self.year_combo.setObjectName(u"year_combo")
        self.year_combo.setMaximumSize(QSize(90, 30))

        self.time_layout.addWidget(self.year_combo)

        self.quarter_combo = QComboBox(self.nameBox_frm)
        self.quarter_combo.setObjectName(u"quarter_combo")
        self.quarter_combo.setMaximumSize(QSize(60, 30))

        self.time_layout.addWidget(self.quarter_combo)


        self.verticalLayout_4.addLayout(self.time_layout)

        self.nameBox_spc = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.nameBox_spc)

        self.artistName_layout = QHBoxLayout()
        self.artistName_layout.setObjectName(u"artistName_layout")
        self.artistName_layout.setContentsMargins(32, -1, -1, -1)
        self.artist_label = QLabel(self.nameBox_frm)
        self.artist_label.setObjectName(u"artist_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artist_label.sizePolicy().hasHeightForWidth())
        self.artist_label.setSizePolicy(sizePolicy)
        self.artist_label.setMinimumSize(QSize(60, 30))
        self.artist_label.setMaximumSize(QSize(60, 30))
        font = QFont()
        font.setPointSize(15)
        self.artist_label.setFont(font)

        self.artistName_layout.addWidget(self.artist_label, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.name_label = QLabel(self.nameBox_frm)
        self.name_label.setObjectName(u"name_label")
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setMinimumSize(QSize(150, 30))
        self.name_label.setMaximumSize(QSize(80, 30))
        self.name_label.setFont(font)

        self.artistName_layout.addWidget(self.name_label, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.artistName_spc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.artistName_layout.addItem(self.artistName_spc)


        self.verticalLayout_4.addLayout(self.artistName_layout)

        self.level_layout = QHBoxLayout()
        self.level_layout.setObjectName(u"level_layout")
        self.level_layout.setContentsMargins(30, -1, -1, -1)
        self.lebel_label = QLabel(self.nameBox_frm)
        self.lebel_label.setObjectName(u"lebel_label")

        self.level_layout.addWidget(self.lebel_label, 0, Qt.AlignLeft|Qt.AlignTop)

        self.levelName_label = QLabel(self.nameBox_frm)
        self.levelName_label.setObjectName(u"levelName_label")

        self.level_layout.addWidget(self.levelName_label, 0, Qt.AlignRight|Qt.AlignTop)

        self.level_spc = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.level_layout.addItem(self.level_spc)


        self.verticalLayout_4.addLayout(self.level_layout)

        self.nameBox_spc2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(self.nameBox_spc2)


        self.workData_btn = QPushButton(self.nameBox_frm)
        self.workData_btn.setObjectName(u"workData_btn")

        self.verticalLayout_4.addWidget(self.workData_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.memberData_layout.addWidget(self.nameBox_frm)

        self.tasksBox_frm = QFrame(self.memberData_frm)
        self.tasksBox_frm.setObjectName(u"tasksBox_frm")
        self.tasksBox_frm.setMinimumSize(QSize(0, 181))
        self.tasksBox_frm.setMaximumSize(QSize(190, 16777215))
        self.tasksBox_frm.setFrameShape(QFrame.StyledPanel)
        self.tasksBox_frm.setFrameShadow(QFrame.Sunken)
        self.tasksBox_frm.setLineWidth(5)
        self.tasksBox_frm.setMidLineWidth(5)
        self.verticalLayout_5 = QVBoxLayout(self.tasksBox_frm)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tasks_layout = QHBoxLayout()
        self.tasks_layout.setObjectName(u"tasks_layout")
        self.tasks_label = QLabel(self.tasksBox_frm)
        self.tasks_label.setObjectName(u"tasks_label")
        self.tasks_label.setMaximumSize(QSize(80, 16777215))
        self.tasks_label.setFrameShape(QFrame.NoFrame)
        self.tasks_label.setFrameShadow(QFrame.Plain)
        self.tasks_label.setLineWidth(1)
        self.tasks_label.setMidLineWidth(0)

        self.tasks_layout.addWidget(self.tasks_label)

        self.tasks_lineEdit = QLineEdit(self.tasksBox_frm)
        self.tasks_lineEdit.setObjectName(u"tasks_lineEdit")
        self.tasks_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.tasks_layout.addWidget(self.tasks_lineEdit)


        self.verticalLayout_5.addLayout(self.tasks_layout)

        self.tasksBox_spc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.tasksBox_spc)


        self.memberData_layout.addWidget(self.tasksBox_frm)

        self.mandayBox_frm = QFrame(self.memberData_frm)
        self.mandayBox_frm.setObjectName(u"mandayBox_frm")
        self.mandayBox_frm.setFrameShape(QFrame.StyledPanel)
        self.mandayBox_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mandayBox_frm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.manday_layout = QHBoxLayout()
        self.manday_layout.setObjectName(u"manday_layout")
        self.manday_label = QLabel(self.mandayBox_frm)
        self.manday_label.setObjectName(u"manday_label")
        self.manday_label.setMaximumSize(QSize(80, 50))

        self.manday_layout.addWidget(self.manday_label, 0, Qt.AlignLeft)

        self.manday_lineEdit = QLineEdit(self.mandayBox_frm)
        self.manday_lineEdit.setObjectName(u"manday_lineEdit")
        self.manday_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.manday_layout.addWidget(self.manday_lineEdit)


        self.verticalLayout_2.addLayout(self.manday_layout)

        self.actManday_layout = QHBoxLayout()
        self.actManday_layout.setObjectName(u"actManday_layout")
        self.actManday_label = QLabel(self.mandayBox_frm)
        self.actManday_label.setObjectName(u"actManday_label")
        self.actManday_label.setMaximumSize(QSize(80, 50))

        self.actManday_layout.addWidget(self.actManday_label, 0, Qt.AlignLeft)

        self.actManday_lineEdit = QLineEdit(self.mandayBox_frm)
        self.actManday_lineEdit.setObjectName(u"actManday_lineEdit")
        self.actManday_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.actManday_layout.addWidget(self.actManday_lineEdit)


        self.verticalLayout_2.addLayout(self.actManday_layout)

        self.manday_prog = QProgressBar(self.mandayBox_frm)
        self.manday_prog.setObjectName(u"manday_prog")
        self.manday_prog.setValue(24)

        self.verticalLayout_2.addWidget(self.manday_prog)

        self.mandayBox_spc = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.mandayBox_spc)

        self.achieve_layout = QHBoxLayout()
        self.achieve_layout.setObjectName(u"achieve_layout")
        self.achieve_label = QLabel(self.mandayBox_frm)
        self.achieve_label.setObjectName(u"achieve_label")
        self.achieve_label.setMaximumSize(QSize(16777215, 50))

        self.achieve_layout.addWidget(self.achieve_label)

        self.achieve_ratio = QLabel(self.mandayBox_frm)
        self.achieve_ratio.setObjectName(u"achieve_ratio")
        self.achieve_ratio.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(19)
        self.achieve_ratio.setFont(font1)

        self.achieve_layout.addWidget(self.achieve_ratio, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.achieve_layout)


        self.memberData_layout.addWidget(self.mandayBox_frm)

        self.difficulty_frm = QFrame(self.memberData_frm)
        self.difficulty_frm.setObjectName(u"difficulty_frm")
        self.difficulty_frm.setFrameShape(QFrame.StyledPanel)
        self.difficulty_frm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.difficulty_frm)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.difficulty_layout = QHBoxLayout()
        self.difficulty_layout.setObjectName(u"difficulty_layout")
        self.difficulty_label = QLabel(self.difficulty_frm)
        self.difficulty_label.setObjectName(u"difficulty_label")
        self.difficulty_label.setMaximumSize(QSize(80, 50))

        self.difficulty_layout.addWidget(self.difficulty_label, 0, Qt.AlignLeft)

        self.difficulty_lineEdit = QLineEdit(self.difficulty_frm)
        self.difficulty_lineEdit.setObjectName(u"difficulty_lineEdit")
        self.difficulty_lineEdit.setMaximumSize(QSize(90, 16777215))

        self.difficulty_layout.addWidget(self.difficulty_lineEdit, 0, Qt.AlignLeft)


        self.verticalLayout_3.addLayout(self.difficulty_layout)

        self.difficultyBox_spc = QSpacerItem(20, 49, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.difficultyBox_spc)

        self.evaluation_layout = QHBoxLayout()
        self.evaluation_layout.setObjectName(u"evaluation_layout")
        self.evaluation_label = QLabel(self.difficulty_frm)
        self.evaluation_label.setObjectName(u"evaluation_label")
        self.evaluation_label.setMaximumSize(QSize(80, 50))

        self.evaluation_layout.addWidget(self.evaluation_label, 0, Qt.AlignLeft)

        self.evaluation_value = QLabel(self.difficulty_frm)
        self.evaluation_value.setObjectName(u"evaluation_value")
        self.evaluation_value.setMaximumSize(QSize(16777215, 50))
        self.evaluation_value.setFont(font1)

        self.evaluation_layout.addWidget(self.evaluation_value, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.evaluation_layout)


        self.memberData_layout.addWidget(self.difficulty_frm)


        self.verticalLayout.addLayout(self.memberData_layout)

        self.artist_label.setText("Artist :")
        self.name_label.setText("name")
        self.lebel_label.setText("Level :")
        self.levelName_label.setText("artist")
        self.workData_btn.setText("WorkData info.")
        self.tasks_label.setText("Tasks")
        self.manday_label.setText("Manday")
        self.actManday_label.setText("Act Manday")
        self.achieve_label.setText("Achievement R :")
        self.achieve_ratio.setText("0 %")
        self.difficulty_label.setText("Difficulty Lv.")
        self.evaluation_label.setText("Evaluation :")
        self.evaluation_value.setText("0     ")





