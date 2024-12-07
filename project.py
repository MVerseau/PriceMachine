import os
import json
import csv
import sys


class PriceMachine():
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0
    
    def load_prices(self, file_path=r'.'):
        good=['товар','название','наименование','продукт']
        price=['розница','цена']
        weight=['вес','масса','фасовка']
        for files in os.walk(file_path):
            print(files)
            for file in files[-1]:
                if 'price' in file and file.endswith('.csv'):
                    with open(file, 'r', encoding='utf-8') as file:
                        rows=csv.DictReader(file)
                        for row in rows:
                            row={k:v for k,v in row.items() if k in (good+price+weight)}
                            print(row)
            return self.data
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        
    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''

    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
    
    def find_text(self, text):
        pass
    
pm = PriceMachine()
print(pm.load_prices())

for line in sys.stdin:
    if 'exit' in line[:-1].lower():
        print('the end')
        sys.exit()
    pm.find_text(line[:-1])

print(pm.export_to_html())
