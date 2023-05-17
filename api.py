from PyQt6.QtWidgets import *
from ApiConfig import Ui_ApiConfig
from PyQt6.QtCore import QThread, pyqtSignal
from register import Register
from bypass import Bypass
import requests

class APIConfig(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ApiConfig()
        self.ui.setupUi(self)
        self.setFixedSize(413, 300)

        self.ui.submit_button.clicked.connect(self.start_verification)
        self.ui.register_button.clicked.connect(self.open_website)

        self.ui.mirror_box.currentIndexChanged.connect(self.handle_combo_box)
        self.register_widget = None
        self.bypass_window = None

        # Does there exist a better solution? Yes.
        self.url = ""
        self.header = {}
        self.payload = {}
        self.api_key = ""
        self.handle_combo_box(0)

        self.worker_thread = WorkerThread()
        self.worker_thread.response_received.connect(self.handle_response)

        self.show()

    def handle_combo_box(self, index):
        urls = {
            0: "https://openai80.p.rapidapi.com/chat/completions",
            1: "https://chatgpt53.p.rapidapi.com/",
        }
        payloads = {
        # OFFICIAL CHATGPT
            0: {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello."
                    }
                ]
            },

        # CHATGPT FORK
            1: {
                "messages": [
                    {
                        "role": "user",
                        "content": "Hello."
                    }
                ]
            },
        }
        headers = {
            0: {
                "content-type": "application/json",
                "X-RapidAPI-Key": self.ui.lineEdit_2.text().strip(),
                "X-RapidAPI-Host": "openai80.p.rapidapi.com"
            },
            1: {
                "content-type": "application/json",
                "X-RapidAPI-Key": self.ui.lineEdit_2.text().strip(),
                "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
            },
        }
        self.url = urls[index]
        self.payload = payloads[index]
        self.header = headers[index]

    def open_website(self):
        if self.register_widget is None or not self.register_widget.isVisible():
            self.register_widget = Register(self)
            self.register_widget.show()
        else:
            self.register_widget.raise_()
            self.register_widget.activateWindow()

    def start_verification(self):
        self.api_key = self.ui.lineEdit_2.text().strip()
        self.handle_combo_box(self.ui.mirror_box.currentIndex())
        self.ui.textBrowser.append("INFO: Verifying key... (this uses a prompt)")

        self.worker_thread.set_api_key(self.api_key)
        self.worker_thread.set_variables(self.url, self.payload, self.header)  # Pass variables to WorkerThread
        self.worker_thread.start()

    def handle_response(self, response):
        if response.status_code != 200:
            self.ui.textBrowser.append(f"ERROR: Received response status {response.status_code}")
            message = response.json().get('message')
            if message:
                self.ui.textBrowser.append(f"INFO: {message} (try a mirror)")
        else:
            self.ui.textBrowser.append("INFO: Successfully verified key")
            if self.bypass_window is None:
                self.bypass_window = Bypass(self.url, self.payload, self.header)
            else:
                self.bypass_window.update_data(self.url, self.payload, self.header)

            self.bypass_window.show()
    def show_api_config(self):
        self.show()

class WorkerThread(QThread):
    response_received = pyqtSignal(requests.Response)

    def __init__(self):
        super().__init__()
        self.api_key = ""
        self.url = ""
        self.payload = ""
        self.headers = ""

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_variables(self, url, payload, headers):
        self.url = url
        self.payload = payload
        self.headers = headers

    def run(self):
        response = requests.post(self.url, json=self.payload, headers=self.headers)
        self.response_received.emit(response)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = APIConfig()
    sys.exit(app.exec())