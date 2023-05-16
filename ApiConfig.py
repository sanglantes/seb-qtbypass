# Form implementation generated from reading ui file 'ApiConfig.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ApiConfig(object):
    def setupUi(self, ApiConfig):
        ApiConfig.setObjectName("ApiConfig")
        ApiConfig.resize(413, 300)
        self.label = QtWidgets.QLabel(parent=ApiConfig)
        self.label.setGeometry(QtCore.QRect(30, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=ApiConfig)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.register_button = QtWidgets.QPushButton(parent=ApiConfig)
        self.register_button.setGeometry(QtCore.QRect(230, 250, 161, 41))
        self.register_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.register_button.setObjectName("register_button")
        self.submit_button = QtWidgets.QPushButton(parent=ApiConfig)
        self.submit_button.setGeometry(QtCore.QRect(130, 250, 91, 41))
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.submit_button.setObjectName("submit_button")
        self.lineEdit = QtWidgets.QLineEdit(parent=ApiConfig)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 251, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=ApiConfig)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 50, 251, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=ApiConfig)
        self.textBrowser.setGeometry(QtCore.QRect(20, 120, 371, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(parent=ApiConfig)
        self.label_3.setGeometry(QtCore.QRect(70, 41, 16, 10))
        self.label_3.setObjectName("label_3")
        self.mirror_box = QtWidgets.QComboBox(parent=ApiConfig)
        self.mirror_box.setGeometry(QtCore.QRect(257, 90, 131, 22))
        self.mirror_box.setObjectName("mirror_box")
        self.mirror_box.addItem("")
        self.mirror_box.addItem("")
        self.mirror_box.addItem("")

        self.retranslateUi(ApiConfig)
        self.lineEdit_2.returnPressed.connect(self.submit_button.click) # type: ignore
        self.lineEdit.returnPressed.connect(self.submit_button.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ApiConfig)

    def retranslateUi(self, ApiConfig):
        _translate = QtCore.QCoreApplication.translate
        ApiConfig.setWindowTitle(_translate("ApiConfig", "API Setup"))
        self.label.setText(_translate("ApiConfig", "ChatGPT API key"))
        self.label_2.setText(_translate("ApiConfig", "RapidAPI key"))
        self.register_button.setText(_translate("ApiConfig", "Register RapidAPI key"))
        self.submit_button.setText(_translate("ApiConfig", "Submit"))
        self.textBrowser.setHtml(_translate("ApiConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:12pt;\">Connection details:</span></p></body></html>"))
        self.label_3.setText(_translate("ApiConfig", "or"))
        self.mirror_box.setItemText(0, _translate("ApiConfig", "RapidAPI main"))
        self.mirror_box.setItemText(1, _translate("ApiConfig", "RapidAPI mirror (1)"))
        self.mirror_box.setItemText(2, _translate("ApiConfig", "RapidAPI mirror (2)"))
