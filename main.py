from database import Database
from finder import Finder
from calculator import Calculator
from main_window import Ui_mainWindow
import os
from PyQt6 import QtWidgets


# nastavení cesty k databázi
database_path = os.path.abspath("database.db")
# vytvoření instance databáze
lego_database = Database(database_path)
# připojení k databázi
lego_database.connect()

# vytvoření instance třídy Finder, do konstruktoru přidána jako argument instance třídy Database
finder = Finder(lego_database)
finder.find()

# vytvoření instance třídy Calculator, do konstruktoru přidána jako argument instance třídy Database
calculator = Calculator(lego_database)

# Vytvoření instance třídy Ui_mainWindow
main_window = Ui_mainWindow(lego_database, calculator)

calculator.calculate_difference()
calculator.calculate_total_price()
calculator.caculate_price_increase()

# Spuštění hlavního okna main_window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QDialog()
    main_window.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())


