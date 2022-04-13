# -*- encoding: utf-8 -*-
'''
@File    :   GetInfoWindow.py
@Time    :   2022/04/12 23:30:57
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''
from PySide6.QtWidgets import (
    QWidget, 
    QListWidget, 
    QHBoxLayout, 
    QFormLayout, 
    QStackedWidget, 
    QLineEdit,
    QRadioButton,
    QCheckBox,
    QLabel,
    QFileDialog,
    QPushButton,
    QGridLayout,
    QMainWindow
)
from view.OpenFileWidget import OpenFileWidget
from PySide6 import QtCore
from PySide6.QtCore import Signal

class GetInfoWindow(QMainWindow):
    def __init__(self):
        super(GetInfoWindow, self).__init__()
        self._widget = QWidget()
        # 設置視窗的初始位置跟大小、應用程式的標題
        self.setGeometry(1600,600,600,500)
        self.setWindowTitle('StackedWidget 例子')
        self.openfilewidget = OpenFileWidget()
        self.setCentralWidget(self.openfilewidget)
        # openfilewidget.show()
        # hbox = QHBoxLayout()
        # hbox.addWidget(self.openfilewidget)
        # hbox.addWidget(self.openfilewidget)
        # self._widget.setLayout(hbox)
        # self.setLayout(hbox)
        # openfilewidget.show()
