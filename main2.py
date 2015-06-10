from __future__ import  with_statement
__author__ = 'Mateusz'


import numpy as np
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import queue
from socket import *
import os, sys, time
from client.gui_main import Ui_MainWindow
from socket_thread.socket_thread import SocketClientThread
from socket_thread.socket_thread import ClientCommand
from socket_thread.socket_thread import ClientReply

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self._connected = 0
        self._connectionParameters = {}
        self.connectionStatusTextBox.setReadOnly(True)
        self.setValidatorsForInputs()
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL("clicked()"), self.connect_to_server)
        QtCore.QObject.connect(self.startMonitButton, QtCore.SIGNAL("clicked()"), self.start_monitoring)

        self.sct = SocketClientThread()
        self.sct.start()



    def connect_to_server(self):
        """try to get data from inputs and connect to arduino server"""
        self.connectionStatusTextBox.clear()
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
        try:
            self.connectionStatusTextBox.append("Próba utworzenia gniazda...\n")
            s = socket(AF_INET, SOCK_STREAM)
            self.connectionStatusTextBox.append("Gniazdo utworzone pomyślnie.\n")
            self.connectionStatusTextBox.append("Próba połączenia z serwerem...\n")
            s.connect((self._connectionParameters['address'], int(self._connectionParameters['port'])))
            self.connectionStatusTextBox.append("Połączenie nawiązane pomyślnie.\n")
            self.connectionStatusTextBox.append("Zamykanie połączenia...\n")
            s.close()
            self.connectionStatusTextBox.append("Połączenie zamknięte pomyślnie.\n")
        except:
            self.connectionStatusTextBox.append("Nie udało się połączyć z serwerem!\n")

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

    def start_monitoring(self):

        try:
            if self._connected == 0:
                self.sct.cmd_q.put(ClientCommand(ClientCommand.CONNECT, ('localhost', 8888)))
                reply = self.sct.reply_q.get(True)
                self._connected= 1

            self.sct.cmd_q.put(ClientCommand(ClientCommand.SEND, "hellothere"))
            reply = self.sct.reply_q.get(True)
            self.sct.cmd_q.put(ClientCommand(ClientCommand.RECEIVE, "hellothere"))
            reply = self.sct.reply_q.get(True)
            print(reply.type, reply.data)

        except queue.Empty:
            pass

    def monit(self):
        while (True):
            try:
                reply = self.sct.reply_q.get(block=False)
                status = "SUCCESS" if reply.type == ClientReply.SUCCESS else "ERROR"
                print('Client reply %s: %s' % (status, reply.data))
                self.sct.cmd_q.put(ClientCommand(ClientCommand.RECEIVE, "hellothere"))
            except queue.Empty:
                pass



app = QtGui.QApplication(sys.argv)
# instantiate the main window
dmw = MainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())