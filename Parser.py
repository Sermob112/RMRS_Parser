import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import locale
import re

import json
import os

class  Parser:
    def __init__(self):
        self.log_data = []
        self.all_data = []
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

    def all_info(self):
        info = {}

        tablse = self.soup.find_all(class_= 'table table-bordered table-striped fs14 mb40')
        for table in tablse:
            tr = table.find_all('td')
            for td in tr:
                td = td.get_text().strip()
                self.all_data.append(td)

        # return self.all_data

    def execl_maker(self):
        columns = [self.all_data[i] for i in range(len(self.all_data)) if i % 2 == 0]
        # Создаем пустой DataFrame
        df = pd.DataFrame(columns=columns)

        # Добавляем значения в DataFrame
        for i in range(1, len(self.all_data), 2):
            df.loc[0, columns[i // 2]] = self.all_data[i]
        df.to_excel('output.xlsx', index=False)
par = Parser()
par.agent()
par.all_info()
par.execl_maker()
# print(par.parse_head())