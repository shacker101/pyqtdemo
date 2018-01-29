import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class Example(QMainWindow):     #状态栏是由QMainWindow创建的
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')     #statusBar()创建状态栏，showMessage()显示状态栏信息
        self.setGeometry(500,200,1000,800)
        self.setWindowTitle('StatusBar')
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
