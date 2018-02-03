#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')      #这两行可以简写为self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)    #checkable=True令菜单可选
        viewStatAct.setChecked(True)         #默认设置为选中状态
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.triggered.connect(self.toggleMenu)    #与下面的toggleMenu连接

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):       #切换状态栏的显示与否
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
