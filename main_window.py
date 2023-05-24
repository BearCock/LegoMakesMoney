from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import keyboard
from edit_window import Ui_edit_window
from add_window import Ui_add_window
from remove_item_dialog import RemoveDialog


class Ui_mainWindow(object):
    def __init__(self, database, calculator, finder):
        self.database = database
        self.calculator = calculator
        self.finder = finder

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1125, 555)
        mainWindow.setStyleSheet("QDialog {\n"
            "    background-color: #343640;\n"
            "    color: #9c9ca1;\n"  # barva textu obsahu tabulky
            "}")
        self.tableWidget = QtWidgets.QTableWidget(parent=mainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(50, 90, 851, 371))
        self.tableWidget.setMinimumSize(QtCore.QSize(701, 0))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
            "    background-color: #444654;\n" 
            "    color: #9c9ca1;\n" # barva textu obsahu tabulky
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    background-color: #686a7d;\n"
            "    color: #cdcdd3;\n"
            "}\n"
            "")

        # tabulka
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)

        self.pridat_polozku = QtWidgets.QPushButton(parent=mainWindow)
        self.pridat_polozku.setGeometry(QtCore.QRect(940, 90, 151, 51))
        self.pridat_polozku.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pridat_polozku.setStyleSheet("QPushButton {\n"
            "    background-color:#25e317;\n"
            "    font-size: 15px;\n"
            "    border-radius: 12px;\n"
            "}")


        # blok pro vypsání dat do tabulky
        # vytáhne data z databáze
        data_extraction = self.database.cursor.execute(
            "SELECT id, cislo_setu, nazev_setu, pocet_kusu, datum_nakupu,porizovaci_cena, aktualni_cena, rozdil_cen FROM lego_sets").fetchall()

        # nastaví počet řádků tabulky
        self.tableWidget.setRowCount(len(data_extraction))

        for row_number, row_data in enumerate(data_extraction):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                # zarovná obsah buněk sloupce 1 na levou stranu
                if column_number != 2:
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.tableWidget.setItem(row_number, column_number, item)

        self.tableWidget.verticalHeader().setVisible(False)


        # tlačítko Přidat položku
        self.pridat_polozku.setObjectName("pridat_polozku")
        self.upravit_polozku = QtWidgets.QPushButton(parent=mainWindow)
        self.upravit_polozku.setGeometry(QtCore.QRect(940, 180, 151, 51))
        self.pridat_polozku.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.upravit_polozku.setStyleSheet("QPushButton {\n"
                                           "    background-color: #ff9817;\n"
                                           "    font-size: 15px;\n"
                                           "    border-radius: 12px;\n"
                                           "}")
        # napojení na okno add_window
        self.pridat_polozku.clicked.connect(self.show_add_window)

        # tlačítko Upravit položku
        self.upravit_polozku.setObjectName("upravit_polozku")
        self.odstranit_polozku = QtWidgets.QPushButton(parent=mainWindow)
        self.odstranit_polozku.setGeometry(QtCore.QRect(940, 270, 151, 51))
        self.upravit_polozku.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.odstranit_polozku.setStyleSheet("QPushButton {\n"
                                             "    background-color: #e31717;\n"
                                             "    font-size: 15px;\n"
                                             "    border-radius: 12px;\n"
                                             "}")
        # napojení na okno edit_window
        self.upravit_polozku.clicked.connect(self.show_edit_window)


        # tlačítko Odstranit položku
        self.odstranit_polozku.setObjectName("odstranit_polozku")
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=mainWindow)
        self.textBrowser_9.setGeometry(QtCore.QRect(940, 470, 171, 61))
        self.textBrowser_9.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"    font-size: 14px;\n"
"    padding-left: 0px;\n"
"}")
        # po kliknutí na tlačítko Odstranit položku se zobrazí remove_item_dialog:
        self.odstranit_polozku.clicked.connect(self.show_remove_dialog)

        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser = QtWidgets.QTextBrowser(parent=mainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(50, 20, 461, 51))
        self.textBrowser.setStyleSheet("QTextEdit {\n"
"    background-color: #343640;\n"
"    color: #CDCDD3;\n"
"}")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=mainWindow)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 480, 281, 41))
        self.textBrowser_2.setStyleSheet("QTextBrowser {\n"
            "    background-color: #444654;\n"
            "    color: #cdcdd3;\n"
            "    padding-top: 6px;\n"
            "    font-size: 10pt;\n"
            "    text-align: center;\n"
            "}")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")


        # výpis dat do widgetů
        celkova_cena_portfolia = self.database.cursor.execute("SELECT celkova_cena_portfolia FROM portfolio_data").fetchone()[0]
        self.textBrowser_2.setText(f"Celková cena portfolia: {celkova_cena_portfolia},- Kč")
        # vystředí text horizontálně
        self.textBrowser_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=mainWindow)
        self.textBrowser_3.setGeometry(QtCore.QRect(620, 480, 281, 41))
        self.textBrowser_3.setStyleSheet("QTextBrowser {\n"
            "    background-color: #444654;\n"
            "    color: #cdcdd3;\n"
            "    padding-top: 6px;\n"
            "    font-size: 10pt;\n" 
            "}")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")

        narust_ceny_portfolia = self.database.cursor.execute("SELECT narust_ceny_portfolia FROM portfolio_data").fetchone()[0]
        narust_ceny_portfolia_procenta = self.database.cursor.execute("SELECT narust_ceny_portfolia_procenta FROM portfolio_data").fetchone()[0]
        self.textBrowser_3.setText(f"Nárůst ceny portfolia: {round(narust_ceny_portfolia_procenta, 2)}% = {narust_ceny_portfolia},- Kč")

        # vystředí text horizontálně
        self.textBrowser_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "LegoMakesMoney"))

        item = self.tableWidget.horizontalHeaderItem(0)
        self.tableWidget.setColumnWidth(0, 20)
        item.setText(_translate("mainWindow", "ID"))

        item = self.tableWidget.horizontalHeaderItem(1)
        self.tableWidget.setColumnWidth(1, 70)
        item.setText(_translate("mainWindow", "Číslo setu"))

        item = self.tableWidget.horizontalHeaderItem(2)
        # upravuje šířku sloupce tabulky
        self.tableWidget.setColumnWidth(2, 295)
        item.setText(_translate("mainWindow", "Název setu"))

        item = self.tableWidget.horizontalHeaderItem(3)
        self.tableWidget.setColumnWidth(3, 70)
        item.setText(_translate("mainWindow", "Počet kusů"))

        item = self.tableWidget.horizontalHeaderItem(4)
        self.tableWidget.setColumnWidth(4, 92)
        item.setText(_translate("mainWindow", "Datum nákupu"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "Pořizovací cena Kč/ks"))
        self.tableWidget.setColumnWidth(5, 125)

        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("mainWindow", "Aktuální cena"))
        self.tableWidget.setColumnWidth(6, 85)

        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("mainWindow", "Rozdíl ceny"))
        self.tableWidget.setColumnWidth(7, 75)


        self.pridat_polozku.setText(_translate("mainWindow", "Přidat položku"))
        self.upravit_polozku.setText(_translate("mainWindow", "Upravit položku"))
        self.odstranit_polozku.setText(_translate("mainWindow", "Odstranit položku"))
        self.textBrowser_9.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Created by Jiří Mareček</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">BearCock Technology 2023</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">LegoMakesMoney</span></p></body></html>"))

    # dostane url produktu z databáze na základě id
    def get_url(self, id):
        url = "SELECT url FROM lego_sets WHERE id = ?"
        result = self.database.cursor.execute(url, (id,)).fetchone()
        if result:
            url = result[0]
            return url
        return None

    # po kliknutí na tlacitko Upravit položku se otevře editační okno
    def show_edit_window(self):
        # získání informací o označené položce v tabulce
        current_row = self.tableWidget.currentRow()

        # pokud není označen žádný řádek, program se vrátí bez provedení dalšího kódu
        if current_row == -1:
            return

        # pro vyhledání správného url z databáze se z tabulky vytáhne id položky a to je předáno jako parametr metodě get_url
        id_item = self.tableWidget.item(current_row, 0)

        # ověření, zda je označený řádek prázdný. Pokud ano program se vrátí bez provedení dalšího kódu
        if id_item is None or id_item.text() == "":
                return

        # převede id na celočíselnou hodnotu pro další operace
        id = int(id_item.text())
        url = self.get_url(id)

        cislo_setu = self.tableWidget.item(current_row, 1).text()
        nazev_setu = self.tableWidget.item(current_row, 2).text()
        pocet_kusu = self.tableWidget.item(current_row, 3).text()
        datum_nakupu = self.tableWidget.item(current_row, 4).text()
        porizovaci_cena = self.tableWidget.item(current_row, 5).text()

        # Vytvoření instance Ui_edit_window
        self.edit_window = QtWidgets.QDialog()
        self.edit_ui = Ui_edit_window(self.database, self.edit_window)
        self.edit_ui.setupUi(self.edit_window)

        # nastavení hodnot v edit_window
        self.edit_ui.lineEdit.setText(cislo_setu)
        self.edit_ui.lineEdit_2.setText(nazev_setu)
        self.edit_ui.lineEdit_3.setText(pocet_kusu)
        self.edit_ui.lineEdit_4.setText(datum_nakupu)
        self.edit_ui.lineEdit_5.setText(porizovaci_cena)
        self.edit_ui.lineEdit_6.setText(url)

        # nastaví do widgetu text + předá ID označené položky edit window
        self.edit_ui.textBrowser_2.setText(f"Upravit položku ID {id}:")

        # zobrazení okna edit_window
        self.edit_window.show()


    # po kliknutí na tlacitko Přidat položku se otevře nové okno pro vložení nové položky
    def show_add_window(self):
        # Vytvoření instance Ui_add_window
        self.add_window = QtWidgets.QDialog()
        self.add_ui = Ui_add_window(self.database, self.calculator)
        self.add_ui.setupUi(self.add_window)
        self.add_window.show()

    # po kliknutí na Odstranit položku se otevře dialog
    def show_remove_dialog(self):
        # získání informací o označené položce v tabulce
        current_row = self.tableWidget.currentRow()

        # pokud není označen žádný řádek, program se vrátí bez provedení dalšího kódu
        if current_row == -1:
            return

        # pro vyhledání správného url z databáze se z tabulky vytáhne id položky a to je předáno jako parametr metodě get_url
        id_item = self.tableWidget.item(current_row, 0)

        # ověření, zda je označený řádek prázdný. Pokud ano program se vrátí bez provedení dalšího kódu
        if id_item is None or id_item.text() == "":
            return

        # Vytvoření instance třídy RemoveDialog
        dialog = RemoveDialog()

        # zobrazení dialogového okna a získání výsledku
        result = dialog.exec()

        # zpracování výsledku dialogového okna
        if result == QMessageBox.StandardButton.Yes:
            self.remove_item()


    # metoda odstraní položku z databáze a z tabulky
    def remove_item(self):
        # získání informací o označené položce v tabulce
        current_row = self.tableWidget.currentRow()

        # pro vyhledání správného url z databáze se z tabulky vytáhne id položky a to je předáno jako parametr metodě get_url
        id_item = self.tableWidget.item(current_row, 0)
        id = int(id_item.text())

        # Odstranění položky z databáze
        self.database.cursor.execute("DELETE FROM lego_sets WHERE id = ?", (id,))
        self.database.connection.commit()

        # Odstranění položky z tabulky
        self.tableWidget.removeRow(current_row)

    def press_F5_update_data(self):
        self.finder.find()
        self.calculator.calculate_difference()
        self.calculator.calculate_total_price()
        self.calculator.caculate_price_increase()





