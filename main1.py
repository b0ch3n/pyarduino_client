from __future__ import  with_statement
__author__ = 'Mateusz'
'''
from socket import *
s = socket(AF_INET, SOCK_STREAM) #utworzenie gniazda
s.connect(('localhost', 8888)) # nawiazanie polaczenia
tm = s.recv(1024) #odbior danych (max 1024 bajtów)
s.close()
print(tm)
'''



import numpy as np
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from client.gui_main import Ui_MainWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

# create the GUI application
app = QtGui.QApplication(sys.argv)
# instantiate the main window
dmw = MainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())