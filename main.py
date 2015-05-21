__author__ = 'Mateusz'
'''
from socket import *
s = socket(AF_INET, SOCK_STREAM) #utworzenie gniazda
s.connect(('localhost', 8888)) # nawiazanie polaczenia
tm = s.recv(1024) #odbior danych (max 1024 bajtów)
s.close()
print(tm)
'''


from __future__ import  with_statement
import numpy as np
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from client.qtdesigner import Ui_MplMainWindow

class DesignerMainWindow(QtGui.QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)

        QtCore.QObject.connect(self.mplpushButton,)



