#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

import sys
import time
import os
from PyQt5.QtCore import QCoreApplication, Qt, QSize
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog

IMAGES_DIR = os.path.join(os.getcwd(), 'pyspace', 'res', 'images')


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 800, 500)
        self.setWindowTitle('PySpace Launcher')
        self.setWindowIcon(QIcon('pic.png'))

        action_quit = QAction('&Quit', self)
        action_quit.setShortcut('Ctrl+Q')
        action_quit.setStatusTip('Quit Program')
        action_quit.triggered.connect(self.close_application)

        action_camera_select = QAction('&Adjust', self)
        action_camera_select.setShortcut('Ctrl+C')
        action_camera_select.setStatusTip('Adjust Camera Settings')
        action_camera_select.triggered.connect(self.adjust_camera_settings)

        action_render = QAction('&Render Recording', self)
        action_render.setShortcut('Ctrl+R')
        action_render.setStatusTip('Select Recording To Render')
        action_render.triggered.connect(self.select_recording)

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(action_quit)

        editorMenu = mainMenu.addMenu('&Camera')
        editorMenu.addAction(action_camera_select)

        rendorMenu = mainMenu.addMenu('&Render')
        rendorMenu.addAction(action_render)

        self.home()

    def adjust_camera_settings(self):
        #TODO Create menu with selection of low/med/high/custom camera parameters and
        #     comboboxes for the most important camera params.
        pass

    def select_recording(self):
        qfd = QFileDialog()
        path = os.path.join(os.getcwd(), 'recordings')
        if not os.path.exists(path):
            os.makedirs(path)
        filter = "npy(*.npy)"
        filename = QFileDialog.getOpenFileName(qfd, 'Select Recording File', path, filter)
        #TODO: Launch ray_marcher and immediately use the playback function
        #TODO: Add progress bar for rendering process. Might be tricky due to comms with ray_marcher.py
        '''
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        '''

    def home(self):
        self.btn = QPushButton(QIcon(os.path.join(IMAGES_DIR, 'testing.png')), '', self)
        self.btn.setGeometry(111,111,128,128)
        self.btn.setIconSize(QSize(128, 128))
        self.btn.clicked.connect(self.close_application)
        
        self.show()

    def close_application(self):

        if (choice := QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)) == QMessageBox.Yes:
            sys.exit()
        else:
            pass

def run():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('motif'))
    Gui = window()
    sys.exit(app.exec_())

run()

''' 
----------- Useful QT things -------------- 
self.setGeometry(50, 50, 1000, 600)     # Set the window geometry

checkBox = QCheckBox('Text with checkbox', self)
checkBox.toggle()  # if you want to be checked in in the begin
checkBox.move(x, y)
checkBox.stateChanged.connect(self.checkbox_callback)

comboBox = QComboBox(self)
comboBox.addItem('motif')
comboBox.addItem('Windows')

QApplication.setStyle(QStyleFactory.create('motif'))   # Some styles -- 'motif' 'Windows' 'cde' 'Plastique' 'Cleanlooks' 'windowsvista'

self.progress = QProgressBar(self)
self.progress.setGeometry(200, 80, 250, 20)
self.progress.setValue(0-100)

self.btn = QPushButton('download', self)
self.btn.move(x, y)
self.btn.clicked.connect(self.download)

self.textEdit = QTextEdit()
self.setCentralWidget(self.textEdit)    # Creates a text editor and makes it the focus

color = QColorDialog.getColor()         # Pops up with menu to select color from palette
self.styleChoice.setStyleSheet('QWidget{background-color: %s}' % color.name())
'''
