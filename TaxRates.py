import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TaxRate(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.rate = 17.5

class Form(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.taxrate = TaxRate()

        self.rateLabel = QLabel("Tax rate is "+ str(self.taxrate.rate) + " "*18)
        self.spinBox = QDoubleSpinBox()
        self.spinBox.setRange(.01, 1000000.00)
        self.spinBox.setValue(self.taxrate.rate)

        grid = QGridLayout()
        grid.addWidget(self.rateLabel, 0, 0)
        grid.addWidget(self.spinBox, 1, 0)
        self.setLayout(grid)
        self.setWindowTitle("Tax Rate")
        self.spinBox.valueChanged.connect(self.updateUi)

    def updateUi(self):
        self.rateLabel.setText("Tax rate changed to " + str(self.spinBox.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
