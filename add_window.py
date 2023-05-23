from PyQt6 import QtCore, QtGui, QtWidgets
from lego_set import LegoSet
from info_dialog import InfoDialog
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QFont

class Ui_add_window(object):

    def __init__(self, database, calculator):
        self.database = database
        self.calculator = calculator

        # po kliknutí na tlačítko "přidat položku" se spustí nasledující blok kódu
    def pridat_polozku_clicked(self):
        cislo_setu = self.lineEdit.text()
        nazev_setu = self.lineEdit_2.text()
        pocet_kusu = self.lineEdit_3.text()
        datum_nakupu = self.lineEdit_4.text()
        porizovaci_cena = self.lineEdit_5.text()
        url = self.lineEdit_6.text()

        lego_set = LegoSet(cislo_setu, nazev_setu, pocet_kusu, datum_nakupu, porizovaci_cena, url) #vytvoří novou instanci legosetu


        self.database.insert_lego_set(lego_set) #uloží instanci legosetu do databáze

        self.clear_form() #vymaže z formulář pro nové zadání

        # Vytvoření instance QMessageBox
        info_dialog = InfoDialog()
        # Zobrazení dialogového okna a čekání na uživatelskou interakci
        info_dialog.exec()

    # funkce pro vyčištění formuláře
    def clear_form(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()

    def setupUi(self, add_window):
        add_window.setObjectName("add_window")
        add_window.resize(1125, 555)
        add_window.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        add_window.setStyleSheet("QDialog {\n"
"    background-color: #343640;\n"
"}")

        # tlačítko pro přidání položky
        self.pridat_polozku = QtWidgets.QPushButton(parent=add_window)
        self.pridat_polozku.setGeometry(QtCore.QRect(740, 420, 151, 51))
        self.pridat_polozku.setStyleSheet("QPushButton {\n"
                "    background-color: #25e317;\n"
                "    font-size: 15px;\n"
                "    border-radius: 12px;\n"
                "}")

        # přiřazení metody k tlačítku
        self.pridat_polozku.clicked.connect(self.pridat_polozku_clicked)

        self.pridat_polozku.setObjectName("pridat_polozku")
        self.lineEdit = QtWidgets.QLineEdit(parent=add_window)
        self.lineEdit.setGeometry(QtCore.QRect(50, 170, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=add_window)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 260, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=add_window)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 350, 311, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=add_window)
        self.lineEdit_4.setGeometry(QtCore.QRect(580, 170, 311, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=add_window)
        self.lineEdit_5.setGeometry(QtCore.QRect(580, 260, 311, 41))
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=add_window)
        self.lineEdit_6.setGeometry(QtCore.QRect(580, 350, 311, 41))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textBrowser = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser.setGeometry(QtCore.QRect(50, 20, 461, 51))
        self.textBrowser.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"}")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 80, 311, 41))
        self.textBrowser_2.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #25e317;\n"
"}")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 140, 311, 31))
        self.textBrowser_3.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_4.setGeometry(QtCore.QRect(50, 230, 311, 31))
        self.textBrowser_4.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_5.setGeometry(QtCore.QRect(50, 320, 311, 31))
        self.textBrowser_5.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_6.setGeometry(QtCore.QRect(580, 140, 311, 31))
        self.textBrowser_6.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_7.setGeometry(QtCore.QRect(580, 230, 311, 31))
        self.textBrowser_7.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_8.setGeometry(QtCore.QRect(580, 320, 311, 31))
        self.textBrowser_8.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_8.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=add_window)
        self.textBrowser_9.setGeometry(QtCore.QRect(940, 470, 171, 61))
        self.textBrowser_9.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_9.setObjectName("textBrowser_9")

        self.retranslateUi(add_window)
        QtCore.QMetaObject.connectSlotsByName(add_window)

    def retranslateUi(self, add_window):
        _translate = QtCore.QCoreApplication.translate
        add_window.setWindowTitle(_translate("add_window", "LegoMakesMoney"))
        self.pridat_polozku.setText(_translate("add_window", "Přidat položku"))
        self.textBrowser.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">LegoMakesMoney</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Přidat novou položku:</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Číslo setu: </span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Název setu:</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Počet kusů: </span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'sans-serif\'; font-size:10pt;\">Datum nákupu:</span><span style=\" font-size:9pt;\"> </span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Pořizovací cena (za 1ks): </span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Vložit odkaz: </span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("add_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Created by Jiří Mareček</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">BearCock Technology 2023</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_window = QtWidgets.QDialog()
    ui = Ui_add_window()
    ui.setupUi(add_window)
    add_window.show()
    sys.exit(app.exec())
