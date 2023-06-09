from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainWindow import Ui_MainWindow
from api import APIConfig

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.api_widget = None
        self.ui.pushButton.clicked.connect(self.gpt_api)
        self.ui.config_wfram.clicked.connect(self.in_progress)

        self.show()

    def gpt_api(self):
	    if self.api_widget is None or not self.api_widget.isVisible():
	        self.api_widget = APIConfig(self)
	        self.api_widget.show()
	    else:
	        self.api_widget.raise_()
	        self.api_widget.activateWindow()

    def in_progress(self):
        message = "This feature is not available yet."
        QMessageBox.information(self, "WolframAlpha API", message)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
