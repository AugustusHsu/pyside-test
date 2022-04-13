# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/03/31 20:10:52
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

import sys
from view.OpenFileWidget import OpenFileWidget
from view.StackedWidget import StackedExample
from view.GetInfoWindow import GetInfoWindow
from PySide6 import QtWidgets
import controller
from openwindowsctr import Controller

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app = QtWidgets.QApplication([])    
    # ctr = controller.Controller()
    # ctr = Controller()
    # ctr.show()
    view = GetInfoWindow()
    view.show()
    
    app.exec()
