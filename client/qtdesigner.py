# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created: Thu May 21 20:31:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName(_fromUtf8("MplMainWindow"))
        MplMainWindow.resize(402, 260)
        self.mplcentralwidget = QtGui.QWidget(MplMainWindow)
        self.mplcentralwidget.setObjectName(_fromUtf8("mplcentralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mplcentralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplhorizontalLayout = QtGui.QHBoxLayout()
        self.mplhorizontalLayout.setObjectName(_fromUtf8("mplhorizontalLayout"))
        self.mplpushButton = QtGui.QPushButton(self.mplcentralwidget)
        self.mplpushButton.setObjectName(_fromUtf8("mplpushButton"))
        self.mplhorizontalLayout.addWidget(self.mplpushButton)
        self.mpllineEdit = QtGui.QLineEdit(self.mplcentralwidget)
        self.mpllineEdit.setObjectName(_fromUtf8("mpllineEdit"))
        self.mplhorizontalLayout.addWidget(self.mpllineEdit)
        self.verticalLayout.addLayout(self.mplhorizontalLayout)
        self.mpl = MplWidget(self.mplcentralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.verticalLayout.addWidget(self.mpl)
        MplMainWindow.setCentralWidget(self.mplcentralwidget)
        self.menubar = QtGui.QMenuBar(MplMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        MplMainWindow.setMenuBar(self.menubar)
        self.mplactionOpen = QtGui.QAction(MplMainWindow)
        self.mplactionOpen.setObjectName(_fromUtf8("mplactionOpen"))
        self.mplactionQuit = QtGui.QAction(MplMainWindow)
        self.mplactionQuit.setObjectName(_fromUtf8("mplactionQuit"))
        self.menu_File.addAction(self.mplactionOpen)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.mplactionQuit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow", None))
        self.mplpushButton.setText(_translate("MplMainWindow", "PushButton", None))
        self.menu_File.setTitle(_translate("MplMainWindow", "&File", None))
        self.mplactionOpen.setText(_translate("MplMainWindow", "Open", None))
        self.mplactionQuit.setText(_translate("MplMainWindow", "Quit", None))

from mplwidget import MplWidget
