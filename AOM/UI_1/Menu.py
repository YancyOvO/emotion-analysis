# -*- coding: utf-8 -*-



from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_Menu import Ui_MainWindow
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_xiaozhi_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.hide()
        os.system("Xiaozhi_Choose.py")
        self.show()
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
