#!/usr/bin/python3
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)        #将点击按钮与下面的showDialog方法连接

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')          #第一个参数是输入框的标题，第二个参数是输入框的占位符
                                                  #对话框返回输入内容和一个布尔值
        if ok:
            self.le.setText(str(text))            #在le上显示输入的内容

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
