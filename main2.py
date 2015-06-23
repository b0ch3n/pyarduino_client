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

import threading

class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def setup(self, thread_no, connected, sct, params):
        self.thread_no = thread_no
        self._connected = connected
        self.sct = sct
        self._params = params

    def run(self):
        while True:
            try:
                if self._connected == 0:
                    self.sct.cmd_q.put(ClientCommand(ClientCommand.CONNECT, (self._params['address'],
                                                                             int(self._params['port']))))
                    reply = self.sct.reply_q.get(True)
                    self._connected= 1

                self.sct.cmd_q.put(ClientCommand(ClientCommand.SEND, "aaaaa"))
                reply = self.sct.reply_q.get(True)
                print(reply.data)
                self.sct.cmd_q.put(ClientCommand(ClientCommand.RECEIVE, "Client_Getter"))
                reply = self.sct.reply_q.get(True)
                self.trigger.emit(reply.data)

            except queue.Empty:
                pass



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



    def setValidatorsForInputs(self):
        validator = QtGui.QIntValidator()
        self.serverPortTextLine.setValidator(validator)

    def start_monitoring(self):
        self.monit()

    def update_text(self, reply):
        self.connectionStatusTextBox.append(reply)

    def update_chart(self, reply):
        self.mplplotwidget.canvas.update_figure(reply)

    def monit(self):
        thread = MyThread(self)
        thread.trigger.connect(self.update_chart)
        thread.setup(1, 0, self.sct, self._connectionParameters)
        thread.start()



app = QtGui.QApplication(sys.argv)
dmw = MainWindow()
dmw.show()
sys.exit(app.exec_())