import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)
contacts_list.pop(0)

for item in contacts_list:
    fio = item[0].split(" ")
    for i, word in enumerate(fio):
        item[i] = word.strip()


    pattern_phone = re.compile(
        r'(\+*)([0-9])([\s]*)(\(*)(\d{3})([\)\-]*)(\s*)(\d{3})([\-]*)(\d{2})([\-]*)(\d{2})(\s*)(\(*)([а-я]*\.*)(\s*)(\d*)(\)*)')
    repl_phone = r'+7(\5)\8-\10-\12 доб.\17'
    item[-2] = re.sub(pattern_phone, repl_phone, item[-2])

def combine_doubles(contacts_list):
    lastname = []
    combine = {}
    book = []
    for item in contacts_list:
        lastname.append(item[0])
    for item in contacts_list:
        if lastname.count(item[0]) > 1:
            if item[0] in combine.keys():
                combine[item[0]].append(item)
            else:
                combine[item[0]] = [item, ]
        else:
            book.append(item)
    for doubled in combine.values():
        out_list = []
        for i, word in enumerate(doubled[0]):
            if word:
                out_list.append(word)
            else:
                for items in range(len(doubled)):
                    if doubled[items][i]:
                        out_list.append(doubled[items][i])
                        break
        book.append(out_list)
    return book

# pprint(combine_doubles(contacts_list))
my_list = []
my_list = combine_doubles(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(my_list)