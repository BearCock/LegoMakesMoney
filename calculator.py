class Calculator:

    def __init__(self, database):
        self.database = database
        self.aktualni_ceny = self.get_aktualni_ceny()
        self.porizovaci_ceny = self.get_porizovaci_ceny()

    # získává aktuální ceny všech lego setů z databáze
    def get_aktualni_ceny(self):
        aktualni_ceny = self.database.cursor.execute("SELECT aktualni_cena FROM lego_sets").fetchall()
        return [aktualni_cena[0] for aktualni_cena in aktualni_ceny]

    # získává pořizovací ceny všech lego setů z databáze
    def get_porizovaci_ceny(self):
        porizovaci_ceny = self.database.cursor.execute("SELECT porizovaci_cena FROM lego_sets").fetchall()
        return [porizovaci_cena[0] for porizovaci_cena in porizovaci_ceny]

    # získává id lego setů z databáze
    def get_lego_set_ids(self):
        ids = self.database.cursor.execute("SELECT id FROM lego_sets").fetchall()
        return [id[0] for id in ids]

    # vypočítá rozdíl mezi cenou nakupu a aktuální cenou
    def calculate_difference(self):
        ids = self.get_lego_set_ids()
        for id_lego_set, (aktualni_cena, porizovaci_cena) in zip(ids, zip(self.aktualni_ceny, self.porizovaci_ceny)):
            difference = aktualni_cena - porizovaci_cena

            self.database.update_data_rozdil_ceny(difference, id_lego_set)

            """zip vezme prvky z každého ze tří seznamů na stejném indexu a vytvoří n-tici. Tyto n-tice pak postupně projde pomocí cyklu for, 
            kde se získají jednotlivé prvky aktuální ceny a pořizovací ceny pro danou Lego stavebnici. Poté jsou tyto prvky použity k výpočtu 
            rozdílu cen, který se uloží do databáze spolu s identifikátorem Lego stavebnice pomocí metody update_data_rozdil_ceny."""


    def calculate_total_price(self):
        # Získá data o sadách Lego z databáze.
        sets = self.database.cursor.execute("SELECT pocet_kusu, porizovaci_cena FROM lego_sets").fetchall()

        # Inicializuje proměnnou pro celkovou cenu
        total_price = 0

        # cyklus projde všechny sety
        for set in sets:
            # Získá počet kusů a pořizovací cenu aktuální sady Lego.
            pocet_kusu, porizovaci_cana = set

            # Pokud je více než jeden kus, vypočítá celkovou cenu jako součin počtu kusů a pořizovací ceny.
            if pocet_kusu > 1:
                total_price += pocet_kusu * porizovaci_cana
            # Pokud máme jen jeden kus, použijeme pouze pořizovací cenu.
            else:
                total_price += porizovaci_cana

        self.database.update_total_price(total_price)

    def calculate_price_increase(self):
        total_price = self.database.cursor.execute("SELECT celkova_cena_portfolia FROM portfolio_data").fetchone()[0]
        difference_price = self.database.cursor.execute("SELECT rozdil_cen, pocet_kusu FROM lego_sets").fetchall()

        percent = sum([rozdil_cen * pocet_kusu for rozdil_cen, pocet_kusu in difference_price]) / (total_price / 100)
        increase = sum([rozdil_cen * pocet_kusu for rozdil_cen, pocet_kusu in difference_price])

        self.database.update_price_increase(increase, percent)



