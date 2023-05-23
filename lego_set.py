class LegoSet:

    # kontruktor lego setu
    def __init__(self, cislo_setu, nazev_setu, pocet_kusu, datum_nakupu, porizovaci_cena, url):
        self.cislo_setu = cislo_setu
        self.nazev_setu = nazev_setu
        self.pocet_kusu = pocet_kusu
        self.datum_nakupu = datum_nakupu
        self.porizovaci_cena = porizovaci_cena
        self.url = url

    def __str__(self):
        return f"{self.cislo_setu} {self.nazev_setu} {self.pocet_kusu} {self.datum_nakupu} {self.porizovaci_cena} {self.url}"