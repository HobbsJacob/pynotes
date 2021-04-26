# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expanded.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 907)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.taskLayout = QtWidgets.QWidget(self.splitter)
        self.taskLayout.setAutoFillBackground(True)
        self.taskLayout.setObjectName("taskLayout")
        self.seriesPaneLayout = QtWidgets.QVBoxLayout(self.taskLayout)
        self.seriesPaneLayout.setContentsMargins(0, 0, 0, 0)
        self.seriesPaneLayout.setSpacing(0)
        self.seriesPaneLayout.setObjectName("seriesPaneLayout")
        self.dailyList = QtWidgets.QListWidget(self.taskLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dailyList.sizePolicy().hasHeightForWidth())
        self.dailyList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dailyList.setFont(font)
        self.dailyList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dailyList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dailyList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.dailyList.setProperty("isWrapping", False)
        self.dailyList.setResizeMode(QtWidgets.QListView.Fixed)
        self.dailyList.setWordWrap(True)
        self.dailyList.setObjectName("dailyList")
        self.seriesPaneLayout.addWidget(self.dailyList)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.seriesPaneLayout.addItem(spacerItem)
        self.projectList = QtWidgets.QListWidget(self.taskLayout)
        self.projectList.setObjectName("projectList")
        self.seriesPaneLayout.addWidget(self.projectList)
        self.textLayout = QtWidgets.QWidget(self.splitter)
        self.textLayout.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLayout.sizePolicy().hasHeightForWidth())
        self.textLayout.setSizePolicy(sizePolicy)
        self.textLayout.setObjectName("textLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.textLayout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QPlainTextEdit(self.textLayout)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionRemove_Credits = QtWidgets.QAction(MainWindow)
        self.actionRemove_Credits.setObjectName("actionRemove_Credits")
        self.action2x = QtWidgets.QAction(MainWindow)
        self.action2x.setObjectName("action2x")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "None"))
        self.actionUpdate.setText(_translate("MainWindow", "Update All"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSettings.setText(_translate("MainWindow", "Settings..."))
        self.actionRemove_Credits.setText(_translate("MainWindow", "Remove Credits"))
        self.action2x.setText(_translate("MainWindow", "2x"))
