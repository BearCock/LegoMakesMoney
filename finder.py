import requests
from bs4 import BeautifulSoup
import re


class Finder:
    def __init__(self, database):
        self.database = database
        self.ids = self.get_ids()

    def get_ids(self):
        ids = self.database.cursor.execute("SELECT id FROM lego_sets").fetchall()
        return [id[0] for id in ids]

    def get_urls(self):
        urls = self.database.cursor.execute("SELECT url FROM lego_sets").fetchall()
        return [url[0] for url in urls]

    def find(self):
        #cyklus pro iteraci položek url
        for id in self.ids:
            # použití modulu requests
            # stáhne HTML obsah URL pomocí funkce "get" z modulu "requests" a uloží ho do proměnné "requests".
            url = self.database.cursor.execute("SELECT url FROM lego_sets WHERE id=?", (id,)).fetchone()[0]
            response = requests.get(url)

        # uloží obsah HTML z proměnné " response" do proměnné html_content
            html_content = response.text

        # vytvoří "BeautifulSoup" objekt z HTML obsahu uloženého v proměnné "html_content"
            soup = BeautifulSoup(html_content, 'html.parser')

        # tato část kódu najde všechny výskyty tagů s třídou "c-offer__price" a uloží je do seznamu "find_price_tags"
        # je to nutné kvůli tomu, že ne vždy se ze stránky stáhnou data o ceně 1. položky, ale kolikrát to bere top_produkt
            find_price_tags = soup.find_all('div', {'class': 'c-offer__price'})

            """  
            - funkce sub() z modulu re nahrazuje všechny výskyty vzoru v řetězci jiným řetězcem.
            - řetězce s regulárními výrazy zapisovat s prefixem "r" ("raw").
                prefix umožňuje psát regulární výrazy bez nutnosti escapovat zpětnými lomítky všechny speciální znaky.

            [^ ... ]: neguje vše, co není v závorce
            \d: shoduje se s libovolnou číslicí (0-9)
            ,: shoduje se s čárkou
            .: shoduje se s tečkou
             """
            sorted_price_items = sorted(find_price_tags,
                                    key=lambda tag: float(re.sub(r'[^\d,.]', '', tag.text).replace(',', '.')))

        # vybere 1. položku ze seznamu, tedy položku s nejnižší cenou
            lowest_item_price = sorted_price_items[0].text

            # k url může vypsat id položky
            id_lego_set = self.database.cursor.execute("SELECT id FROM lego_sets WHERE url=?", (url,)).fetchone()[0]

            result = (float(re.sub(r'[^\d,.]', '', lowest_item_price).replace(',', '.')), id)

            # uložení ceny do databáze pomocí metody ze třídy Database
            print(result)
            self.database.update_data_aktualni_cena(result[0], id_lego_set)



