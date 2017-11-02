# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\biancheng\Python\AOM\UI\Xiaozhi_Audio.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("04b_21")
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.record = QtWidgets.QPushButton(Dialog)
        self.record.setGeometry(QtCore.QRect(120, 130, 141, 31))
        self.record.setObjectName("record")
        self.continue_2 = QtWidgets.QPushButton(Dialog)
        self.continue_2.setGeometry(QtCore.QRect(120, 130, 141, 31))
        self.continue_2.setObjectName("continue_2")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(120, 180, 141, 31))
        self.exit.setObjectName("exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.record.setText(_translate("Dialog", "点我一下就可以说话啦"))
        self.continue_2.setText(_translate("Dialog", "继续聊"))
        self.exit.setText(_translate("Dialog", "挂掉电话"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

