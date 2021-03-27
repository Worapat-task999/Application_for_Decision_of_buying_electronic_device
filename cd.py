# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_creditWindow(object):
    def setupUi(self, creditWindow):
        creditWindow.setObjectName("creditWindow")
        creditWindow.resize(800, 600)
        creditWindow.setStyleSheet("background-image: url(:/creditImage/cd.png);")
        self.centralwidget = QtWidgets.QWidget(creditWindow)
        self.centralwidget.setObjectName("centralwidget")
        creditWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(creditWindow)
        QtCore.QMetaObject.connectSlotsByName(creditWindow)

    def retranslateUi(self, creditWindow):
        _translate = QtCore.QCoreApplication.translate
        creditWindow.setWindowTitle(_translate("creditWindow", "Credit"))

import credit_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    creditWindow = QtWidgets.QMainWindow()
    ui = Ui_creditWindow()
    ui.setupUi(creditWindow)
    creditWindow.show()
    sys.exit(app.exec_())

