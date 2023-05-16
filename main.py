from PyQt6.QtWidgets import *
from ApiConfig import Ui_ApiConfig
from PyQt6.QtCore import QThread, pyqtSignal
import requests
from time import sleep

class APIConfig(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ApiConfig()
        self.ui.setupUi(self)
        self.setFixedSize(413, 300)

        self.ui.submit_button.clicked.connect(self.start_verification)
        self.ui.register_button.clicked.connect(self.open_website)
        self.ui.mirror_box.currentIndexChanged.connect(self.handle_combo_box)

        self.worker_thread = WorkerThread()
        self.worker_thread.response_received.connect(self.handle_response)

        self.show()

    def handle_combo_box(self, index):
        urls = {
            0: "https://chatgpt53.p.rapidapi.com/",
            1: "https://openai80.p.rapidapi.com/chat/completions",
            2: "https://chatgpt-api6.p.rapidapi.com/standard-gpt",
        }
        payloads = {
        # CHATGPT FORK
            0: {
                "messages": [
                    {
                        "role": "user",
                        "content": "Echo."
                    }
                ]
            },
        # OFFICIAL CHATGPT
            1: {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": "Echo."
                    }
                ]
            },
        # CHATGPT FORK
            2: {
                "conversation": [
                    {
                        "role": "user",
                        "content": "Echo."
                    }
                ]
            },
        }
        headers = {
            0: {
                "content-type": "application/json",
                "X-RapidAPI-Key": self.ui.lineEdit_2.text().strip(),
                "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
            },
            1: {
                "content-type": "application/json",
                "X-RapidAPI-Key": self.ui.lineEdit_2.text().strip(),
                "X-RapidAPI-Host": "openai80.p.rapidapi.com"
            },
            2: {
                "content-type": "application/json",
                "X-RapidAPI-Key": self.ui.lineEdit_2.text().strip(),
                "X-RapidAPI-Host": "chatgpt-api6.p.rapidapi.com"
            },
        }
        self.url = urls[index]
        self.payload = payloads[index]
        self.headers = headers[index]

    def open_website(self):
        import webbrowser
        webbrowser.open("https://rapidapi.com/auth/sign-up")

    def start_verification(self):
        lineEdit_focus = self.ui.lineEdit.hasFocus()
        lineEdit_2_focus = self.ui.lineEdit_2.hasFocus()

        if lineEdit_2_focus or not len(self.ui.lineEdit.text().strip()):
            api_key = self.ui.lineEdit_2.text()
            self.ui.textBrowser.append("INFO: Verifying key (this uses a prompt)...")
            self.worker_thread.set_api_key(api_key)
            self.worker_thread.start()

        elif lineEdit_focus or not len(self.ui.lineEdit_2.text().strip()):
            api_key = self.ui.lineEdit.text()
            print(api_key)
        else:
            self.ui.textBrowser.append("ERROR: Multiple forms filled")

    def handle_response(self, response):
        if response.status_code != 200:
            self.ui.textBrowser.append(f"ERROR: Received response status {response.status_code}")
            message = response.json().get('message')
            if message:
                self.ui.textBrowser.append(f"INFO: {message} (try a mirror)")
        else:
            self.ui.textBrowser.append("INFO: Successfully verified key")

class WorkerThread(QThread):
    response_received = pyqtSignal(requests.Response)

    def __init__(self):
        super().__init__()
        self.api_key = ""

    def set_api_key(self, api_key):
        self.api_key = api_key

    def run(self):
        url = "https://chatgpt53.p.rapidapi.com/"
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": "Echo."
                }
            ]
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key.strip(),
            "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
        }
        response = requests.post(url, json=payload, headers=headers)
        self.response_received.emit(response)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = APIConfig()
    sys.exit(app.exec())