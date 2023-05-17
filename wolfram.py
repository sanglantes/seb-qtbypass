from PyQt6.QtWidgets import QApplication, QDialog 
from PyQt6.QtCore import QThread, pyqtSignal
from WolframAlpha import Ui_Wfram
import requests

class Wolfram(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Wfram()
        self.ui.setupUi(self)
        
        self.setFixedSize(451, 292)
    
        self.ui.connect_button.clicked.connect(self.start_w_verification)
        self.ui.help_button.clicked.connect(self.open_help)

        self.worker_thread = WorkerThread()
        self.worker_thread.response_received.connect(self.handle_response)

        self.show()

    def start_w_verification(self):
        w_api_key = self.ui.w_apikey.text().strip()
        self.ui.w_connection.append("INFO: Verifying key... (this uses a prompt)")
        self.worker_thread.set_api_key(w_api_key)
        self.worker_thread.start()

    def handle_response(self, response):
        if response.status_code != 200:
            self.ui.w_connection.append(f"ERROR: Received response status {response.status_code}")
            if response:
                self.ui.w_connection.append(f"INFO: {response} (try a mirror)")
        else:
            self.ui.w_connection.append("INFO: Successfully verified key")

    def open_help(self):
        pass

class WorkerThread(QThread):
    response_received = pyqtSignal(requests.Response)

    def __init__(self):
        super().__init__()
        self.api_key = ""
        self.url = ""

    def set_api_key(self, api_key):
        self.api_key = api_key
        self.url = f"https://api.wolframalpha.com/v1/simple?i=2+plus+2%3F&appid={self.api_key}"
        print(self.api_key)

    def run(self):
        response = requests.post(self.url)
        print(response, self.api_key, self.url)
        self.response_received.emit(response)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Wolfram()
    sys.exit(app.exec())
