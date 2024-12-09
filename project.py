import os
import csv
import sys

'''Использованы только проприетарные библиотеки.'''


class PriceMachine:

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, file_path=r'.'):
        good = ['товар', 'название', 'наименование', 'продукт']
        price = ['розница', 'цена']
        weight = ['вес', 'масса', 'фасовка']
        fields = {'Наименование': good, 'Цена': price, 'Вес': weight}
        for files in os.walk(file_path):
            for file in files[-1]:
                if 'price' in file and file.endswith('.csv'):
                    with open(file, 'r', encoding='utf-8') as f:
                        rows = csv.DictReader(f)
                        # Приведение к единому формату {Наименование: наименование, Цена: цена, Вес: вес}
                        for row in rows:
                            row = {k: v.lower() for k, v in row.items() if k in (good + price + weight)}
                            for i in fields:
                                for j in fields[i]:
                                    if j in row.keys():
                                        row[i] = row.pop(j)
                            if self.name_length < len(row['Наименование']):
                                self.name_length = len(row['Наименование'])
                            row.setdefault('file_name', file)
                            self.data.append(row)
            # self.name_length = len(max(self.data, key=lambda name: len(name['Наименование']))['Наименование'])
            self.data.sort(key=lambda x: float(x['Цена']) / float(x['Вес']))
            return self.data

    # Заготовка не использована, т.к. в работе использован словарь
    # def _search_product_price_weight(self, headers):
    #     '''
    #         Возвращает номера столбцов
    #     '''

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
        for number, item in enumerate(self.data):
            product_name, price, weight, file_name = item.values()
            result += '<tr>'
            result += f'<td>{number + 1}</td>'
            result += f'<td>{product_name}</td>'
            result += f'<td>{price}</td>'
            result += f'<td>{weight}</td>'
            result += f'<td>{file_name}</td>'
            result += f'<td>{round(float(price) / float(weight), 2)}</td></tr>\n'

        with open(fname, 'w', encoding='utf-8') as fn:
            fn.write(result)
        return "Данные в " + str(fname)

    def find_text(self, text):
        data = []
        for item in self.data:
            if text.lower() in item['Наименование'].lower():
                data.append(item)
        if len(data) == 0:
            print('Ничего не найдено.')
            return
        print(
            f'{'№'.ljust(5, " ")}'
            f'{'Наименование'.ljust(self.name_length, " ")}'
            f'{'Цена'.center(6, " ")}'
            f'{'Вес'.center(3, " ")}'
            f'{"Файл".center(13, " ")}'
            f'{'Цена за кг.'.center(9, ' ')}'
        )

        for i in range(len(data)):
            print(
                f'{str(i + 1).ljust(5, " ")}'
                f'{data[i]['Наименование'].ljust(self.name_length, " ")}'
                f'{data[i]['Цена'].rjust(6, " ")}'
                f'{data[i]['Вес'].rjust(3, " ")}'
                f'{data[i]["file_name"].center(13, " ")}'
                f'{str(round(float(data[i]['Цена']) / float(data[i]['Вес']), 2)).ljust(9, ' ')}'
            )
        print('\n' + 'Введите слово или его часть для поиска продукта либо exit для выхода из программы: ')


pm = PriceMachine()
print(pm.load_prices())

if __name__ == '__main__':
    print('\n' + 'Введите слово или его часть для поиска продукта либо exit для выхода из программы: ')
    for line in sys.stdin:
        if 'exit' in line[:-1].lower():
            print('\n' + 'the end' + '\n')
            to_html = input('Перенести данные в HTML? Д/Н ')
            if to_html.lower() in 'lfда':
                print(pm.export_to_html())
            sys.exit()
        pm.find_text(line[:-1].lower())