from bs4 import BeautifulSoup as bf
import requests as req


class CursParser:
    """Класс, выполняющий действия над сайтами."""

    def __init__(self, valyta):
        link = "https://www.banki.ru/products/currency/cash/eur/sankt-peterburg/"
        self.LINK = link
        self.content = req.get(self.LINK)
        self.soup = bf(self.content.text, 'html.parser')
        self.LINK = self.LINK.replace("eur", valyta)

    def get_bank(self):
        all_banks = self.soup.find_all("a", class_="font-bold")
        all_sails = self.soup.find_all("div", class_="table-flex__cell table-flex__rate font-size-large   text-nowrap")
        banks = []
        for bank in all_banks:
            banks.append(bank["data-currencies-bank-name"])
        banks = tuple(banks)
        return banks

Cur = CursParser("eur")
Cur.get_bank()
