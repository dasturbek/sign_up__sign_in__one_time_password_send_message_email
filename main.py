from PyQt5 import QtWidgets
import sys
from my_py_code.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()