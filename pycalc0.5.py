#!/usr/bin/env python

# To run it on linux: 1.Open folder with this file in terminal
# 2.Execute with "python (name).py"
import webbrowser

print('Welcome to PyCalculator! :D')


def add(opt1, opt2):
    return opt1 + opt2

def subtract(opt1, opt2):
    return opt1 - opt2

def multiply(opt1, opt2):
    return opt1 * opt2

def divide(opt1, opt2):
    return opt1 / opt2

def modulo(opt1, opt2):
    return opt1 % opt2

def exponent(opt1, opt2):
    return opt1 ** opt2

op_dict = {'+': add,
            '-': subtract,
           '*': multiply,
           '/': divide,
           '%': modulo,
           '^': exponent}

while True:
    print('''
Add (+)
Subtract (-)
Multiply (*)
Divide (/)
Modulo (%)
Exponent (^)
GitHub Respository (Git)''')
    while True:
        choice = input("Your choice: ").lower()

        if choice in op_dict:
            while True:
                try:
                    opt1 = float(input("First number: "))
                    opt2 = float(input("Second number: "))
                except ValueError:
                    print("Didn't I say number? :P")
                    continue

                try:
                    print('{} {} {} = {}'.format(opt1, choice,
                                                 opt2, op_dict[choice](opt1, opt2)))
                except ZeroDivisionError:
                    print("Can't divide by zero!")
                    continue
                except NameError:
                    pass
                break
            break
        elif choice == "git":
            webbrowser.open("https://github.com/exostin/Python-calculator")
            break
        else:
            print('Wrong input! Try again.')
            continue

    again = input('Do you want to do next calculation? [y/n] ').lower()
    if again == 'y':
        continue
    else:
        break
