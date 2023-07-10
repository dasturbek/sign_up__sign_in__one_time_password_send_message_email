from PyQt5.QtWidgets import *


def show_internet_messagebox():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)

    # setting message for Message Box
    msg.setText("No Internet")

    # setting Message box window title
    msg.setWindowTitle("Internet")

    # declaring buttons on Message Box
    msg.setStandardButtons(QMessageBox.Ok)

    msg.exec_()
