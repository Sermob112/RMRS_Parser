import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locale
import re

import json
import os
href="vessel?fleet_id=1102"
class  Parser:
    def __init__(self):
        self.log_data = []
        self.all_data = []
        pass

    def agent(self):
        try:
            test_url3 = 'https://lk.rs-class.org/regbook/regbookVessel'
            self.HEADERS_test = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0'
                              ' YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36', 'accept': '*/*'}

            req = requests.get(test_url3, headers=self.HEADERS_test, params=None)
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



    def get_links(self):
        links = []
        HEADERS_test = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0'
                          ' YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
        url = 'https://lk.rs-class.org/regbook/regbookVessel'
        params = {
            'gorodRegbook_name': '',
            'countryId_name': '%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F',
            'statgr_name': '',
            'icecat_name': '',
            'gorodRegbook': '',
            'countryId': '6CF1E5F4-2B6D-4DC6-836B-287154684870',
            'statgr': '',
            'icecat': '',
            'namer': ''
        }
        # with open("Онлайн информация.html", encoding='UTF-8') as file:
        #     src = file.read()
        response = requests.get(url, params=params, headers=HEADERS_test)
        src = response.text
        soup = BeautifulSoup(src, 'lxml')
        wrapper = soup.find(class_='table table-bordered table-striped fs14')
        linkers = wrapper.find_all('a')
        for link in linkers:
            link = 'https://lk.rs-class.org/regbook/'+ link.get('href')
            links.append(link)

        return links

    def get_all_links_selenium(self):

        HEADERS_test = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0'
                          ' YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
        # driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
        # driver.get('https://lk.rs-class.org/regbook/regbookVessel')
        # # driver.execute_script("lite('getDictionary2?d=countryId&f=formfield')")
        # #Рабочий код
        # wait = WebDriverWait(driver, 1)
        # country_input = wait.until(EC.presence_of_element_located((By.ID, "countryId_name")))
        #
        # # Кликаем на поле ввода, чтобы открыть модальное окно
        # country_input.click()
        # #####################################################
        # frame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name='h-100 bx-core bx-no-touch bx-no-retina bx-chrome']")))
        # # Выводим код фрейма модального окна
        # print(frame)
        url = 'https://lk.rs-class.org/regbook/regbookVessel'
        params = {
            'gorodRegbook_name': '',
            'countryId_name': '%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F',
            'statgr_name': '',
            'icecat_name': '',
            'gorodRegbook': '',
            'countryId': '6CF1E5F4-2B6D-4DC6-836B-287154684870',
            'statgr': '',
            'icecat': '',
            'namer': ''
        }
        response = requests.get(url, params=params,headers=HEADERS_test)
        src = response.text
        soup = BeautifulSoup(src, 'lxml')
        print(soup)
        # Ожидаем появления кнопки "Найти" и кликаем на нее
        # find_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")))
        # find_button.click()

        # print(html)
        # link_element = result.find_element(By.XPATH,"//a[contains(text(), 'Россия')]")
        # link_element.click()
        # res2 = result.execute_script("return sendall2('formfield','countryId','6CF1E5F4-2B6D-4DC6-836B-287154684870','Россия')")

        # time.sleep(10)
        # html = driver.page_source
        #
        # soup = BeautifulSoup(html, 'lxml')

        # driver.quit()
        # wrapper = soup.find_all(class_='col-12 col-md-10 col-main-with-sidebar pl0 pr0')
        # links = []
        # step = self.soup.find(class_ = 'myTable0')
        # linkers = step.find_all('a')

        # for link in linkers:
        #     link = 'https://lk.rs-class.org/regbook/' + link.get('href')
        #     links.append(link)
        # return links

    def all_info(self):
        HEADER = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0'
                          ' YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
        info = {}
        i = 0

        links = self.get_links()
        t = len(links)
        for link in range(t):
            req = requests.get(links[link], headers=HEADER, params=None)
            src = req.text
            soup = BeautifulSoup(src, 'lxml')
            tablse = soup.find_all('td')
            for table in tablse:
                table = table.get_text().strip()
                self.all_data.append(table)
            i = i + 1
            print(f"текущая итерация {i} из {t}")



        return self.all_data

    def all_info_optimazed(self):
        all_data = []
        HEADER = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0'
                          ' YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36', 'accept': '*/*'}

        test_url3 = 'https://lk.rs-class.org/regbook/vessel?fleet_id=1102'

        req = requests.get(test_url3, headers=HEADER, params=None)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        tablse = soup.find_all('td')
        for table in tablse:
            table = table.get_text().strip()
            all_data.append(table)
        return all_data
    def execl_maker(self):
        # columns = [self.all_data[i] for i in range(len(self.all_data)) if i % 2 == 0]
        # # Создаем пустой DataFrame
        # df = pd.DataFrame(columns=columns)
        #
        # # Добавляем значения в DataFrame
        # for i in range(1, len(self.all_data), 2):
        #     df.loc[0, columns[i // 2]] = self.all_data[i]
        # df.to_excel('output.xlsx', index=False)

        columns = self.all_data[0:112][::2]
        values = self.all_data[1:len(self.all_data)][::2]

        # Создание пустого списка для хранения данных в виде столбцов
        columns_data = [[] for _ in range(len(columns))]
        #
        # Заполнение списка данными
        for i, value in enumerate(values):
            column_index = i % len(columns)  # Определение индекса столбца
            columns_data[column_index].append(value)

        # Создание DataFrame из данных
        df = pd.DataFrame({column: values for column, values in zip(columns, columns_data)})
        #
        # Запись DataFrame в Excel-документ
        df.to_excel('data.xlsx', index=False)
par = Parser()
# par.get_all_links_selenium()
# par.agent()

# print(par.all_info_optimazed())
par.get_links()
par.all_info()

# print(par.get_all_links())
# par.all_info()
par.execl_maker()
# print(par.parse_head())