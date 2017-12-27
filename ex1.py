#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    app=QApplication(sys.argv)

    w=QWidget()
    w.resize(1000,800)
    w.move(500,200)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec_())
