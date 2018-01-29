#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))       #设置提示框的字体
        self.setToolTip('这是一个<b>QWidget</> widget')   #调用setTooltip()创建提示框可以使用富文本格式的内容，鼠标移动到窗口内的空白位置时可以显示这条提示

        btn=QPushButton('Button',self)           #创建一个按钮
        btn.setToolTip('这是一个<b>QPushButton</b> widget')    #为按钮添加了一个提示框，鼠标移动到按钮时会显示这条提示
        btn.resize(btn.sizeHint())         #调整按钮大小，sizeHint()方法提供了一个默认的按钮大小
        btn.move(100,80)

        self.setGeometry(800,500,300,200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
