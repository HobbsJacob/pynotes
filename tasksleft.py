#Maybe put in a template. e.g. you make a new task and it automatically fills the note with
#Done when
#Due complete
#Jira link?
#e.t.c.



from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import shutil
import sys
import glob

from expanded_layout import Ui_MainWindow

JUNK_PATH = "C:\\Users\\jacobh\\Desktop\\Notes"

with open("C:\\Users\\jacobh\\pynotes-master\\error.txt", "w") as file:
    file.write("OK")


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
        self.lowest_project = 999

        self.project_list = []

        with open("corner.png", "rb") as file:
            map = QPixmap()
            map.loadFromData(file.read())
            self.l.setPixmap(map)

    def leaveEvent(self, event):
        self.hide_ui()

#    def double_clicked(self):
#        try:
#            for item in self.ui.dailyList.selectedItems():
#                self.ui.dailyList.takeItem(self.ui.dailyList.row(item))
#                self.daily_list.remove(item.text())
#        except:
#            print(sys.exc_info())

    def proj_clicked(self):
        try:
            self.resize(800,800)
            self.ui.splitter.setSizes([300,500])
            opened = self.ui.projectList.selectedItems()[0].text()
            g = glob.glob(os.path.join(JUNK_PATH, "*(P) " + opened))
            with open(os.path.join(g[0], opened + ".txt"), "r") as file:
                self.ui.textEdit.setPlainText(file.read())
        except:
            print(sys.exc_info())

    def text_changed(self):
        opened = self.ui.projectList.selectedItems()[0].text()
        g = glob.glob(os.path.join(JUNK_PATH, "*(P) " + opened))
        with open(os.path.join(g[0], opened + ".txt"), "w") as file:
            file.write(self.ui.textEdit.toPlainText())

    def expand_ui(self):
        print("expand")
        self.statusBar().setSizeGripEnabled(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        self.ui.splitter.setSizes([100, 0])
        self.resize(300, 800)

        for task in self.project_list:
            self.ui.projectList.addItem(task)

        #window.ui.dailyList.doubleClicked.connect(self.double_clicked)
        window.ui.projectList.clicked.connect(self.proj_clicked)
        window.ui.textEdit.textChanged.connect(self.text_changed)
        window.ui.newButton.clicked.connect(self.add_proj)
        window.ui.deleteButton.clicked.connect(self.delete_proj)

    def add_proj(self):
        t, ok = QInputDialog.getText(self, "Project Name", "")
        if ok:
            self.lowest_project -= 1
            os.mkdir(JUNK_PATH + "\\" + str(self.lowest_project) + "(P) " + t)
            self.project_list.insert(0, t)

    def delete_proj(self):
        try:
            opened = self.ui.projectList.selectedItems()[0].text()
            g = glob.glob(os.path.join(JUNK_PATH, "*(P) " + opened))
            print(g[0])
            shutil.rmtree(g[0])
            self.project_list.remove(opened)
        except:
            print(sys.exc_info())


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
    for dire in os.listdir(JUNK_PATH):
        if "(P)" in dire:
            split = dire.split("(P) ")
            window.project_list.append(split[1])

            project_number = int(split[0])
            if project_number < window.lowest_project:
                window.lowest_project = project_number


try:


    app = QApplication(sys.argv)
    window = MainWindow()

    read_files()

    window.setMinimumSize(10, 10)

    window.resize(100, 100)
    window.move(0,0)

    window.show()
    sys.exit(app.exec_())

except Exception as e:
    with open("C:\\Users\\jacobh\\pynotes-master\\error.txt", "w") as file:
        file.write(e)

input("OK?")
