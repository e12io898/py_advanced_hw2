test = ['', '', '']
test1 = ' '.join(test).split()
print(test1)
# (7|8)?\s*?\((\d{3})\)\s*(\d{2}|\d{3})[\s-]+(\d+)[\s-]+(\d{2}|\d{4})
print()
# # Ф + И + О (правильно):
# if row[0] != '' and row[1] != '' and row[2] != '':
#     lastname, firstname, surname = row[0], row[1], row[2]
#     print(lastname, firstname, surname)
# # ФИО (ФИ) + '' + '':
# elif row[1] == '' and row[2] == '':
#     # ФИО + '' + '':
#     if len(row[0].split()) == 3:
#         lastname, firstname, surname = row[0].split()
#         print(lastname, firstname, surname)
#     # ФИ + ''
#     elif len(row[0].split()) == 2:
#         lastname, firstname = row[0].split()
#         surname = ''
#         print(lastname, firstname, surname)
# # Ф + ИО + '':
# elif len(row[1].split()) == 2 and row[2] == '':
#     lastname = row[0]
#     firstname, surname = row[1].split()
#     print(lastname, firstname, surname)

pat1 = r'(\+7|8)?\s*\(?(\d{3})\)?\D*?(\d{3})\D*?(\d{2})'r'\D*?(\d{2})'
pat2 = r'(\s*\(?[доб\.]*\s*(\d+)\)?)?'

print('Мартиняхин' == 'Мартиняхин')