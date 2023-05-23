from PyQt6 import QtCore, QtGui, QtWidgets
import re
from info_dialog import InfoDialog

class Ui_edit_window(object):

    def __init__(self, database, edit_window):
        self.database = database
        self.edit_window = edit_window

    # vytvoří instanci info_dialog a po potvrzení se zavřespolu s editačním oknem
    def show_info_dialog(self):
        info_dialog = InfoDialog()
        info_dialog.exec()

        # Zavření dialogového okna a editačního okna
        if info_dialog.close():
                # Zavření editačního okna
                self.edit_window.close()

    def save_edit_item_clicked(self):
        cislo_setu = self.lineEdit.text()
        nazev_setu = self.lineEdit_2.text()
        pocet_kusu = self.lineEdit_3.text()
        datum_nakupu = self.lineEdit_4.text()
        porizovaci_cena = self.lineEdit_5.text()
        url = self.lineEdit_6.text()

        # vrací textový obsah widgetu jako obyčejný řetězec (string).
        id_from_text = self.textBrowser_2.toPlainText()
        # louží k extrakci číselného identifikátoru (ID) z řetězce id_from_text.
        id = re.findall(r'\d+', id_from_text)[0]

        # Aktualizace záznamu v databázi
        self.database.update_all_data(cislo_setu, nazev_setu, pocet_kusu, datum_nakupu, porizovaci_cena, url, id)
        self.database.connection.commit()

        # zavolá info dialog
        self.show_info_dialog()


    def setupUi(self, edit_window):
        edit_window.setObjectName("edit_window")
        edit_window.resize(1125, 555)
        edit_window.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        edit_window.setStyleSheet("QDialog {\n"
"    background-color: #343640;\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(parent=edit_window)
        self.lineEdit.setGeometry(QtCore.QRect(50, 170, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setAccessibleDescription("")
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
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=edit_window)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 260, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setWhatsThis("")
        self.lineEdit_2.setAccessibleName("")
        self.lineEdit_2.setAccessibleDescription("")
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=edit_window)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 350, 311, 41))
        self.lineEdit_3.setWhatsThis("")
        self.lineEdit_3.setAccessibleName("")
        self.lineEdit_3.setAccessibleDescription("")
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=edit_window)
        self.lineEdit_4.setGeometry(QtCore.QRect(580, 170, 311, 41))
        self.lineEdit_4.setWhatsThis("")
        self.lineEdit_4.setAccessibleName("")
        self.lineEdit_4.setAccessibleDescription("")
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=edit_window)
        self.lineEdit_5.setGeometry(QtCore.QRect(580, 260, 311, 41))
        self.lineEdit_5.setWhatsThis("")
        self.lineEdit_5.setAccessibleName("")
        self.lineEdit_5.setAccessibleDescription("")
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=edit_window)
        self.lineEdit_6.setGeometry(QtCore.QRect(580, 350, 311, 41))
        self.lineEdit_6.setWhatsThis("")
        self.lineEdit_6.setAccessibleName("")
        self.lineEdit_6.setAccessibleDescription("")
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    background-color: #444654;\n"
"    color: #cdcdd3;\n"
"    font-size: 14px;\n"
"    padding-left: 8px;\n"
"}")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textBrowser = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser.setGeometry(QtCore.QRect(50, 20, 461, 51))
        self.textBrowser.setWhatsThis("")
        self.textBrowser.setAccessibleName("")
        self.textBrowser.setAccessibleDescription("")
        self.textBrowser.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"}")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 80, 311, 41))
        self.textBrowser_2.setWhatsThis("")
        self.textBrowser_2.setAccessibleName("")
        self.textBrowser_2.setAccessibleDescription("")
        self.textBrowser_2.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #ff9817;\n"
"    font-size: 15pt;\n" 
"}")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 140, 311, 31))
        self.textBrowser_3.setWhatsThis("")
        self.textBrowser_3.setAccessibleName("")
        self.textBrowser_3.setAccessibleDescription("")
        self.textBrowser_3.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_4.setGeometry(QtCore.QRect(50, 230, 311, 31))
        self.textBrowser_4.setWhatsThis("")
        self.textBrowser_4.setAccessibleName("")
        self.textBrowser_4.setAccessibleDescription("")
        self.textBrowser_4.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_5.setGeometry(QtCore.QRect(50, 320, 311, 31))
        self.textBrowser_5.setWhatsThis("")
        self.textBrowser_5.setAccessibleName("")
        self.textBrowser_5.setAccessibleDescription("")
        self.textBrowser_5.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_6.setGeometry(QtCore.QRect(580, 140, 311, 31))
        self.textBrowser_6.setWhatsThis("")
        self.textBrowser_6.setAccessibleName("")
        self.textBrowser_6.setAccessibleDescription("")
        self.textBrowser_6.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_7.setGeometry(QtCore.QRect(580, 230, 311, 31))
        self.textBrowser_7.setWhatsThis("")
        self.textBrowser_7.setAccessibleName("")
        self.textBrowser_7.setAccessibleDescription("")
        self.textBrowser_7.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_8.setGeometry(QtCore.QRect(580, 320, 311, 31))
        self.textBrowser_8.setWhatsThis("")
        self.textBrowser_8.setAccessibleName("")
        self.textBrowser_8.setAccessibleDescription("")
        self.textBrowser_8.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        self.textBrowser_8.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=edit_window)
        self.textBrowser_9.setGeometry(QtCore.QRect(940, 470, 171, 61))
        self.textBrowser_9.setWhatsThis("")
        self.textBrowser_9.setAccessibleName("")
        self.textBrowser_9.setAccessibleDescription("")
        self.textBrowser_9.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")


        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.ulozit = QtWidgets.QPushButton(parent=edit_window)
        self.ulozit.setGeometry(QtCore.QRect(740, 420, 151, 51))
        self.ulozit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ulozit.setWhatsThis("")
        self.ulozit.setAccessibleName("")
        self.ulozit.setAccessibleDescription("")
        self.ulozit.setStyleSheet("QPushButton {\n"
"    background-color:  #ff9817;\n"
"    font-size: 15px;\n"
"    border-radius: 12px;\n"
"}")
        self.ulozit.setText("Uložit")
        self.ulozit.setObjectName("ulozit")

        # přiřazení metody k tlačítku - po kliknutí na tlačítko se data uloží
        self.ulozit.clicked.connect(self.save_edit_item_clicked)

        self.retranslateUi(edit_window)
        QtCore.QMetaObject.connectSlotsByName(edit_window)


    def retranslateUi(self, edit_window):
        _translate = QtCore.QCoreApplication.translate
        edit_window.setWindowTitle(_translate("edit_window", "LegoMakesMoney"))
        self.textBrowser.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">LegoMakesMoney</span></p></body></html>"))

        self.textBrowser_3.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Číslo setu: </span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Název setu:</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Počet kusů: </span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'sans-serif\'; font-size:10pt;\">Datum nákupu:</span><span style=\" font-size:9pt;\"> </span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Pořizovací cena (za 1ks): </span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Upravit odkaz:</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("edit_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
    edit_window = QtWidgets.QDialog()
    ui = Ui_edit_window()
    ui.setupUi(edit_window)
    edit_window.show()
    sys.exit(app.exec())
