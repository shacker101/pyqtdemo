#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct=QAction(QIcon('exit.jpeg'), '&Exit', self)        #QAction第一个参数是菜单选项的图标，第二个是选项的名称
        exitAct.setShortcut('Ctrl+Q')         #设定快捷键
        exitAct.setStatusTip('Exit application')       #当鼠标移动到选项时在状态栏显示Exit application
        exitAct.triggered.connect(qApp.quit)        #将动作与事件联系

        self.statusBar()

        menubar=self.menuBar()        #menuBar()创建菜单栏
        fileMenu=menubar.addMenu('&File')        #添加叫做File的菜单
        fileMenu.addAction(exitAct)        #添加上面创建的退出动作

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

if __name__ == '__main__':

    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
