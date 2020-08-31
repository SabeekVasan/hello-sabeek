import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from View.mainwindow import Ui_MainWindow
from pip._internal import self_outdated_check


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()    
    window.show()
    sys.exit(app.exec_())
