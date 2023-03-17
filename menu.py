from config import open_file
from config import show_contacts
from config import save_file
from config import add_contact
from config import find_contact
from config import change_contact
from config import delete_contact


def menu():
    print('\nЭто меню телефонного справочника:\n'
          '1.Открыть файл\n'
          '2.Сохранить файл\n'
          '3.Показать контакты\n'
          '4 Добавить контакт\n'
          '5 Найти контакт\n'
          '6 Изменить контакт\n'
          '7 Удалить контакт\n'
          '8 Выход\n')
    data = int(input('Выберите действия: '))
    return data


while True:
    user_choice = menu()
    match user_choice:
        case 1:
            open_file()
            print('-' * 100)
        case 2:
            save_file()
            print('-' * 100)
        case 3:
            show_contacts()
            print('-' * 100)
        case 4:
            add_contact()
            print('-' * 100)
        case 5:
            find_contact()
            print('-' * 100)
        case 6:
            change_contact()
            print('-' * 100)
        case 7:
            delete_contact()
            print('-' * 100)
        case 8:
            print('Справочник закрыт')
            print('-' * 100)
            break
