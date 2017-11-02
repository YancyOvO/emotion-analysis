# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_Xiaozhi_Choose import Ui_Dialog
import os

class Xiaozhi_Choose(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Xiaozhi_Choose, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_audio_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.hide()
        os.system('Xiaozhi_Audio.py')
        self.close()
    
    @pyqtSlot()
    def on_text_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.hide()
        os.system('Xiaozhi_Text.py')
        self.close()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Xiaozhi_Choose()
    dlg.show()
    sys.exit(app.exec_())
