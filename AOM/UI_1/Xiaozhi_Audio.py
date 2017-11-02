# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_Xiaozhi_Audio import Ui_Dialog
import pygame
import time
import sys
import os
os.chdir("../")
#print(os.getcwd())
sys.path.append(os.getcwd())
import audio as au
import os

class Xiaozhi_Audio(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Xiaozhi_Audio, self).__init__(parent)
        self.setupUi(self)
        self.continue_2.hide()
        self.exit.hide()

    
    @pyqtSlot()
    def on_record_pressed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.record.setText('小芝安静地听着')
        
        
    @pyqtSlot()
    def on_record_released(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
    @pyqtSlot()
    def on_record_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        os.system("E:/biancheng/Python/AOM/record.py")
        self.record.hide()
        #os.system("E:/biancheng/Python/AOM/audio.py")
        result = au.thinking()
        pygame.mixer.init() 
        pygame.mixer.music.load(result)
        if result =='data/audio/xiaozhi/Never be alone.mp3':
            pygame.mixer.music.play()
            time.sleep(30)
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.play()
        self.continue_2.show()
        self.exit.show()

    @pyqtSlot()
    def on_continue_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.continue_2.hide()
        self.exit.hide()
        self.record.show()
        self.record.setText('按一下就可以说话啦')
        
    def on_exit_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Xiaozhi_Audio()
    dlg.show()
    sys.exit(app.exec_())
    

