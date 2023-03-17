phone_book = []

def open_file():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        phone_book = data.readlines()
        print('Файл открыт')
        return phone_book


def show_contacts():
    if len(phone_book) == 0:
        print('Файл ещё не открыт')
    else:
        for i in phone_book:
            print(' '.join(i.split(';')).title())


def save_file():
    with open('phone_book.txt', 'w', encoding='utf-8') as data:
        for i in phone_book:
            data.write(i)


def add_contact():
    if len(phone_book) == 0:
        print('Файл ещё не открыт')
    else:
        user_info = input('Введите новый контакт: ')
        user_info = ';'.join(user_info.split(' ')).lower()
        phone_book.append(user_info)


def find_contact():
    if len(phone_book) == 0:
        print('Файл ещё не открыт')
    else:
        find_user = input('Видите имя контакта которого нужно найти: ').lower()
        for user in phone_book:
            if find_user in user:
                print(user)
                break
        else:
            print('Такого контакта нет')


def change_contact():
    if len(phone_book) == 0:
        print('Файл ещё не открыт')
    else:
        user_info = input('Видите контакт которую нужно изменить: ').lower()
        for i in range(len(phone_book)):
            if user_info in phone_book[i]:
                print(phone_book[i])
                new_user_info = input('Видите новые данные: ').lower()
                new_user_info = ';'.join(new_user_info.split(' ')).lower()
                phone_book[i] = phone_book[i].replace(phone_book[i], (new_user_info + ';' + '\n').lower())


def delete_contact():
    if len(phone_book) == 0:
        print('Файл ещё не открыт')
    else:
        deleting_user = input('Видите контакт которую нужно удалить: ').lower()
        for i in range(len(phone_book)):
            if deleting_user in phone_book[i]:
                print('\n' + phone_book[i].title())
                q = str(input('Вы уверены что хотите удалить этот контакт' + '\n' +
                              'нажмите  Y - чтобы удалить' + '\n' +
                              'нажмите N - чтобы не удалять' + '\n' + ':'))
                if q == 'y' or q == 'Y':
                    del phone_book[i]
                    print('Контакт удалён')
                    break


phone_book = open_file()
