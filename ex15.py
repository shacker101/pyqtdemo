#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()       #创建QGridLayout实例
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',         #按钮名称
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]     #按钮位置列表

        for position, name in zip(positions, names):    #zip函数将列表positions和names中的元素一一对应
            if name == '':    #遇到空白字符串时跳过接下来的语句，进行下一轮循环
                continue
            button = QPushButton(name)        #创建按钮
            grid.addWidget(button, *position)     #position前加*代表将position“解包”

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
