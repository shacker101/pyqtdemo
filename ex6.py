#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 800)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qtRectangle=self.frameGeometry()  #得到主窗口大小
        centerPoint=QDesktopWidget().availableGeometry().center()  #得到屏幕中心点的位置
        qtRectangle.moveCenter(centerPoint)    #把qtRectangle的中心点移到屏幕的中心点,这两行代码看不懂
        self.move(qtRectangle.topLeft())   #把主窗口左上角的坐标改为此时qtRectangle左上角的坐标，这样主窗口的中心点就在屏幕的中心


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
