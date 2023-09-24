'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''
#
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных и поиска по фамилии.


from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(last_name)
    info.append(first_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info


def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()


def write_file(lst):
    # with open('phone.txt', 'a', encoding='utf-8') as data:
    #     data.write(f'{lst[0]};{lst[1]};{lst[2]}\n')

    with open('phone.csv', 'r+', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        for el in res:
            f_n_writer.writerow(el)


def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def search_lastname(file_name):
    last_name = input("Введите фамилию: ")
    records_last_name = [record for record in file_name if last_name.lower() in record["Фамилия"].lower()]
    if not records_last_name:
        print("Фамилия не найдена в справочнике")
    else:
        for record in records_last_name:
            print(record)

def make_changes(file_name):
    last_name = input("Изменение фамилии: ").lower()
    first_name = input("Изменение имени: ").lower()
    record_changes = []
    for record in file_name:
        if record["Фамилия"].lower() == last_name and record["Имя"].lower() == first_name:
            record_changes.append(record)
    if not record_changes:
        print("Not found entry")
    else:
        new_record = get_info()
        for record in record_changes:
            record["Фамилия"] = new_record[0]
            record["Имя"] = new_record[1]
            record["Номер"] = new_record[2]
    with open(file_name, 'w', encoding='utf-8') as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=["Фамилия", "Имя", "Номер"])
        f_n_writer.writeheader()
        f_n_writer.writerows(file_name)
    print("Changes recorded!")

def delete_data(file_name):
    last_name = input("Введите фамилию для удаления: ").lower()
    first_name = input("Введите имя для удаления: ").lower()
    phone_book = read_file(file_name)
    delete_record = []
    for record in phone_book:
        if record["Фамилия"].lower() == last_name and record["Имя"].lower() == first_name:
            delete_record.append(record)

    new_phone_book = [record for record in phone_book if record not in delete_record]

    with open(file_name, "w", encoding="utf-8", newline="") as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=["Фамилия", "Имя", "Номер"])
        f_n_writer.writeheader()
        f_n_writer.writerows(new_phone_book)
    print("Запись удалена")
def record_info():
    lst = get_info()
    write_file(lst)


def main():
    main_menu = '''Главное меню:
    'Открыть файл - r'
    'Создать контакт - w'
    'Поиск по фамилии - s'
    'Изменить контакт - с'
    'Удалить - d'
    'Выход - q'''
    print(main_menu)
    while True:
        command = input('Введите команду: \n')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(*read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 's':
                search_lastname('phone.csv')
        elif command == 'd':
                delete_data('phone.csv')
        elif command == 'c':
                make_changes('phone.csv')
        else:
            print("Invalid command")


main()



