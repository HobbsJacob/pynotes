from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import sys

from expanded_layout import Ui_MainWindow

junk_path = "C:\\Users\\Jacob\\Desktop\\junk"

class Label(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setMargin(0)

    def enterEvent(self, event):
        window.expand_ui()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.l = Label(self)
        self.l.setAlignment(Qt.AlignTop)
        self.statusBar().setSizeGripEnabled(False)
        self.setWindowOpacity(1)

        self.daily_list = []
        self.project_list = []

        with open("corner.png", "rb") as file:
            map = QPixmap()
            map.loadFromData(file.read())
            self.l.setPixmap(map)

    def leaveEvent(self, event):
        self.hide_ui()

    def double_clicked(self):
        try:
            for item in self.ui.dailyList.selectedItems():
                self.ui.dailyList.takeItem(self.ui.dailyList.row(item))
                self.daily_list.remove(item.text())
        except:
            print(sys.exc_info())

    def proj_clicked(self):
        try:
            self.resize(800,800)
            self.ui.splitter.setSizes([300,500])
            opened = self.ui.projectList.selectedItems()[0].text()
            with open(os.path.join(junk_path, "(P) " + opened, opened + ".txt"), "r") as file:
                self.ui.textEdit.setPlainText(file.read())
        except:
            print(sys.exc_info())

    def text_changed(self):
        opened = self.ui.projectList.selectedItems()[0].text()
        with open(os.path.join(junk_path, "(P) " + opened, opened + ".txt"), "w") as file:
            file.write(self.ui.textEdit.toPlainText())

    def expand_ui(self):
        print("expand")
        self.statusBar().setSizeGripEnabled(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        self.ui.splitter.setSizes([100, 0])
        self.resize(300, 800)

        for task in self.daily_list:
            self.ui.dailyList.addItem(task)
        for task in self.project_list:
            self.ui.projectList.addItem(task)

        window.ui.dailyList.doubleClicked.connect(self.double_clicked)
        window.ui.projectList.clicked.connect(self.proj_clicked)
        window.ui.textEdit.textChanged.connect(self.text_changed)


    def hide_ui(self):
        try:
            print("hide")
            for i in self.ui.centralWidget.children():
                i.deleteLater()
            self.resize(50, 50)
            self.ui.centralWidget.deleteLater()
        except:
            print(sys.exc_info())

        self.l = Label(self)
        self.l.setAlignment(Qt.AlignTop)
        self.statusBar().setSizeGripEnabled(False)

def read_files():
    with open(os.path.join(junk_path, "DAILY.txt"), "r") as file:
        for line in file:
            window.daily_list.append(line.replace("\n", ""))
    for dire in os.listdir(junk_path):
        if "(P)" in dire:
            window.project_list.append(dire.replace("(P) ", ""))





app = QApplication(sys.argv)
window = MainWindow()

read_files()

window.setMinimumSize(10, 10)

window.resize(100, 100)
window.move(0,0)

window.show()
sys.exit(app.exec_())
