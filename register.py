from PyQt6.QtWidgets import *
from RegisterDialog import Ui_Dialog
from PyQt6.QtCore import QThread, pyqtSignal

class Register(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
	import sys

	app = QApplication(sys.argv)
	window = Register()
	sys.exit(app.exec())