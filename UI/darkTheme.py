import os
from PySide2 import QtWidgets, QtGui, QtCore

def set_palette():
    darkPalette = QtGui.QPalette()
    # active color set

    darkPalette.setColor(QtGui.QPalette.Window, QtGui.QColor(60, 60, 60))
    darkPalette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Base, QtGui.QColor(70, 70, 70))
    darkPalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Text, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    darkPalette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(180, 20, 20))
    darkPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(35, 100, 180))
    darkPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(35, 100, 180))
    darkPalette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(180, 180, 180))
    darkPalette.setColor(QtGui.QPalette.Mid, QtGui.QColor(100, 100, 100))


    # disabled color set
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, QtGui.QColor(100, 100, 100))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, QtGui.QColor(100, 100, 100))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, QtGui.QColor(100, 100, 100))
    darkPalette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtGui.QColor(100, 100, 100))

    return darkPalette

def set_styleSheet():
    #rootPath = os.environ['REZ_JAMONG_ROOT_BASE']
    darkStyleSheet = '''

        /* QTreeView */
        QTreeView::indicator:unchecked {
            border: 1px solid #222222;
        }
        QTreeView::indicator:checked {
            border: 1px solid #222222;
            background-color: #a4a4a4;
        }

        QListView {
            background-color: #2d2d2d;
        }

        QComboBox {
            font-size: 30px;
            font-weight: bold;
        }


    ''' 
    #background-color: #b4b4b4;
    return darkStyleSheet