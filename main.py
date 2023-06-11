import re
import csv

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # Конечный список контактов:
    phonebook = [['lastname', 'firstname', 'surname', 'organization',
                  'position', 'phone', 'email']]
    # Словарь для удаления дублей:
    book_raw = {}

    for row in contacts_list[1:]:
        # Извлечение ФИО:
        name_row = ' '.join(row[0:3]).split()
        lastname, firstname, surname = '', '', ''
        if len(name_row) == 3:
            lastname, firstname, surname = name_row
        else:
            name_row_upd = ['' for i in range(3 - len(name_row))]
            lastname, firstname, surname = name_row + name_row_upd

        # Оставшиеся поля:
        organization, position, phone, email = row[3:7]

        # Паттерн для поиска номеров телефона (разделён, т.к. длинный слишком):
        pat1 = r'(\+7|8)?\s*\(?(\d{3})\)?\D*?(\d{3})\D*?(\d{2})'r'\D*?(\d{2})'
        pat2 = r'(\s*\(?[доб\.]*\s*(\d+)\)?)?'
        pattern = pat1 + pat2

        # Проверка на наличие добавочного номера и соответствующее изменение:
        if 'доб' in phone:
            sub_pattern = r'+7(\2)\3-\4-\5 доб. \7'
            phone = re.sub(pattern, sub_pattern, phone)
        else:
            sub_pattern = r'+7(\2)\3-\4-\5'
            phone = re.sub(pattern, sub_pattern, phone)

        values = [firstname, surname, organization, position, phone, email]

        # Объединение дублирующихся записей:
        if lastname not in book_raw:
            book_raw[lastname] = values
        else:
            for i in range(len(book_raw[lastname])):
                if book_raw[lastname][i] == '':
                    book_raw[lastname][i] = values[i]
                    
    # Добавление в конечный список контактов:
    for i in book_raw:
        phonebook.append([i] + book_raw[i])

    # Запись в новый файл:
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(phonebook)