# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\biancheng\Python\AOM\UI\Xiaozhi_Choose.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.audio = QtWidgets.QPushButton(Dialog)
        self.audio.setGeometry(QtCore.QRect(140, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(9)
        self.audio.setFont(font)
        self.audio.setObjectName("audio")
        self.text = QtWidgets.QPushButton(Dialog)
        self.text.setGeometry(QtCore.QRect(140, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.audio.setText(_translate("Dialog", "想和你通电话"))
        self.text.setText(_translate("Dialog", "想和你打字呢"))
        self.label.setText(_translate("Dialog", "小芝"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

