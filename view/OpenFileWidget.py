# -*- encoding: utf-8 -*-
'''
@File    :   OpenFileWidget.py
@Time    :   2022/04/12 23:28:30
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, 
    QFormLayout, 
    QLabel,
    QPushButton,
    QGridLayout,
    QFileDialog,
)

class OpenFileWidget(QWidget):
    def __init__(self):
        super(OpenFileWidget, self).__init__()
        # 目的路徑
        #设置窗口初始位置和大小
        # self.setGeometry(1600,600,600,500)
        
        g_layout = QGridLayout()
        openfile = self._FileOpen()
        g_layout.addLayout(openfile, 0, 0)
        self.setLayout(g_layout)
        self._SetupOpenFile()
        
    def _FileOpen(self):
        self.open_file_btn = QPushButton('open')
        self.show_file_path = QLabel()
        f_layout = QFormLayout()
        f_layout.addRow(self.open_file_btn, self.show_file_path)
        # h_layout.addWidget(self.show_file_path)
        return f_layout
    
    def _SetupOpenFile(self):
        self.open_file_btn.clicked.connect(self.OpenFileNameDialog)
        self.open_file_btn.setIcon(QIcon('./media/import.svg'))
        
    def OpenFileNameDialog(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Open file", 
                                                         "./",
                                                         "Python Files (*.py);;All Files (*)")
        print(filename, filetype)
        self.show_file_path.setText(filename)
        
    def OpenFolderDialog(self):
        filename = QFileDialog.getExistingDirectory(self,
                                                    "Open file",
                                                    "./",)
        print(filename)
        self.show_file_path.setText(filename)
        