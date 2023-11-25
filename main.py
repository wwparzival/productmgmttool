# Standard classes / libraries
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream

# Custom classes / libraries
from classes.Controller import Controller

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))

    app = QApplication(sys.argv)
    
    # set stylesheet
    file = QFile(dir_path + "/styles/Ubuntu.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    controller = Controller(dir_path)
    sys.exit(app.exec_())