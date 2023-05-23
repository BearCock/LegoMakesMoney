from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 146)
        Dialog.setStyleSheet("background-color: #343640;")

        self.odstranit_polozku = QtWidgets.QPushButton(parent=Dialog)
        self.odstranit_polozku.setGeometry(QtCore.QRect(20, 80, 161, 41))
        self.odstranit_polozku.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.odstranit_polozku.setWhatsThis("")
        self.odstranit_polozku.setStyleSheet("QPushButton {\n"
"    background-color: #e31717;\n"
"    font-size: 14px;\n"
"    border-radius: 12px;\n"
"}")


        self.odstranit_polozku.setObjectName("odstranit_polozku")
        self.ponechat_polozku = QtWidgets.QPushButton(parent=Dialog)
        self.ponechat_polozku.setGeometry(QtCore.QRect(210, 80, 161, 41))
        self.ponechat_polozku.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ponechat_polozku.setWhatsThis("")
        self.ponechat_polozku.setStyleSheet("QPushButton {\n"
"    background-color:#25e317;\n"
"    font-size: 14px;\n"
"    border-radius: 12px;\n"
"}")
        self.ponechat_polozku.setObjectName("ponechat_polozku")
        self.textBrowser_1 = QtWidgets.QTextBrowser(parent=Dialog)
        self.textBrowser_1.setGeometry(QtCore.QRect(20, 20, 341, 41))
        self.textBrowser_1.setWhatsThis("")
        self.textBrowser_1.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_1.setObjectName("textBrowser_1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", ""))
        self.odstranit_polozku.setText(_translate("Dialog", "Odstranit položku"))
        self.ponechat_polozku.setText(_translate("Dialog", "Ponechat položku"))
        self.textBrowser_1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11.6pt;\">Opravdu si přejete odstranit označenou položku?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
