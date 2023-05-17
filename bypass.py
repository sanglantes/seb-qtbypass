from PyQt6.QtWidgets import *
from BypassMenu import Ui_BypassMenu
import json
import pyperclip
import requests
from PyQt6.QtCore import QThread, pyqtSignal

class Bypass(QDialog):
    def __init__(self, url, payload, header):
        super().__init__()
        
        self.ui = Ui_BypassMenu()
        self.ui.setupUi(self)

        self.run = False

        self.url = url
        self.payload = payload
        self.header = header

        self.ui.start_button.clicked.connect(self.start)
        self.ui.stop_button.clicked.connect(self.stop)

        self.show()

    def start(self):
        self.run = True
        self.run_bypass()
        self.ui.label_2.setText("active")

    def stop(self):
        self.run = False
        self.ui.label_2.setText("inactive")

    def run_bypass(self):
        while (self.run):
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

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Bypass()
    sys.exit(app.exec())
