from bs4 import BeautifulSoup as bf
import requests as req


class CursParser:
    """Класс, выполняющий действия над сайтами."""

    def __init__(self, valyta):
        link = "https://www.banki.ru/products/currency/cash/eur/sankt-peterburg/"
        self.LINK = link
        self.content = req.get(self.LINK)
        self.soup = bf(self.content.text, 'html.parser')
        self.valyta = valyta.lower


    def get_bank(self):
        self.LINK = self.LINK.replace("eur", self.valyta)
        all_banks = soup.find_all("a", class_="font-bold")
        all_sails = soup.find_all("div", class_="table-flex__cell table-flex__rate font-size-large   text-nowrap")
        self.banks = ()
        for bank in range(all_banks):
            self.banks.append(str(bank["data-currencies-bank-name"]))
            self.banks.append(str())