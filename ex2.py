#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()   #使用super构造器方法返回父级的对象
        self.initUI()

    def initUI(self):
        self.setGeometry(500,200,1000,800)    #设置窗口的坐标和宽、高
        self.setWindowTitle('Icon')    #标题名称
        self.setWindowIcon(QIcon('web.jpeg'))   #显示图标
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
