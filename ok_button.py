from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(312, 127)
        Dialog.setStyleSheet("QDialog {\n"
                             "    background-color: #343640;\n"
                             "}")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 40, 121, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                       "    background-color:#25e317;\n"
                                       "    font-size: 15px;\n"
                                       "    border-radius: 12px;\n"
                                       "}")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(Dialog.close)

        # Přidání události stisknutí klávesy Enter
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.clicked.connect(Dialog.accept)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Data uložena - stiskněte Enter"))
        self.pushButton.setText(_translate("Dialog", "Data uložena"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())