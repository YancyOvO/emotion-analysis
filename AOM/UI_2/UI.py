from PyQt5.QtCore import Qt, QRect, QTimer
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QAction, QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
#from XiaoZhi import Ui_XiaoZhi
import pygame
import os
os.chdir("../") 



import MacLean
import Dictionary

class Ui_MainWindow(QWidget):

    def __init__(self, parent=None):
        width = 480
        height = 670
        
        super(Ui_MainWindow, self).__init__(parent,
                Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        screen = QApplication.desktop().screenGeometry()
        self.setGeometry(440, screen.height()/20,width,height)
        #self.setWindowOpacity(0.7)#透明
       # self.setAttribute(Qt.WA_TranslucentBackground, True)#完全透明
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('UI_2/bg.jpg')))   # 设置背景图片
        self.setPalette(palette1)      
        
        quitAction = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=QApplication.instance().quit)
        self.addAction(quitAction)

        self.setContextMenuPolicy(Qt.ActionsContextMenu)#允许右键关闭
        
        #hbox = QHBoxLayout(self)
        path = QtGui.QPixmap('UI_2/images/logo.png')
        self.lb1 = QLabel(self)
        self.lb1.setGeometry(QRect(0, 0, 480, 407))
        self.lb1.setPixmap(path)
        
        path2 = QtGui.QPixmap('UI_2/images/frame.png')
        self.lb2 = QLabel(self)
        self.lb2.setGeometry(QRect(0, 400, 480, 10))
        self.lb2.setPixmap(path2)
        
        path3 = QtGui.QPixmap('outcome/plt_outcome.png')
        self.lb3 = QLabel(self)
        self.lb3.setGeometry(QRect(260, 350, 240, 240))
        self.lb3.setPixmap(path3)
        self.lb3.hide()
        
        self.button1 = QPushButton(self)
        self.button1.setGeometry(QRect(-10, 410, 500, 65))       
        #self.dict.resize(480, 63)     #sizeHant表示给出推荐大小按钮 

        self.button1.setStyleSheet("""QPushButton{background-image:url(UI_2/images/button1);background-repeat: repeat-xy;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/button1_0);}""");
       
       # button.move(0, height*3/4)  
        self.button2 = QPushButton(self)
        self.button2.setGeometry(QRect(-10, 475, 500, 63))       
        self.button2.setStyleSheet("""QPushButton{background-image:url(UI_2/images/button2);background-repeat: repeat-xy;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/button2_0);}""");
        self.button3 = QPushButton(self)
        self.button3.setGeometry(QRect(-10, 538, 500, 63))       
        self.button3.setStyleSheet("""QPushButton{background-image:url(UI_2/images/button3);background-repeat: repeat-xy;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/button3_0);}""");
        self.button4 = QPushButton(self)
        self.button4.setGeometry(QRect(-10, 600, 500, 63))       
        self.button4.setStyleSheet("""QPushButton{background-image:url(UI_2/images/button4);background-repeat: repeat-xy;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/button4_0);}""");

        self.dict_button1 = QPushButton(self)
        self.dict_button1.setGeometry(QRect(60, 580, 107,42))       
        self.dict_button1.setStyleSheet("""QPushButton{background-image:url(UI_2/images/dict_button1);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/dict_button1_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/dict_button1_1);}""");
        self.dict_button1.hide()

        self.dict_button2 = QPushButton(self)
        self.dict_button2.setGeometry(QRect(width-167, 580, 107,42))       
        self.dict_button2.setStyleSheet("""QPushButton{background-image:url(UI_2/images/dict_button2);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/dict_button2_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/dict_button2_1);}""");
        self.dict_button2.hide()
        
        
        self.mac_button1 = QPushButton(self)
        self.mac_button1.setGeometry(QRect(60, 580, 107,42))       
        self.mac_button1.setStyleSheet("""QPushButton{background-image:url(UI_2/images/dict_button1);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/dict_button1_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/dict_button1_1);}""");
        self.mac_button1.hide()       


        self.mac_button2 = QPushButton(self)
        self.mac_button2.setGeometry(QRect(width-167, 580, 107,42))       
        self.mac_button2.setStyleSheet("""QPushButton{background-image:url(UI_2/images/dict_button2);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/dict_button2_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/dict_button2_1);}""");
        self.mac_button2.hide() 
        
        self.xiaozhi_button2 = QPushButton(self)
        self.xiaozhi_button2.setGeometry(QRect(width-167, 580, 107,42))       
        self.xiaozhi_button2.setStyleSheet("""QPushButton{background-image:url(UI_2/images/dict_button2);background-repeat: repeat;
                                               background-position: center;background-attachment: fixed;
                                               background-clip: padding;background-color:transparent;}
                                               QPushButton:hover{background-image:url(UI_2/images/dict_button2_0);}
                                               QPushButton:pressed{background-image:url(UI_2/images/dict_button2_1);}""");
        self.xiaozhi_button2.hide() 

        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button3.clicked.connect(self.on_button3_clicked)
        
        self.dict_button1.clicked.connect(self.on_dict_button1_clicked)
        self.dict_button2.clicked.connect(self.on_dict_button2_clicked)
        self.mac_button1.clicked.connect(self.on_mac_button1_clicked)
        self.mac_button2.clicked.connect(self.on_mac_button2_clicked)
        self.xiaozhi_button2.clicked.connect(self.on_xiaozhi_button2_clicked)
       #定时刷新文本(滚动)
        self.dictButton1 = False
        self.dictButtonBack = False
        self.macButton1 = False
        self.macButtonBack = False
        self.xiaozhiButton1 = False 
        self.xiaozhiButtonBack = False

        self.t = QTimer()
        self.txt = open('outcome/dict.txt', 'r', encoding = 'utf-8')
        self.txt2 = open('outcome/mac.txt', 'r', encoding = 'utf-8')
        self.newX = 0  
        self.newY = 0
        self.high = 22
        self.font = QtGui.QFont(('Adobe 楷体 Std R'), 11)
        self.t.timeout.connect(self.changeTxtPosition)
        self.newLine = []
        self.outcome1 = []
        self.outcome2 = []
        self.outcome3 = []
        for line in self.txt:
            if not line == '/n':
                self.outcome1.append(line)
        self.clearLine1 = []
        for l in range(0, len(self.outcome1)):
            self.clearLine1.append('')
            
        for line in self.txt2:
            if not line == '/n':
                self.outcome2.append(line)
        self.clearLine2 = []
        for l in range(0, len(self.outcome2)):
            self.clearLine2.append('')
            
        self.clearLine3 = []
        self.i = 0
        
        #self.xiaozhi = Ui_XiaoZhi()


    def clear(self):
        self.lb1.hide()
        self.lb2.hide()
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.hide()
    
    def back(self):
        self.lb1.show()
        self.lb2.show()
        self.button1.show()
        self.button2.show()
        self.button3.show()
        self.button4.show()   


    def on_button1_clicked(self):
        self.clear()       
        self.dict_button1.show()
        self.dict_button2.show()

    def on_button2_clicked(self):
        
        self.clear()       
        self.mac_button1.show()
        self.mac_button2.show()
        

    def on_button3_clicked(self):

        self.clear()       
        os.system('UI_2\XiaoZhi.py')

        
        #f=open('E:/biancheng/Python/AOM/outcome/xiaozhi_text/input.txt', 'r', encoding = 'utf-8')
#        lines = f.readlines()
#        data = lines[-1]
        #f.close()
        outcome = Dictionary.audio(open("outcome/xiaozhi_text/input.txt",'r',encoding='utf-8'))
        emo = outcome[-1]
        if emo == 0:
            file_music ='data/audio/xiaozhi/no_emo.mp3'
        elif emo<0:
            file_music ='data/audio/xiaozhi/sad.mp3'
        elif emo >0:
            file_music ='data/audio/xiaozhi/pleasant.mp3'
        result = file_music
        pygame.mixer.init() 
        pygame.mixer.music.load(result)
        pygame.mixer.music.play()
        self.outcome3 = []
        self.clearLine3 = []
        self.txt3=open('outcome/record.txt', 'r', encoding = 'utf-8')
        for line in self.txt3:
            if not line == '/n':
                self.outcome3.append(line)
        for l in range(0, len(self.outcome3)):
            self.clearLine3.append('')
        self.txt3.close()
        self.xiaozhiButton1 = True
        self.xiaozhi_button2.show()
        print(outcome)
#        self.xiaozhi.show()
#        text = self.xiaozhi.qte.toPlainText()
        

    def on_dict_button1_clicked(self):
        
        self.dictButton1 = True

    def on_dict_button2_clicked(self):
        
        self.dict_button1.hide()
        self.dict_button2.hide() 
        self.dictButton1 = False 
        self.dictButtonBack = True
        self.lb3.hide()
        self.back()

    def on_mac_button1_clicked(self):
        
        self.macButton1 = True

    def on_mac_button2_clicked(self):
        
        self.mac_button1.hide()
        self.mac_button2.hide() 
        self.macButton1 = False 
        self.macButtonBack = True
        self.lb3.hide()
        self.back()

    def on_xiaozhi_button2_clicked(self):

        self.xiaozhi_button2.hide() 
        self.xiaozhiButton1 = False 
        self.xiaozhiButtonBack = True
        self.lb3.hide()
        self.back()        
        
    def changeTxtPosition(self):
        if self.dictButton1 == True:
            if self.i <len(self.newLine)-1:#逐行打印
                self.newY += 22
                self.i+=1
        if self.macButton1 == True:
            if self.i <len(self.newLine)-1:#逐行打印
                self.newY += 22
                self.i+=1
        if self.xiaozhiButton1 == True:
            if self.i <len(self.newLine)-1:#逐行打印
                self.newY += 22
                self.i+=1               
#        if self.bton3 == True:
#            if self.newX < self.textRect.width():
#            #每次向前滚动5像素
#                self.newX += 3
#            if self.newX>=self.textRect.width() and self.i <len(self.newLine)-1:#逐行打印
#                self.newY += 17.5
#                self.i+=1
#                self.newX = 0

        #print(len(self.newLine))
        self.update()
    
    def setText(self, s):
        if self.newLine == self.outcome1:
             self.txt = s
        if self.newLine == self.outcome2:
             self.txt2 = s
        if self.newLine == self.outcome3:
             self.txt3 = s
        #滚动起始位置设置为10,留下视觉缓冲
        #以免出现 “没注意到第一个字是什么” 的情况
        self.newX = 0
        self.update()
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setFont(self.font)
        self.drawWidget(qp)
        qp.end()
    def drawWidget(self, qp):
        if self.dictButton1 == True:
            self.newLine = self.outcome1
            qp.setPen(QtGui.QColor('transparent'))  
            self.textRect = qp.drawText(QRect(0, 0, 50, 25), Qt.AlignHCenter | Qt.AlignVCenter, self.newLine[self.i])
            qp.setPen(QtGui.QColor(255, 255, 255, 255))
            qp.drawText(QRect(self.width()/8, self.height()/14+self.newY, self.width(), 17.5), Qt.AlignLeft| Qt.AlignTop, self.newLine[self.i])
            if self.i == len(self.newLine)-1:
                path3 = QtGui.QPixmap('outcome/plt_outcome.png')
                self.lb3.setPixmap(path3)
                self.lb3.show()
            self.t.start(450)
        if self.dictButtonBack == True:
            self.newLine = self.clearLine1
            self.i = 0
            self.newY = 0
            self.dictButtonBack = False
            
        if self.macButton1 == True:
            self.newLine = self.outcome2
            qp.setPen(QtGui.QColor('transparent'))  
            self.textRect = qp.drawText(QRect(0, 0, 50, 25), Qt.AlignHCenter | Qt.AlignVCenter, self.newLine[self.i])
            qp.setPen(QtGui.QColor(255, 255, 255, 255))
            qp.drawText(QRect(self.width()/8, self.height()/14+self.newY, self.width(), 17.5), Qt.AlignLeft| Qt.AlignTop, self.newLine[self.i])
            if self.i == len(self.newLine)-1:
                path3 = QtGui.QPixmap('outcome/plt_outcome.png')
                self.lb3.setPixmap(path3)
                self.lb3.show()
            self.t.start(450)
        if self.macButtonBack == True:
            self.newLine = self.clearLine2
            self.i = 0
            self.newY = 0
            self.macButtonBack = False
            
        if self.xiaozhiButton1 == True:
            self.newLine = self.outcome3
            qp.setPen(QtGui.QColor('transparent'))  
            self.textRect = qp.drawText(QRect(0, 0, self.width()*3/4, 25), Qt.AlignHCenter | Qt.AlignVCenter, self.newLine[self.i])
            qp.setPen(QtGui.QColor(255, 255, 255, 255))
            qp.drawText(QRect(self.width()/8, self.height()/14+self.newY, self.width()*3/4, 17.5), Qt.AlignLeft| Qt.AlignTop, self.newLine[self.i])
            if self.i == len(self.newLine)-1:
                path3 = QtGui.QPixmap('outcome/plt_outcome.png')
                self.lb3.setPixmap(path3)
                self.lb3.show()
            self.t.start(450)
        if self.xiaozhiButtonBack == True:
            self.newLine = self.clearLine3
            self.i = 0
            self.newY = 0
            self.xiaozhiButtonBack = False
            #每50ms毫秒滚动一次
            

        
        for j in range(0, self.i):
            qp.drawText(QRect(self.width()/8, self.height()/14+j*self.high, self.width()*3/4, self.newY-j*self.high), Qt.AlignLeft| Qt.AlignTop, self.newLine[j])
      
#            固定滚动的上一行
#            #如果绘制文本宽度小于控件宽度，不需要滚动，文本居中对齐
#            qp.setPen(QtGui.QColor(255, 255, 255, 255));
#            self.textRect = qp.drawText(QRect(0, -7, 50, 25), Qt.AlignHCenter | Qt.AlignVCenter, self.txt)
#            self.t.stop()g

    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
#    clock = ShapedClock()
#    clock.show()
    sys.exit(app.exec_())    


