import pandas as pd
import openpyxl

import os
import win32com.client as win32
import comtypes.client
from openpyxl import Workbook

# def excel_to_pdf(excel_file_path, pdf_file_path):
#     # Запускаем Excel
#     excel_app = win32.gencache.EnsureDispatch('Excel.Application')
#
#     # Открываем книгу Excel
#     workbook = excel_app.Workbooks.Open(excel_file_path)
#
#     try:
#         # Сохраняем книгу в формате PDF
#         workbook.ExportAsFixedFormat(0, pdf_file_path)
#     except Exception as e:
#         print(f"Ошибка при конвертации в PDF: {e}")
#     finally:
#         # Закрываем книгу Excel
#         workbook.Close(False)
#         # Завершаем Excel
#         excel_app.Quit()
#
# # Пример использования
# excel_file = 'output.xlsx'
# pdf_file = 'pdf_data.pdf'
# excel_to_pdf(excel_file, pdf_file)

# Разделение данных на колонки
# columns = data[0:112][::2]
# values = data[1:len(data)][::2]
#
# # Создание пустого списка для хранения данных в виде столбцов
# columns_data = [[] for _ in range(len(columns))]
# #
# # Заполнение списка данными
# for i, value in enumerate(values):
#     column_index = i % len(columns)  # Определение индекса столбца
#     columns_data[column_index].append(value)
#
# # Создание DataFrame из данных
# df = pd.DataFrame({column: values for column, values in zip(columns, columns_data)})
# #
# # Запись DataFrame в Excel-документ
# df.to_excel('data.xlsx', index=False)

def write_array_to_xlsx(filename):
    # Создаем новую книгу Excel
    workbook = Workbook()
    data = [
        ['Имя', 'Возраст', 'Город'],
        ['Алексей', 25, 'Москва'],
        ['Елена', 32, 'Санкт-Петербург'],
        ['Иван', 18, 'Казань']
    ]

    # Получаем активный лист
    sheet = workbook.active

    # Записываем массив в ячейки листа
    for row in data:
        sheet.append(row)

    # Сохраняем книгу в файл
    workbook.save(f'{filename}/TEST.xlsx')

# Пример использования

write_array_to_xlsx("D:\download")
