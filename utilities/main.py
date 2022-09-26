import csv

a = 'spareparts_data_GT42.csv'

def get_spareparts_data(file_path):

    with open(file_path, 'r', encoding='utf-8-sig', newline='') as csvfile:
        sp_reader = csv.DictReader(csvfile, delimiter=';')
        spareparts_list = list(sp_reader)

    print(spareparts_list[0])

    cats = {
        'all' : {
            'count' : 0,
            'value' : 0
        }
    }

    for line in spareparts_list:
        cat = line['Категория ВЕРХ']
        u = float(line['SET'].replace(',', '.') or 0)
        q = float(line['Кол-во НИЗ'].replace(',','.').replace(' ','') or 0)
        p = float(''.join(x for x in line['Цена НИЗ'] if x in '0123456789,').replace(',','.') or 0)

        if cat not in cats.keys():
            cats[cat] = {
                'count' : 0,
                'value' : 0
            }

        cats[cat]['count'] += u
        cats['all']['count'] += u

        cats[cat]['value'] += q * p
        cats['all']['value'] += q * p

    print(cats)

get_spareparts_data(a)