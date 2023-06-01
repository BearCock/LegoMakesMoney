import sqlite3

class Database:
    def __init__(self, database_path):
            self.database_path = database_path
            self.connection = None
            self.cursor = None

    def connect(self):
            self.connection = sqlite3.connect(self.database_path)
            self.cursor = self.connection.cursor()

    # metoda se spustí po kliknutí na tlačítko "Přidat položku" a následně se data uloží do databáze
    def insert_lego_set(self, lego_set):
        self.cursor.execute(
            "INSERT INTO lego_sets (cislo_setu, nazev_setu, pocet_kusu, datum_nakupu, porizovaci_cena, url) VALUES (?, ?, ?, ?, ?, ?)",
            (lego_set.cislo_setu, lego_set.nazev_setu, lego_set.pocet_kusu, lego_set.datum_nakupu,
             lego_set.porizovaci_cena, lego_set.url))
        self.connection.commit()

    def update_data_aktualni_cena(self, result, id_lego_set):
        self.cursor.execute("UPDATE lego_sets SET aktualni_cena = ? WHERE id = ?", (result, id_lego_set))
        self.connection.commit()

    def update_data_rozdil_ceny(self, difference, id_lego_set):
        self.cursor.execute("UPDATE lego_sets SET rozdil_cen = ? WHERE id = ?", (difference, id_lego_set))
        self.connection.commit()


    def update_total_price(self, total_price):
        self.cursor.execute("UPDATE portfolio_data SET celkova_cena_portfolia = ?", (total_price,))
        self.connection.commit()

    def update_price_increase(self, price_increase, percent):
        self.cursor.execute("UPDATE portfolio_data SET narust_ceny_portfolia = ?, narust_ceny_portfolia_procenta = ?", (price_increase, percent))
        self.connection.commit()


    def update_all_data(self, cislo_setu, nazev_setu, pocet_kusu, datum_nakupu, porizovaci_cena, url, id):
        self.cursor.execute(
            "UPDATE lego_sets SET cislo_setu=?, nazev_setu=?, pocet_kusu=?, datum_nakupu=?, porizovaci_cena=?, url=? WHERE id=?",
            (cislo_setu, nazev_setu, pocet_kusu, datum_nakupu, porizovaci_cena, url, id))





