import csv

from bs4 import BeautifulSoup
import requests
import locale
import re

import json
import os

class  Parser:
    def __init__(self):
        self.log_data = []
        pass

    def agent(self):
        try:
            test_url3 = 'https://lk.rs-class.org/regbook/vessel?fleet_id=1003542'
            HEADERS_test = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0'
                              ' YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36', 'accept': '*/*'}

            req = requests.get(test_url3, headers=HEADERS_test, params=None)
            src = req.text
            self.soup = BeautifulSoup(src, 'lxml')
            self.status = 'Успешное подключение'
            return self.soup
        except:
            self.status = 'Ошибка подключения'

    def parse_head(self):
        titles_mass = []
        main_title = self.soup.find_all(class_="service-main-block nav-item square-xs-block square-xl-block col-4 col-md-4 col-xl-4")
        for title in main_title:
            title = title.find(class_ = 'title').get_text().strip()
            titles_mass.append(title)
        return titles_mass

par = Parser()
par.agent()
print(par.parse_head())