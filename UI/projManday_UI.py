# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_status_projMandayzbNNWa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_mandayStatus(object):
    def setupUi(self, Form_mandayStatus):
        if not Form_mandayStatus.objectName():
            Form_mandayStatus.setObjectName(u"Form_mandayStatus")
        Form_mandayStatus.resize(956, 118)
        self.verticalLayout_2 = QVBoxLayout(Form_mandayStatus)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_mandayStatus = QFrame(Form_mandayStatus)
        self.frame_mandayStatus.setObjectName(u"frame_mandayStatus")
        self.frame_mandayStatus.setMaximumSize(QSize(16777215, 110))
        self.frame_mandayStatus.setFrameShape(QFrame.StyledPanel)
        self.frame_mandayStatus.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_mandayStatus)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.h_Layout_project = QHBoxLayout()
        self.h_Layout_project.setObjectName(u"h_Layout_project")
        self.label_project = QLabel(self.frame_mandayStatus)
        self.label_project.setObjectName(u"label_project")
        self.label_project.setMinimumSize(QSize(300, 0))

        self.h_Layout_project.addWidget(self.label_project)


        self.horizontalLayout_2.addLayout(self.h_Layout_project)

        self.v_Layout_project = QVBoxLayout()
        self.v_Layout_project.setObjectName(u"v_Layout_project")
        self.h_Layout_shots = QHBoxLayout()
        self.h_Layout_shots.setSpacing(20)
        self.h_Layout_shots.setObjectName(u"h_Layout_shots")
        self.label_shots = QLabel(self.frame_mandayStatus)
        self.label_shots.setObjectName(u"label_shots")
        self.label_shots.setMinimumSize(QSize(70, 0))
        self.label_shots.setMaximumSize(QSize(100, 16777215))

        self.h_Layout_shots.addWidget(self.label_shots)

        self.label_progressBar_shots = QProgressBar(self.frame_mandayStatus)
        self.label_progressBar_shots.setObjectName(u"label_progressBar_shots")
        self.label_progressBar_shots.setValue(24)

        self.h_Layout_shots.addWidget(self.label_progressBar_shots)

        self.label_amount_shots = QLabel(self.frame_mandayStatus)
        self.label_amount_shots.setObjectName(u"label_amount_shots")
        self.label_amount_shots.setMinimumSize(QSize(110, 0))
        self.label_amount_shots.setMaximumSize(QSize(70, 16777215))

        self.h_Layout_shots.addWidget(self.label_amount_shots)


        self.v_Layout_project.addLayout(self.h_Layout_shots)

        self.h_Layout_manday = QHBoxLayout()
        self.h_Layout_manday.setSpacing(20)
        self.h_Layout_manday.setObjectName(u"h_Layout_manday")
        self.label_manday = QLabel(self.frame_mandayStatus)
        self.label_manday.setObjectName(u"label_manday")
        self.label_manday.setMinimumSize(QSize(70, 0))
        self.label_manday.setMaximumSize(QSize(100, 16777215))

        self.h_Layout_manday.addWidget(self.label_manday)

        self.label_progressBar_md = QProgressBar(self.frame_mandayStatus)
        self.label_progressBar_md.setObjectName(u"label_progressBar_md")
        self.label_progressBar_md.setValue(24)

        self.h_Layout_manday.addWidget(self.label_progressBar_md)

        self.label_amount_md = QLabel(self.frame_mandayStatus)
        self.label_amount_md.setObjectName(u"label_amount_md")
        self.label_amount_md.setMinimumSize(QSize(110, 0))
        self.label_amount_md.setMaximumSize(QSize(70, 16777215))

        self.h_Layout_manday.addWidget(self.label_amount_md)


        self.v_Layout_project.addLayout(self.h_Layout_manday)


        self.horizontalLayout_2.addLayout(self.v_Layout_project)


        self.verticalLayout_2.addWidget(self.frame_mandayStatus)


        self.retranslateUi(Form_mandayStatus)

        QMetaObject.connectSlotsByName(Form_mandayStatus)
    # setupUi

    def retranslateUi(self, Form_mandayStatus):
        Form_mandayStatus.setWindowTitle(QCoreApplication.translate("Form_mandayStatus", u"Form", None))
        self.label_project.setText(QCoreApplication.translate("Form_mandayStatus", u"project", None))
        self.label_shots.setText(QCoreApplication.translate("Form_mandayStatus", u"tasks", None))
        self.label_amount_shots.setText(QCoreApplication.translate("Form_mandayStatus", u"n / all", None))
        self.label_manday.setText(QCoreApplication.translate("Form_mandayStatus", u"manday", None))
        self.label_amount_md.setText(QCoreApplication.translate("Form_mandayStatus", u"n / all", None))
    # retranslateUi

