#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)       #Qt.AlignTop代表置顶

        self.setMouseTracking(True)          #打开鼠标跟踪，实测只能跟踪在应用窗口中的移动

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()           #获取x轴坐标
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)            #改变标签名称

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
