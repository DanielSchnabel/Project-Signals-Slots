import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TaxRate(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.rate = 17.5
        self.rateLabel = QLabel(self.rate)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(.01, 10000000.00)
        self.fromSpinBox.setValue(self.rate)

        grid = QGridLayout()
        grid.addWidget(self.rateLabel, 0, 0)
        grid.addWidget(self.fromSpinBox, 1, 0)
        self.setLayout(grid)
        self.setWindowTitle("Tax Rate")
        self.fromSpinBox.valueChanged.connect(self.setRate)

    def rate(self):
        return self.rate

    def setRate(self,rate):
        if rate != self.rate:
            self.rate = rate
            self.emit.rateChanged.connect(self.rate)

def rateChanged(value):
    print("TaxRate changed to %.2f%%" % value)

vat = TaxRate()
vat.rateChanged.connect(rateChanged)
vat.setRate(17.5)
vat.setRate(8.5)
