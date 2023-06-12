from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас данные из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        data_middle = ''
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    print('Вывожу данные для Вас данные из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        print(f'Изменить данную запись\n{data_first[number_journal]}')

        data_temp=data_first[number_journal].split()
        vibor_polya=int(input("Что хотите поменять: 1.Имя 2.Фамилию 3.Номер телефона 4.Город"))

        if vibor_polya ==1:
            data_first = data_first[:number_journal] + [f'{name_data()}\n{data_temp[1]}\n{data_temp[2]}\n{data_temp[3]}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya==2:
            data_first = data_first[:number_journal] + [
                f'{data_temp[0]}\n{surname_data()}\n{data_temp[2]}\n{data_temp[3]}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya == 3:

            data_first = data_first[:number_journal] + [
                f'{data_temp[0]}\n{data_temp[1]}\n{data_temp[2]}\n{phone_data()}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya == 4:
            data_first = data_first[:number_journal] + [
                f'{data_temp[0]}\n{data_temp[1]}\n{data_temp[2]}\n{address_data()}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya == 5:
            data_first = data_first[:number_journal] + [
                f'{name_data()}\n{surname_data()}\n{phone_data()}\n{address_data()}\n'] + \
                         data_first[number_journal + 1:]


        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Изменить данную запись\n{data_second[number_journal]}')
        data_temp=data_second[number_journal].split(';')
        vibor_polya=int(input("Что хотите поменять: 1.Имя 2.Фамилию 3.Номер телефона 4.Город 5.Всю "))

        if vibor_polya == 1:
            data_second = data_second[:number_journal] + [
                f'{name_data()};{data_temp[1]};{data_temp[2]};{data_temp[3]}\n'] + \
                          data_second[number_journal + 1:]
        elif vibor_polya == 2:
            data_second = data_second[:number_journal] + [
                f'{data_temp[0]};{surname_data()};{data_temp[2]};{data_temp[3]}\n'] + \
                          data_second[number_journal + 1:]
        elif vibor_polya == 3:

            data_second = data_second[:number_journal] + [
                f'{data_temp[0]};{data_temp[1]};{phone_data()};{data_temp[3]}\n'] + \
                          data_second[number_journal + 1:]
        elif vibor_polya == 4:
            data_second = data_second[:number_journal] + [f'{data_temp[0]};{data_temp[1]};{data_temp[2]};{address_data()}\n'] + \
                      data_second[number_journal + 1:]
        elif vibor_polya == 5:
            data_second = data_second[:number_journal] + [f'{name_data()};{surname_data()};{phone_data()};{address_data()}\n'] + \
                      data_second[number_journal + 1:]

        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_first[number_journal - 1]}')
        data_temp=data_first[number_journal].split()
        vibor_polya = int(input("Что хотите удалить: 1.Имя 2.Фамилию 3.Номер телефона 4.Город 5.Всю "))

        if vibor_polya == 1:
            data_first = data_first[:number_journal] + [
                f'{""}\n{data_temp[1]}\n{data_temp[2]}\n{data_temp[3]}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya == 2:
            data_first = data_first[:number_journal] + [
                f'{data_temp[0]}\n{""}\n{data_temp[2]}\n{data_temp[3]}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya == 3:

            data_first = data_first[:number_journal] + [
                f'{data_temp[0]}\n{data_temp[1]}\n{""}\n{data_temp[3]}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya == 4:
            data_first = data_first[:number_journal] + [
                f'{data_temp[0]}\n{data_temp[1]}\n{data_temp[2]}\n{""}\n'] + \
                         data_first[number_journal + 1:]
        elif vibor_polya == 5:
            data_first = data_first[:number_journal] + data_first[number_journal + 1:]


        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        print(data_second)
        data_temp = data_second[number_journal-1].split(';')
        vibor_polya = int(input("Что хотите удалить: 1.Имя 2.Фамилию 3.Номер телефона 4.Город 5.Всю "))

        if vibor_polya == 1:
            data_second = data_second[:number_journal-1] + [
                f'{""};{data_temp[1]};{data_temp[2]};{data_temp[3]}'] + \
                          data_second[number_journal:]
        elif vibor_polya == 2:
            data_second = data_second[:number_journal-1] + [
                f'{data_temp[0]};{""};{data_temp[2]};{data_temp[3]}\n'] + \
                          data_second[number_journal:]
        elif vibor_polya == 3:
            data_second = data_second[:number_journal-1] + [
                f'{data_temp[0]};{data_temp[1]};{""};{data_temp[3]}\n'] + \
                          data_second[number_journal:]
        elif vibor_polya == 4:
            data_second = data_second[:number_journal-1] + [
                f'{data_temp[0]};{data_temp[1]};{data_temp[2]};{""}\n'] + \
                          data_second[number_journal:]
        elif vibor_polya == 5:
            data_second = data_second[:number_journal] + data_second[number_journal + 1:]

        init =input('pause')
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')  # Можно вывести конечные данные
