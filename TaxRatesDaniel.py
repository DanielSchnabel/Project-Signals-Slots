import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TaxRate(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.rate = 17.5


    def rate(self):
        return self.rate

    def setRate(self,rate):
        if rate != self.rate:
            self.rate = rate
            self.rateChanged.emit(rate)

def rateChanged(value):
    return "Tax rate changed to %.2f%%" % value

class Form(QDialog):
    def __inti__(self, parent = None):
        super().__init__(parent)

        self.rateLabel = QLabel("Tax rate is "+ str(TaxRate.rate))
        self.spinBox = QDoubleSpinBox()
        self.spinBox.setRange(.01, 10000000.00)
        self.spinBox.setValue(TaxRate.rate)

        grid = QGridLayout()
        grid.addWidget(self.rateLabel, 0, 0)
        grid.addWidget(self.spinBox, 1, 0)
        self.setLayout(grid)
        self.setWindowTitle("Tax Rate")
        self.spinBox.valueChanged.connect(TaxRate.setRate)
        self.rateLabel.valueChanged.connect(TaxRate.rateChanged)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

    #vat.rateChanged.connect(rateChanged)
