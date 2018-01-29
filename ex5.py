#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,200,1000,800)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Message','你确定要关闭窗口吗',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
         #创建了一个消息框，上面有俩按钮：Yes和No.第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，
         #第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的
        if reply==QMessageBox.Yes:       #根据返回值决定是否接受事件
            event.accept()
        else:
            event.ignore()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
