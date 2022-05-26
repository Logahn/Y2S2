#!/usr/bin/env python3
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtQml import QQmlApplicationEngine
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./pyqt.qml')
sys.exit(app.exec())

