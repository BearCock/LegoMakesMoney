from database import Database
from finder import Finder
from calculator import Calculator
from main_window import Ui_mainWindow
from PyQt6 import QtWidgets, QtGui, QtCore
import os
import sys

# Nastavení cesty k databázi
database_path = os.path.abspath("database.db")
# Vytvoření instance databáze
lego_database = Database(database_path)
# Připojení k databázi
lego_database.connect()

# Vytvoření instance třídy Finder a předání instance třídy Database jako argument konstruktoru
finder = Finder(lego_database)

# Blok úvodního textu do konzole
print("__________________________________________________")
print("LegoMakesMoney")
print("Created by Jiří Mareček, BearCock Technology 2023©")
print("__________________________________________________\n")

# Získání aktuálních cen produktů z internetu a uložení do databáze
finder.find()

# Vytvoření instance třídy Calculator a předání instance třídy Database jako argument konstruktoru
calculator = Calculator(lego_database)

# Vytvoření instance třídy Ui_mainWindow
main_window = Ui_mainWindow(lego_database, calculator, finder)

# Spuštění výpočtů
calculator.calculate_difference()
calculator.calculate_total_price()
calculator.calculate_price_increase()

# Spuštění hlavního okna main_window
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QDialog()
    main_window.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
