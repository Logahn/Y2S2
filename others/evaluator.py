#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluator.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1267, 681)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("selection-background-color: rgb(0, 54, 255);\n"
"background-color: rgb(22, 173, 223);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 591, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label2 = QtWidgets.QLabel(self.layoutWidget)
        self.label2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label2.setText("<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Объем предоставляемых услуг</span></p></body></html>")
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setScaledContents(True)
        self.label2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label2.setObjectName("label2")
        self.verticalLayout_5.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(self.layoutWidget)
        self.label3.setObjectName("label3")
        self.verticalLayout_5.addWidget(self.label3)
        self.label4 = QtWidgets.QLabel(self.layoutWidget)
        self.label4.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label4.setText("<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Уровень защиты данных</span></p></body></html>")
        self.label4.setTextFormat(QtCore.Qt.AutoText)
        self.label4.setScaledContents(True)
        self.label4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label4.setObjectName("label4")
        self.verticalLayout_5.addWidget(self.label4)
        self.label5 = QtWidgets.QLabel(self.layoutWidget)
        self.label5.setObjectName("label5")
        self.verticalLayout_5.addWidget(self.label5)
        self.label6 = QtWidgets.QLabel(self.layoutWidget)
        self.label6.setObjectName("label6")
        self.verticalLayout_5.addWidget(self.label6)
        self.label7 = QtWidgets.QLabel(self.layoutWidget)
        self.label7.setObjectName("label7")
        self.verticalLayout_5.addWidget(self.label7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.comboBox1 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setKerning(True)
        self.comboBox1.setFont(font)
        self.comboBox1.setAutoFillBackground(False)
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox1)
        self.comboBox2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox2.setFont(font)
        self.comboBox2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox2)
        self.comboBox3 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox3.setFont(font)
        self.comboBox3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox3)
        self.comboBox4 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox4.setFont(font)
        self.comboBox4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox4)
        self.comboBox5 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox5.setFont(font)
        self.comboBox5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox5.setFrame(True)
        self.comboBox5.setObjectName("comboBox5")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.comboBox5.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox5)
        self.comboBox6 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox6.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox6.setFont(font)
        self.comboBox6.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox6.setFrame(True)
        self.comboBox6.setObjectName("comboBox6")
        self.comboBox6.addItem("")
        self.comboBox6.addItem("")
        self.comboBox6.addItem("")
        self.comboBox6.addItem("")
        self.comboBox6.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(250, 20, 231, 21))
        self.label1.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label1.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; color:#ffffff;\">Положительные критерии</span></p></body></html>")
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setScaledContents(True)
        self.label1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label1.setObjectName("label1")
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(780, 20, 231, 21))
        self.label8.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label8.setText("<html><head/><body><p align=\"center\"><span style=\" font-family:\'Liberation Serif,serif\'; font-size:14pt; font-weight:600; color:#ffffff;\">Отрицательные критерии</span></p></body></html>")
        self.label8.setTextFormat(QtCore.Qt.AutoText)
        self.label8.setScaledContents(True)
        self.label8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label8.setObjectName("label8")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(640, 510, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(11)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(660, 70, 271, 351))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label9.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label9.setText("<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Сложность интерфейса</span></p></body></html>")
        self.label9.setTextFormat(QtCore.Qt.AutoText)
        self.label9.setScaledContents(True)
        self.label9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label9.setObjectName("label9")
        self.verticalLayout_7.addWidget(self.label9)
        self.label10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label10.setObjectName("label10")
        self.verticalLayout_7.addWidget(self.label10)
        self.label11 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label11.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label11.setText("<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Административность ресурса</span></p></body></html>")
        self.label11.setTextFormat(QtCore.Qt.AutoText)
        self.label11.setScaledContents(True)
        self.label11.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label11.setObjectName("label11")
        self.verticalLayout_7.addWidget(self.label11)
        self.label12 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label12.setObjectName("label12")
        self.verticalLayout_7.addWidget(self.label12)
        self.label13 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label13.setObjectName("label13")
        self.verticalLayout_7.addWidget(self.label13)
        self.label_percent = QtWidgets.QLabel(self.centralwidget)
        self.label_percent.setGeometry(QtCore.QRect(780, 510, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(11)
        self.label_percent.setFont(font)
        self.label_percent.setObjectName("label_percent")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(930, 50, 271, 401))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox7 = QtWidgets.QComboBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setKerning(True)
        self.comboBox7.setFont(font)
        self.comboBox7.setAutoFillBackground(False)
        self.comboBox7.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox7.setObjectName("comboBox7")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.comboBox7.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox7)
        self.comboBox8 = QtWidgets.QComboBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox8.setFont(font)
        self.comboBox8.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox8.setObjectName("comboBox8")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.comboBox8.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox8)
        self.comboBox9 = QtWidgets.QComboBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox9.setFont(font)
        self.comboBox9.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox9.setObjectName("comboBox9")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.comboBox9.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox9)
        self.comboBox10 = QtWidgets.QComboBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox10.setFont(font)
        self.comboBox10.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox10.setObjectName("comboBox10")
        self.comboBox10.addItem("")
        self.comboBox10.addItem("")
        self.comboBox10.addItem("")
        self.comboBox10.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox10)
        self.comboBox11 = QtWidgets.QComboBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.comboBox11.setFont(font)
        self.comboBox11.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox11.setFrame(True)
        self.comboBox11.setObjectName("comboBox11")
        self.comboBox11.addItem("")
        self.comboBox11.addItem("")
        self.comboBox11.addItem("")
        self.comboBox11.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox11)
        self.label_comment = QtWidgets.QLabel(self.centralwidget)
        self.label_comment.setGeometry(QtCore.QRect(620, 540, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(11)
        self.label_comment.setFont(font)
        self.label_comment.setText("")
        self.label_comment.setScaledContents(False)
        self.label_comment.setAlignment(QtCore.Qt.AlignCenter)
        self.label_comment.setWordWrap(True)
        self.label_comment.setObjectName("label_comment")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(430, 500, 146, 81))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_result = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(11)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut_2 = QtWidgets.QAction(MainWindow)
        self.actionCut_2.setObjectName("actionCut_2")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionReplace = QtWidgets.QAction(MainWindow)
        self.actionReplace.setObjectName("actionReplace")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut_2)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionReplace)
        self.menuSettings.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.result)
    def result(self, out):

     # ! Positive criteria
        index1 = self.comboBox1.currentIndex()
        if index1 == 1:
            out= out+ 16
        elif index1 == 2:
            out= out+ 8 
        elif index1 ==3:
            out= out+ 0
                
        index2 = self.comboBox2.currentIndex()
        if index2 == 1:
            out= out+ 16
        elif index2 == 2:
            out= out+ 8  
        elif index2 ==3:
            out= out+ 0

        index3 = self.comboBox3.currentIndex()
        if index3 == 1:
            out= out+ 16
        elif index3 == 2:
            out= out+ 8  
        elif index3 ==3:
            out= out+ 0
                
        index4 = self.comboBox4.currentIndex()
        if index4 == 1:
            out= out+ 16
        elif index4 == 2:
            out= out+ 8    
        elif index4 ==3:
            out= out+ 0
        
        index5 = self.comboBox5.currentIndex()
        if index5 == 1:
            out= out+ 16
        elif index5 == 2:
            out= out+ 8  
        elif index5 ==3:
            out= out + 0

        index6 = self.comboBox6.currentIndex()
        if index6 == 1:
            out= out+ 0
        elif index6 == 2:
            out= out+ 7    
        elif index6 ==3:
            out= out+ 14   
        elif index6 == 4 :
            out= out+ 20

        #!  Negative  Criteria

        index7 = self.comboBox7.currentIndex()
        if index7 == 1:
            out = out + 0
        elif index7 == 2:
            out = out - 10     
        elif index7 ==3:
            out = out - 20
                
        index8 = self.comboBox8.currentIndex()
        if index8 == 1:
            out= out+ 0
        elif index8 == 2:
            out= out- 10     
        elif index8 ==3:
            out= out- 20

        index9 = self.comboBox9.currentIndex()
        if index9 == 1:
            out= out+ 0
        elif index9 == 2:
            out= out- 10     
        elif index9 ==3:
            out= out- 20
                
        index10 = self.comboBox10.currentIndex()
        if index10 == 1:
            out= out+ 0
        elif index10 == 2:
            out= out- 10     
        elif index10 ==3:
            out= out- 20
        
        index11 = self.comboBox11.currentIndex()
        if index11 == 1:
            out= out+ 0
        elif index11 == 2:
            out= out- 10     
        elif index11 ==3:
            out= out- 20

        if index1 == 0 or index2 == 0 or index3 == 0 or index4 == 0 or index5 == 0 or index6 == 0:
            comment = "Не все положительные критерии были определены"
        elif index7 == 0 or index8 == 0 or index9 == 0 or index10 == 0 or index11 == 0:
            comment = "Не все отрицательные критерии были определены"
        elif out >= 80:
            comment = "Данная Информационная система соответствует ожиданиям."
        elif out >= 60 and out < 80:
            comment = "Данная Информационная система может соответствовать вашим ожиданиям."
        elif out < 60:
            comment = "Данная информационная система меньше, чем ожидалось."
        

        self.label_percent.setText(str(out) + "%")
        self.label_comment.setText(comment)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evaluator"))
        self.label3.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Локализация ИС</span></p></body></html>"))
        self.label5.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Реализация удаленного доступа</span></p></body></html>"))
        self.label6.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Обратная связь</span></p></body></html>"))
        self.label7.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Качества поддержки</span></p></body></html>"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "Обширный"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "Полный"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "Неполный"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "Надежная"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "Частичная"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "Отсутствие"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "Строго регламентированный"))
        self.comboBox3.setItemText(2, _translate("MainWindow", "Чувствительный"))
        self.comboBox3.setItemText(3, _translate("MainWindow", "Базовый уровень"))
        self.comboBox4.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox4.setItemText(1, _translate("MainWindow", "Немедленный доступ"))
        self.comboBox4.setItemText(2, _translate("MainWindow", "Доступ к конечной точке"))
        self.comboBox4.setItemText(3, _translate("MainWindow", "Неэффективный доступ"))
        self.comboBox5.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox5.setItemText(1, _translate("MainWindow", "Реальные отзывы"))
        self.comboBox5.setItemText(2, _translate("MainWindow", "Сомнительная система"))
        self.comboBox5.setItemText(3, _translate("MainWindow", "Нет отзывов"))
        self.comboBox6.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox6.setItemText(1, _translate("MainWindow", "Нет поддержки"))
        self.comboBox6.setItemText(2, _translate("MainWindow", "Реализация одного варианта"))
        self.comboBox6.setItemText(3, _translate("MainWindow", "Реализация двух вариантов"))
        self.comboBox6.setItemText(4, _translate("MainWindow", "Многовариантная реализация"))
        self.label_output.setText(_translate("MainWindow", "Вывод по ресурсу:"))
        self.label10.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Наличие ненужной информации</span></p></body></html>"))
        self.label12.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Наличие гарантии</span></p></body></html>"))
        self.label13.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Liberation Serif,serif\'; font-weight:600; color:#ffffff;\">Приемлемость модификации</span></p></body></html>"))
        self.label_percent.setText(_translate("MainWindow", "0%"))
        self.comboBox7.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox7.setItemText(1, _translate("MainWindow", "Удобный интерфейс"))
        self.comboBox7.setItemText(2, _translate("MainWindow", "Неадаптированный интерфейс"))
        self.comboBox7.setItemText(3, _translate("MainWindow", "Сложный интерфейс"))
        self.comboBox8.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox8.setItemText(1, _translate("MainWindow", "Нет ненужной информации"))
        self.comboBox8.setItemText(2, _translate("MainWindow", "Небольшое количество "))
        self.comboBox8.setItemText(3, _translate("MainWindow", "Неадаптированная информация"))
        self.comboBox9.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox9.setItemText(1, _translate("MainWindow", "Администрируется"))
        self.comboBox9.setItemText(2, _translate("MainWindow", "Не часто вводится"))
        self.comboBox9.setItemText(3, _translate("MainWindow", "Крайне редко администрируется"))
        self.comboBox10.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox10.setItemText(1, _translate("MainWindow", "Гарантия с полным описанием"))
        self.comboBox10.setItemText(2, _translate("MainWindow", "Не детализированный"))
        self.comboBox10.setItemText(3, _translate("MainWindow", "Без гарантии"))
        self.comboBox11.setItemText(0, _translate("MainWindow", "Выберите"))
        self.comboBox11.setItemText(1, _translate("MainWindow", "Идеально выполненный"))
        self.comboBox11.setItemText(2, _translate("MainWindow", "Приемлемый"))
        self.comboBox11.setItemText(3, _translate("MainWindow", "Неприемлемо"))
        self.label_result.setText(_translate("MainWindow", "Результат Вычисления"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCut_2.setText(_translate("MainWindow", "Cut"))
        self.actionCut_2.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionReplace.setText(_translate("MainWindow", "Replace"))
        self.actionReplace.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


#! pyuic5 -x evaluator.ui -o evaluator.py