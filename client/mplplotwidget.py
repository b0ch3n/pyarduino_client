__author__ = 'Mateusz'


from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(True)
        self.axes.set_autoscale_on(False)
        self.axes.axis([0, 3, 0, 5])
        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class DynamicChartCanvas(MplCanvas):
    def __init__(self, *args, **kwargs):
        MplCanvas.__init__(self, *args, **kwargs)
        self.vltg = None
    def compute_initial_figure(self):
        self.axes.plot([0, 1], [0, 0], 'r')

    def update_figure(self, voltage_value):
        if self.vltg is not None:
            self.vltg.pop(0).remove()

        self.fig.clf()
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(True)
        self.axes.set_autoscale_on(False)
        self.axes.axis([0, 3, 0, 5])
        self.compute_initial_figure()

        voltage_value = float(voltage_value)
        self.axes.fill_between([0, 3], [voltage_value, voltage_value])
        self.vltg = self.axes.plot([0, 3], [voltage_value, voltage_value], 'r')
        self.draw()


class MplPlotWidget(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = DynamicChartCanvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)