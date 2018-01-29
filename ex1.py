#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    app=QApplication(sys.argv)         #每个PyQt5应用都必须创建一个应用对象

    w=QWidget()         #创建构造器
    w.resize(1000,800)      #resize()方法能改变控件的大小，这里的意思是窗口宽1000px，高800px
    w.move(500,200)      #move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(500, 200)的位置。注：屏幕坐标系的原点是屏幕的左上角。
    w.setWindowTitle('simple')   #给这个窗口添加了一个标题，标题在标题栏展示
    w.show()          #show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。

    sys.exit(app.exec_())
