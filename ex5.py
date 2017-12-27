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
            #最后一个参数代表默认选中哪个
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
