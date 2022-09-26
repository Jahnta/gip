import csv

with open('spareparts_data_GT42.csv', 'r', encoding='utf-8-sig', newline='') as csvfile:
    sp_reader = csv.reader(csvfile, delimiter=';')
    spareparts_list = list(sp_reader)

total = 0
count = 0

try:
    x = spareparts_list[0].index('Статус')
except:
    x = 0

for sparepart in spareparts_list[1:]:
    a = ''
    for s in sparepart[spareparts_list[0].index('Цена НИЗ')]:
        if s in '0123456789.,':
            a += s
    total += float(sparepart[spareparts_list[0].index('Кол-во НИЗ')].replace(',', '.') or 0) * float(
        a.replace(',', '.') or 0)

    print(f'''@{sparepart[spareparts_list[0].index('Статус')]}@''')

    if sparepart[spareparts_list[0].index('Статус')] == ' Доставлено ' and sparepart[0]:
        count += 1

total_str = '{:,}'.format(round(total, 2)).replace(',', ' ')

if total != 0:
    count_percent = round((count / total), 2)
else:
    count_percent = 0

print(total)

print(len(set(x[0] for x in spareparts_list)))

print(count, count_percent)