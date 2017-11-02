# -*- coding: utf-8 -*-

"""
Module implementing Judgment.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_Xiaozhi_Text import Ui_Dialog


class Xiaozhi_Text(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Xiaozhi_Text, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushbutton_ok_clicked(self):
        self.label_outcome.setText('您的心情不错呢')#好乱好乱，小芝凌乱了
        self.textEdit.hide()
       
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Xiaozhi_Text()
    dlg.show()
    sys.exit(app.exec_())
