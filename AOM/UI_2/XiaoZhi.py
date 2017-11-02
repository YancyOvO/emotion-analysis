from PyQt5.QtWidgets import QWidget, QApplication, QAction, QPushButton, QLabel, QTextEdit
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRect
import pygame
import time
import os
import re
import sys

sys.path.append(os.getcwd())
#print(os.getcwd())
import audio as au 

class Ui_XiaoZhi(QWidget):

    def __init__(self,  parent=None):
        width = 240
        height = 335
        
        super(Ui_XiaoZhi, self).__init__(parent,
                Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        screen = QApplication.desktop().screenGeometry()
        self.setGeometry(1030, screen.height()/3-50,width,height)
        #self.setWindowOpacity(0.7)#透明
       # self.setAttribute(Qt.WA_TranslucentBackground, True)#完全透明
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('UI_2/bg.jpg')))   # 设置背景图片
        self.setPalette(palette1)      
        
        quitAction = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=QApplication.instance().quit)
        self.addAction(quitAction)

        self.setContextMenuPolicy(Qt.ActionsContextMenu)#允许右键关闭
        
        path = QtGui.QPixmap('UI_2/images/xiaozhi.png')
        self.lb = QLabel(self)
        self.lb.setGeometry(QRect(0, 75, width, 50))
        self.lb.setAlignment(Qt.AlignCenter)
        self.lb.setPixmap(path)
        
        path2 = QtGui.QPixmap('UI_2/images/press.png')
        self.lb2 = QLabel(self)
        self.lb2.setGeometry(QRect(0, 250, width, 20))
        self.lb2.setAlignment(Qt.AlignCenter)
        self.lb2.setPixmap(path2)
        self.lb2.hide()
        
        self.text_button = QPushButton(self)
        self.text_button.setGeometry(QRect(67, 160, 107,42))       
        self.text_button.setStyleSheet("""QPushButton{background-image:url(UI_2/images/text_button);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/text_button_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/text_button_1);}""");


        self.voice_button = QPushButton(self)
        self.voice_button.setGeometry(QRect(67, 212, 107,42))       
        self.voice_button.setStyleSheet("""QPushButton{background-image:url(UI_2/images/voice_button);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/voice_button_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/voice_button_1);}""");

        self.ok_button = QPushButton(self)
        self.ok_button.setGeometry(QRect(67, 260, 107,42))       
        self.ok_button.setStyleSheet("""QPushButton{background-image:url(UI_2/images/ok_button);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/ok_button_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/ok_button_1);}""");
        self.ok_button.hide()
        
        self.record_button = QPushButton(self)
        self.record_button.setGeometry(QRect(75, 70, 87,87))       
        self.record_button.setStyleSheet("""QPushButton{background-image:url(UI_2/images/record_button);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:pressed{background-image:url(UI_2/images/record_button_1);}""");
        self.record_button.hide()
         
        self.txt = ''
        self.qte = QTextEdit(self)
        self.qte.setGeometry(QRect(50, 50, 140,180))     
        self.qte.hide()
        self.text_ok = False
        

        
        self.text_button.clicked.connect(self.on_text_button_clicked)
        self.voice_button.clicked.connect(self.on_voice_button_clicked)
        self.ok_button.clicked.connect(self.on_ok_button_clicked)
        self.qte.textChanged.connect(self.on_changed)
        self.record_button.clicked.connect(self.on_record_button_clicked)

    def on_changed(self):
        self.txt = self.qte.toPlainText()
        length = len(self.txt)
        for i in self.txt:
            if i == '\n':
                self.qte.undo()
        if length>110:
            self.qte.undo()
        #print(self.txt)


    def clear(self):
        self.lb.hide()
        self.text_button.hide()
        self.voice_button.hide()
    
    def on_text_button_clicked(self):
        self.clear()
        self.qte.show()
        self.ok_button.show()
        
    def on_ok_button_clicked(self):
        f=open('E:/biancheng/Python/AOM/outcome/xiaozhi_text/input.txt', 'a', encoding = 'utf-8')
        f.write('\n'+self.txt)
        f.close()
        
        self.close()
        
    def on_voice_button_clicked(self):
        self.clear()
        self.record_button.show()
        self.lb2.show()

     
    def on_record_button_clicked(self): 
        os.system("E:/biancheng/Python/AOM/record.py")      
        record = au.thinking()
        f = open("E:/biancheng/Python/AOM/outcome/xiaozhi_text/input.txt", "a", encoding = "UTF-8")
        if not record == '':
            f.write('\n#'+record[0])
            word = record[0]
            if re.findall('唱首歌', word):
                file_music = 'E:/biancheng/Python/AOM/data/audio/xiaozhi/Never be alone.mp3'
                #result = file_music
                pygame.mixer.init() 
                pygame.mixer.music.load(file_music)
                pygame.mixer.music.play()
                time.sleep(30)
                pygame.mixer.music.stop()
        else:
            f.write('\n#')
        f.close()

        print(record)
        self.close()


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = Ui_XiaoZhi()
    ui.show()
    sys.exit(app.exec_())    
