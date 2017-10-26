import sys
from urllib.request import urlopen
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TaxRate(QObject):
    rateChanged = pyqtSignal(float)

    def __init__(self, parent = None):
        super().__init__(parent)
        self._rate = 17.5

    def rate(self):
        return self.rate

    def setRate(self, rate):
        if rate != self.rate:
            self.rate = rate
            self.rateChanged.emit(rate)

def RateChanged(value):
    print("TaxRate changed to %.2f%%" % value)

class Form(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.rate = TaxRate()


        self.rateLabel = QLabel("Tax rate is "+ str(self.rate._rate))
        self.spinBox = QDoubleSpinBox()
        self.spinBox.setRange(.01, 10000000.00)
        self.spinBox.setValue(self.rate._rate)

        grid = QGridLayout()
        grid.addWidget(self.rateLabel, 0, 0)
        grid.addWidget(self.spinBox, 1, 0)
        self.setLayout(grid)
        self.setWindowTitle("Tax Rate")
        self.spinBox.valueChanged.connect(self.updateUi)

    def updateUi(self):
        self.rateLabel.setText("Tax rate changed to" + str(self.spinBox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
