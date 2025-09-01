# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingProgressSaKniw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_loadingProg(object):
    def setupUi(self, Dialog_loadingProg):
        if not Dialog_loadingProg.objectName():
            Dialog_loadingProg.setObjectName(u"Dialog_loadingProg")
        Dialog_loadingProg.resize(470, 134)
        self.horizontalLayout_2 = QHBoxLayout(Dialog_loadingProg)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.h_Layout_loadingProg = QHBoxLayout()
        self.h_Layout_loadingProg.setSpacing(23)
        self.h_Layout_loadingProg.setObjectName(u"h_Layout_loadingProg")
        self.h_Layout_loadingProg.setContentsMargins(30, -1, 30, -1)
        self.label_data = QLabel(Dialog_loadingProg)
        self.label_data.setObjectName(u"label_data")

        self.h_Layout_loadingProg.addWidget(self.label_data)

        self.progressBar_loading = QProgressBar(Dialog_loadingProg)
        self.progressBar_loading.setObjectName(u"progressBar_loading")
        self.progressBar_loading.setValue(24)

        self.h_Layout_loadingProg.addWidget(self.progressBar_loading)


        self.horizontalLayout_2.addLayout(self.h_Layout_loadingProg)


        self.retranslateUi(Dialog_loadingProg)

        QMetaObject.connectSlotsByName(Dialog_loadingProg)
    # setupUi

    def retranslateUi(self, Dialog_loadingProg):
        Dialog_loadingProg.setWindowTitle(QCoreApplication.translate("Dialog_loadingProg", u"Dialog", None))
        self.label_data.setText(QCoreApplication.translate("Dialog_loadingProg", u"Progress : ", None))
    # retranslateUi

