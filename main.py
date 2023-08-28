# Standard classes / libraries
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream

# Custom classes / libraries
from classes.Controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # set stylesheet
    file = QFile("styles/Ubuntu.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    controller = Controller()
    sys.exit(app.exec_())
