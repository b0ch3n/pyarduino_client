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
from socket import *
from client.gui_main import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self._connectionParameters = {}
        self.connectionStatusTextBox.setReadOnly(True)
        self.setValidatorsForInputs()
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL("clicked()"), self.connect_to_server)

    def connect_to_server(self):
        """try to get data from inputs and connect to arduino server"""
        try:
            self._connectionParameters['address'] = self.serverAddressTextLine.text()
            self._connectionParameters['port'] = int(self.serverPortTextLine.text().strip().replace(" ", ""))
            self._connectionParameters['socket_type'] = self.serverSocketTypeCBox.currentText()
        except:
            self.connectionStatusTextBox.append("Wprowadz prawidlowe dane do połączenia! \n")

        self.sockettype = "Undefined"
        if self._connectionParameters['socket_type'] == 'AF_INET':
            self.sockettype= AF_INET
        elif self._connectionParameters['socket_type'] == 'AF_UNIX':
            self.sockettype= None
        else:
           self.sockettype= AF_INET6
        self.connectionStatusTextBox.append("Próba utworzenia gniazda...\n")
        s = socket(AF_INET, SOCK_STREAM) #utworzenie gniazda
        self.connectionStatusTextBox.append("Gniazdo utworzone pomyślnie.\n")
        self.connectionStatusTextBox.append("Prób połączenia z serwerem...\n")
        s.connect((self._connectionParameters['address'], 8888)) # nawiazanie polaczenia
        self.connectionStatusTextBox.append("Połączenie nawiązane pomyślnie.\n")

        self.connectionStatusTextBox.append("MONITORING ROZPOCZĘTY...\n")
        '''
        self.i = 0;
        while self.i<8:
            s = socket(AF_INET, SOCK_STREAM) #utworzenie gniazda
            s.connect((self._connectionParameters['address'], 8888)) # nawiazanie polaczenia
            tm = s.recv(1024) #odbior danych (max 1024 bajtów)
            print(tm)
            self.i += 1
            s.close()
        '''

    def setValidatorsForInputs(self):
        validator = QtGui.QIntValidator()
        self.serverPortTextLine.setValidator(validator)

# create the GUI application
app = QtGui.QApplication(sys.argv)
# instantiate the main window
dmw = MainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())