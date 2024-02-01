from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import uic
import sys

import platform
import psutil
import GPUtil

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI
        uic.loadUi("specs.ui", self)

        # Define our widgets
        self.cpu_label = self.findChild(QLabel, "label")
        self.storage_label = self.findChild(QLabel, "label_2")
        self.ram_label = self.findChild(QLabel, "label_3")

        # Do something
        self.cpu_label.setText(f"Operating System: {platform.system()} {platform.release()}")
        self.storage_label.setText(f"Storage: {round(psutil.disk_usage('/').total / (1024**3), 2)} GB")
        self.ram_label.setText(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
        GPUtil.getGPUs()


        # show the app
        self.show()

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
