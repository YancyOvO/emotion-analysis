# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\biancheng\Python\AOM\UI\Xiaozhi_Text.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 232)
        Dialog.setSizeGripEnabled(True)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 80, 256, 41))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(60, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")
        self.pushbutton_ok = QtWidgets.QPushButton(Dialog)
        self.pushbutton_ok.setGeometry(QtCore.QRect(90, 150, 75, 23))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(8)
        self.pushbutton_ok.setFont(font)
        self.pushbutton_ok.setObjectName("pushbutton_ok")
        self.pushbutton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushbutton_cancel.setGeometry(QtCore.QRect(220, 150, 75, 23))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(8)
        self.pushbutton_cancel.setFont(font)
        self.pushbutton_cancel.setObjectName("pushbutton_cancel")
        self.label_outcome = QtWidgets.QLabel(Dialog)
        self.label_outcome.setGeometry(QtCore.QRect(120, 90, 141, 16))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(8)
        self.label_outcome.setFont(font)
        self.label_outcome.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_outcome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_outcome.setText("")
        self.label_outcome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_outcome.setObjectName("label_outcome")

        self.retranslateUi(Dialog)
        self.pushbutton_cancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "请写下您的评论："))
        self.pushbutton_ok.setText(_translate("Dialog", "确定"))
        self.pushbutton_cancel.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

