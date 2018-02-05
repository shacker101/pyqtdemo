#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")             #创建两个按钮
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()         #水平布局
        hbox.addStretch(1)           #addStretch方法增加弹性空间
        hbox.addWidget(okButton)         #增加两个按钮
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()         #垂直布局
        vbox.addStretch(1)
        vbox.addLayout(hbox)       #把水平布局放到了一个垂直布局盒里面

        self.setLayout(vbox)         #创建布局

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
