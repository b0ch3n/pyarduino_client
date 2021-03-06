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
from client.qtdesigner import Ui_MplMainWindow

class DesignerMainWindow(QtGui.QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
    
        QtCore.QObject.connect(self.mplpushButton, QtCore.SIGNAL("clicked()"), self.update_graph)
        QtCore.QObject.connect(self.mplactionOpen, QtCore.SIGNAL('triggered()'), self.select_file)
        QtCore.QObject.connect(self.mplactionQuit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT("quit()"))

    def select_file(self):
        """opens a file select dialog"""
        # open the dialog and get the selected file
        file = QtGui.QFileDialog.getOpenFileName()
        # if a file is selected
        if file:
            # update the lineEdit widget text with the selected filename
            self.mpllineEdit.setText(file)


    def parse_file(self, filename):
        """Function to parse a text file to extract letters frequencies"""

        # dict initialization
        letters = {}

        # lower-case letter ordinal numbers
        for i in range(97, 122 + 1):
            letters[chr(i)] = 0

        # parse the input file
        with open(filename) as f:
            for line in f:
                for char in line:
                    # counts only letters
                    if ord(char.lower()) in range(97, 122 + 1):
                        letters[char.lower()] += 1

        # compute the ordered list of keys and relative values
        k = sorted(letters.keys())
        v = [letters[ki] for ki in k]

        return k, v


    def update_graph(self):
        """Updates the graph with new letters frequencies"""

        # get the letters frequencies
        l, v = self.parse_file(self.mpllineEdit.text())

        # clear the Axes
        self.mpl.canvas.ax.clear()

        # draw a bar chart for letters and their frequencies
        # set the width to 0.5 and shift bars of 0.25, to be centered
        self.mpl.canvas.ax.bar(np.arange(len(l))-0.25, v, width=0.5)

        # reset the X limits
        self.mpl.canvas.ax.set_xlim(xmin=-0.25, xmax=len(l)-0.75)
        # set the X ticks & tickslabel as the letters
        self.mpl.canvas.ax.set_xticks(range(len(l)))
        self.mpl.canvas.ax.set_xticklabels(l)
        # enable grid only on the Y axis
        self.mpl.canvas.ax.get_yaxis().grid(True)
        # force an image redraw
        self.mpl.canvas.draw()

# create the GUI application
app = QtGui.QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())