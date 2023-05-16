from PyQt6.QtWidgets import *
from ApiConfig import Ui_ApiConfig

def verify_api_key(api_key):
    if len(api_key) != 50:
        return "ERROR: Invalid API key"

class APIConfig(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ApiConfig()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = APIConfig()
    sys.exit(app.exec())
