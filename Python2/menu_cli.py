# -*-coding:Latin-1 -*

import TP1.TP1_1 as tp1_1
import TP1.TP1_2 as tp1_2
import TP1.TP1_3 as tp1_3
import TP1.TP1_4 as tp1_4
import TP1.TP1_5 as tp1_5

import TP2.TP2_1 as tp2_1
import TP2.TP2_2 as tp2_2
import TP2.TP2_3 as tp2_3
import TP2.TP2_4 as tp2_4
import TP2.TP2_5 as tp2_5

import TP3.TP3_4 as tp3_4

def display_main_menu():
    print("Select a TP Module:")
    print("1. TP1 Menu")
    print("2. TP2 Menu")
    print("3. TP3 Menu")
    print("0. Exit")

def display_tp1_menu():
    print("Select a TP1 Module:")
    print("1. TP1_1")
    print("2. TP1_2")
    print("3. TP1_3")
    print("4. TP1_4")
    print("5. TP1_5")
    print("0. Back to Main Menu")

def display_tp2_menu():
    print("Select a TP2 Module:")
    print("1. TP2_1")
    print("2. TP2_2")
    print("3. TP2_3")
    print("4. TP2_4")
    print("5. TP2_5")
    print("0. Back to Main Menu")

def display_tp3_menu():
    print("Select a TP3 Module:")
    print("1. TP3_4")
    print("0. Back to Main Menu")

def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            tp1_menu()
        elif choice == '2':
            tp2_menu()
        elif choice == '3':
            tp3_menu()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def tp1_menu():
    while True:
        display_tp1_menu()
        choice = input("Enter your choice for TP1: ")

        if choice == '1':
            tp1_1.tp1_1_menu()
        elif choice == '2':
            tp1_2.tp1_2_menu()
        elif choice == '3':
            tp1_3.tp1_3_menu()
        elif choice == '4':
            tp1_4.tp1_4_menu()
        elif choice == '5':
            tp1_5.tp1_5_menu()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def tp2_menu():
    while True:
        display_tp2_menu()
        choice = input("Enter your choice for TP2: ")

        if choice == '1':
            tp2_1.tp2_1_menu()
        elif choice == '2':
            tp2_2.tp2_2_menu()
        elif choice == '3':
            tp2_3.tp2_3_menu()
        elif choice == '4':
            tp2_4.tp2_4_menu()
        elif choice == '5':
            tp2_5.tp2_5_menu()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

def tp3_menu():
    while True:
        display_tp3_menu()
        choice = input("Enter your choice for TP3: ")

        if choice == '1':
            tp3_4.tp3_4_menu()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
