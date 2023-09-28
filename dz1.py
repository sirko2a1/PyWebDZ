import os
from AdressBook.AB import main as ab_main
from NoteBook.NB import main as nb_main
from Map.Map import main as map_main
from sort.sort import main as sort_main
from Game.game import main as game_main

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

class Menu:
    @staticmethod
    def display_menu():
        cls()
        print('MENU')
        choice = input(
            'Вітаю, я ваш персональний помічник.\nОберіть функцію:\n1.Записна книжка\n2.Нотатник\n3.Карта\n4.Сортування папки\n5.Гра\n0.Вихід\n>>>')
        return choice

    @staticmethod
    def run_selected_option(choice):
        if choice == '1':
            cls()
            ab_main()
        elif choice == '2':
            cls()
            nb_main()
        elif choice == '3':
            cls()
            map_main()
        elif choice == '4':
            cls()
            sort_main()
        elif choice == '5':
            cls()
            game_main()

def main():
    while True:
        choice = Menu.display_menu()
        if choice == '0':
            break
        Menu.run_selected_option(choice)

if __name__ == '__main__':
    main()
