# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\biancheng\Python\AOM\UI\Menu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 411)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(150, 60, 241, 81))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(34)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(370, 110, 54, 12))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dictionary = QtWidgets.QPushButton(self.centralWidget)
        self.dictionary.setGeometry(QtCore.QRect(200, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        self.dictionary.setFont(font)
        self.dictionary.setObjectName("dictionary")
        self.maclean = QtWidgets.QPushButton(self.centralWidget)
        self.maclean.setGeometry(QtCore.QRect(200, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        self.maclean.setFont(font)
        self.maclean.setObjectName("maclean")
        self.xiaozhi = QtWidgets.QPushButton(self.centralWidget)
        self.xiaozhi.setGeometry(QtCore.QRect(200, 170, 161, 41))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        self.xiaozhi.setFont(font)
        self.xiaozhi.setObjectName("xiaozhi")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.xiaozhi.clicked.connect(MainWindow.hide)
        self.xiaozhi.clicked.connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "情感分析"))
        self.label_2.setText(_translate("MainWindow", "V1.0"))
        self.dictionary.setText(_translate("MainWindow", "基于词典的情感分析"))
        self.maclean.setText(_translate("MainWindow", "基于机器学习的情感分析"))
        self.xiaozhi.setText(_translate("MainWindow", "小芝"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

