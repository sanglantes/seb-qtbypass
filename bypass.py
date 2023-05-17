from PyQt6.QtWidgets import *
from BypassMenu import Ui_BypassMenu
import json
import pyperclip
import requests
from PyQt6.QtCore import QThread, pyqtSignal

class BypassWorkerThread(QThread):
    response_received = pyqtSignal(str)

    def __init__(self, url, header, payload):
        super().__init__()
        self.url = url
        self.header = header
        self.payload = payload
        self.run_flag = True

    def run(self):
        while self.run_flag:
            command = pyperclip.waitForNewPaste()
            if command.startswith("/c"):
                prompt = command[3:]

                response = requests.post(self.url, json=self.payload, headers=self.header)
                data = json.loads(response.text)
                content = data['choices'][0]['message']['content']

                print(data)
                print(f"prompt: {prompt}\nreply: {content}")
                pyperclip.copy(content)

                self.response_received.emit(content)

    def stop(self):
        self.run_flag = False

class Bypass(QDialog):
    def __init__(self, parent=None, url="", header=None, payload=None):
        super().__init__(parent)
        
        self.ui = Ui_BypassMenu()
        self.ui.setupUi(self)
        self.url = url
        self.header = header
        self.payload = payload

        self.worker_thread = BypassWorkerThread(url, header, payload)
        self.worker_thread.response_received.connect(self.handle_response)

        self.ui.start_button.clicked.connect(self.start)
        self.ui.stop_button.clicked.connect(self.stop)

        self.show()

    def handle_response(self, response):
        # Handle the received response here
        pass

    def start(self):
        print("URL:", self.url)
        print("Header:", self.header)
        print("Payload:", self.payload)
        self.ui.label_2.setText("active")

        self.worker_thread.start()

    def stop(self):
        self.worker_thread.stop()
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.terminate()
        self.worker_thread.wait()
        self.ui.label_2.setText("inactive")

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Bypass()
    sys.exit(app.exec())
