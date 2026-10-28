from csv import reader
import random


def find_string(line='Джордж Оруэлл', search_line1='оруэлл', search_line2='джордж'):
    line = line.lower()
    if search_line1.lower() in line and search_line2.lower() in line:
        return 1
    return 0


def search_author(table):
    searchline1 = input('Введите фамилию автора: ')
    searchline2 = input('Введите имя автора: ')
    if searchline1 in ['0', '']:
        return 0
    flag = 0
    for line in table:
        if find_string(line[4], searchline1, searchline2) == 1 and 2016 <= int(line[6][6:10]) <= 2018:
            print(line[1])
            flag += 1
    if flag == 0:
        print('Поиск не успешен')
    input('Нажмите Enter')


def number_name(table):
    list_name = []
    for line in table:
        if len(line[1]) > 30:
            list_name.append(line[1][1:])
    print(len(list_name))
    input('Нажмите Enter')


def generator(table):
    output = open('result.txt', 'w')
    random20 = random.sample(range(0, 1400), 20)
    for str_tabl in random20:
        line = table[str_tabl]
        output.write(f'{random20.index(str_tabl)+1}. {line[3]}. {line[1]} - {line[6][6:10]}\n')
    output.close()
    input('Генерация произведена. Нажмите Enter')


def book_tag(table):
    tags = set()
    for line in table:
        for tag in line[12].split('#'):
            tag = tag.strip() #убрать пробелы по бокам
            if len(tag) != 0:
                tags.add('#' + tag)
    with open('file_tags', 'w') as tags_file:
        for item in sorted(tags):
            tags_file.write(f'{item}\n')
    #print(tags)
    input('Список тегов сохранён в файле \'file_tags\'. Нажмите Enter')


def popular_books(table):
    dict_popular = {}
    for line in table:
        name_book = line[1]
        sold_books = int(line[8])
        author = line[3]
        if name_book in dict_popular:
            dict_popular[name_book][0] += sold_books
        else:
            dict_popular[name_book] = [sold_books, author]
    top_20_books = sorted(dict_popular, key=dict_popular.get, reverse=True)[:20]
    for name in top_20_books:
        print(f'\'{name}\' {dict_popular.get(name)[1]}')
    input('Нажмите Enter')


csvfile = open('books.csv', 'r')
table = list(reader(csvfile, delimiter=';'))
table = table[1:]


while True:
    print('Меню:\n1 - Книги, у которых в записи названия больше 30 символом\n2 - Поиск по атору\n3 - Генерация библиографических ссылок\n4 - Список тегов\n5 - Самые популярные книги\n0 - Выход')
    menu = input('Введите пункт меню: ')
    match menu:
        case '1':
            number_name(table)
        case '2':
            search_author(table)
        case '3':
            generator(table)
        case '4':
            book_tag(table)
        case '5':
            popular_books(table)
        case '0':
            break
        case _:
            print('Это не пункт меню, нажмине Enter')
            input()

#search_author(table)
#number_name(table)
#generator(table)