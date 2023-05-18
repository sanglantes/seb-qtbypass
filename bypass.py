from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal
from BypassMenu import Ui_BypassMenu
import json
import pyperclip
import requests

class Bypass(QDialog):
    def __init__(self, url, payload, header):
        super().__init__()

        self.ui = Ui_BypassMenu()
        self.ui.setupUi(self)

        self.url = url
        self.payload = payload
        self.header = header

        self.thread = BypassThread(self.url, self.payload, self.header)

        self.ui.start_button.clicked.connect(self.start)
        self.ui.stop_button.clicked.connect(self.stop)

        self.thread.finished.connect(self.on_thread_finished)

        self.show()

    def start(self):
        self.thread.start()
        self.ui.label_2.setText("active")

    def stop(self):
        self.ui.label_2.setText("stopping...")
        self.thread.stop_thread()  # Signal the thread to stop

    def on_thread_finished(self):
        self.ui.label_2.setText("inactive")
        pyperclip.copy('')

class BypassThread(QThread):
    finished = pyqtSignal()  

    def __init__(self, url, payload, header):
        super().__init__()
        self.url = url
        self.payload = payload
        self.header = header
        self._stop_flag = False

    def run(self):
        while not self._stop_flag:
            command = pyperclip.waitForNewPaste()
            if command.startswith("/c"):
                prompt = command[3:]
                self.payload['messages'][0]['content'] = prompt

                response = requests.post(self.url, json=self.payload, headers=self.header)
                data = json.loads(response.text)
                content = data['choices'][0]['message']['content']

                print(data)
                print(f"prompt: {prompt}\nreply: {content}")
                pyperclip.copy(content)

        self.finished.emit() 

    def stop_thread(self):
        self._stop_flag = True
        pyperclip.copy("/c Stopping... (reply with one word)")

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Bypass()
    sys.exit(app.exec())
