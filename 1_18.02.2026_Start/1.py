# print("Hello world")
# multiline string
# dynamic string, formatted string
# winner = "X" 
# loser = "O"
# message = f"Player {winner} is winner, player {loser} lost!"

# константа - це зміна, значення якої ви не плануєте змінювати
# MENU = """
# Hello! Welcome to tic tac toe game
# Rules: X and O takes turns on the grid 3x3
# """
# print(MENU)
# print(message)

#winner = input("Please enter Your sign >>> ")
#loser = input("Please enter Your sign >>> ")

#message = f"Player {winner} is winner, player {loser} lost!"
#print(message)

# sign = input("Please enter your sign (X або Y): ")
# message = f"Player {sign}, your turn!"
# print(message)

# SIGN = {
#     1: "X",
#     2: "O",
# }

# winner_sign = int(input("Please choose a sign [1: X, 2: O] >>> "))
# print(winner_sign)
# print(type(winner_sign))

# message = f"Player {SIGN[winner_sign]} is winner!"
# print(message)

# 

# SIGN = {
#     1: "X",
#     2: "O",
# }

# choice = int(input("Player 1, what's your sign? [choose 1:X or 2:O]: >>> "))

# PPP = {
#     choice % 2 == 0: "True",
#     choice % 2 == 1: "False",
# }

# #message1 = f"Player {SIGN[choice]} is winner!"
# message2 = f"Результат перевірки на парність - {PPP[choice]}"
# #print(message1)
# print(message2)

# choice = int(input("Player 1, what's your sign? [choose 1:X or 2:O]: >>> "))
# message = f"Результат перевірки на парність - {choice % 2 == 0}"
# print(message)

# age = int(input("Hello! What's Your age >>> "))
# print("Welcome to the bar!")
# if age > 18:
#     print("Here is Your beer")
# else:
#     print("You are too young")
# age = int(input("What is your age? >>> "))
# gender = input("What is your gender? [M/F] >>> ")
# if age < 18:
#     if gender == "M":
#         print("Son")
#     else:
#         print("Daughter")
# elif age >= 18 and age < 65:
#     if gender == "M":
#         print("Father")
#     else:
#         print("Mother")
# else:
#     if gender == "M":
#         print("Grandfather")
#     else:
#         print("Grandmother")
# choice = int(input("Player 1, what's Your sign? [choose 1:X or 2:O]"))
# if choice == 1:
#     player1 = "X"
#     player2 = "O"
# elif choice == 2:
#     player1 = "O"
#     player2 = "X"
# elif:
#     print("Not an option, please choose 1 or 2")
# result = f"Plyer1: {player1}, Player2: {player2}"
# print(result)
# has_winner = bool(input("Is there a winner: "))
# count = int(input("What turn is it: "))
# if has_winner == True or count > 8:
#     print("Game is over!")
# else:
#     print("Keep playing!")
# choice = int(input("Player 1, what's your sign? [choose 1:X or 2:O]: "))
    
# if choice == 1:
#     player1 = "X"
#     player2 = "O"
#     print("""player1 = "X", а player2 = "O""")
# elif choice == 2:
#     player1 = "O"
#     player2 = "X"
#     print("""player1 = "O", а player2 = "X""")
# else:
#     print("Not an option")
# >>> text = "to be or not to be"
# >>> text.find("be")
# 3
# >>> text.upper()
# 'TO BE OR NOT TO BE'
# >>> text.split()
# ['to', 'be', 'or', 'not', 'to', 'be']
# >>> text.rstrip("be")
# 'to be or not to '
# >>> text. "Натиснути два рази клавішу Tab"
# text.capitalize()   text.isidentifier() text.rfind(        
# text.casefold()     text.islower()      text.rindex(       
# text.center(        text.isnumeric()    text.rjust(        
# text.count(         text.isprintable()  text.rpartition(   
# text.encode(        text.isspace()      text.rsplit(       
# text.endswith(      text.istitle()      text.rstrip(       
# text.expandtabs(    text.isupper()      text.split(        
# text.find(          text.join(          text.splitlines(   
# text.format(        text.ljust(         text.startswith(   
# text.format_map(    text.lower()        text.strip(        
# text.index(         text.lstrip(        text.swapcase()    
# text.isalnum()      text.maketrans(     text.title()       
# text.isalpha()      text.partition(     text.translate(    
# text.isascii()      text.removeprefix(  text.upper()       
# text.isdecimal()    text.removesuffix(  text.zfill(        
# text.isdigit()      text.replace(

# name = "Марія" str
# age = 25  # int
# weight = 60.5  # float
# is_student = True  # bool

# print(name, age, weight, is_student)

# name = "Igor"
# age = 54
# weight = 60.7
# is_student = True

# print(name, age, weight, is_student)

# my_list = ["apple", "banana", "cherry"]
# print(my_list)
# print(my_list[1])
# my_list[1] = "blueberry"
# print(my_list)

# my_list = ["apple", "blueberry", "cherry"]
# my_list.append("orange")
# print(my_list)
# my_list.insert(1, "banana")
# print(my_list)

# languages = ["Python", "Java", "JavaScript"]
# print(languages)
# languages.insert(0, "JavaScript")
# print(languages)
# languages.insert(0, "C++")
# print(languages)
# languages = ["Python", "Java", "JavaScript"]
# print(languages)
# languages.insert(7, "C++")
# print(languages)
# print(languages[3])

# my_list = ["apple", "banana", "blueberry", "cherry", "orange"]
# print(my_list)
# my_list.remove("banana")
# print(my_list)

# languages = ["Python", "Java", "JavaScript"]
# print(languages)
# languages.insert(2, "C++")
# print(languages)
# languages.remove("Java")
# print(languages)
# languages.remove(languages[0])
# print(languages)

# my_dict = {"name": "Олексій", "age": 30}
# print(my_dict["name"])
# print(my_dict["age"])

# language = {"name": "Python", "version": 3.11}
# print(language["name"])
# print(language["version"])

# my_dict = {"name": "Олексій", "age": 30}
# print(my_dict)
# my_dict["age"] = 31
# print(my_dict)

# my_dict = {"name": "Олексій", "age": 31}
# print(my_dict)
# my_dict["email"] = "oleksiy@gmail.com"
# print(my_dict)

# language = {"name": 'Python', "version": 3.11}
# print(language)
# language["year"] = 1991
# print(language)
# language["version"] = 3.12
# print(language)

# my_dict = {"name": "Олексій", "age": 31, "email": "oleksiy@gmail.com"}
# print(my_dict)
# del my_dict["email"]
# print(my_dict)

# my_dict = {"name": "Олексій", "age": 31}

# if my_dict["age"] >= 18:
#     print("Ви повнолітній")

# condition = 0

# if condition == 0:
#     value = 10
# print(value)

# my_dict = {"name": "Андрій", "age": 16}

# if my_dict["age"] >= 18:
#     print("Ви повнолітній")
# else:
#     print("Вибачте, ви ще не маєте права голосу")

# condition = 7

# if condition >= 13:
#     value = 10
# else:
#     value = 20
# print(value)

# my_dict = {"name": "Степан", "age": 65}

# if my_dict["age"] <= 18:
#     print("Вибачте, ви ще не маєте права голосу")
# elif my_dict["age"] >= 65:
#     print("Ви маєте право на пенсію")
# else:
#     print("Ви повнолітній, але ще не маєте права на пенсію")

# condition = 7

# if condition >= 13:
#      value = 10
# elif condition >= 1:
#      value = 15
# else:
#      value = 20
# print(value)

# fruits = ["яблуко", "банан", "вишня"]
# for fruit in fruits:
#     print(fruit)

# languages = ["Python", "Java", "C++", "JavaScript"]
# for language in languages:
#     print(language)

# for letter in "Python":
#     print(letter)

# sentence = "The quick brown fox jumps over the lazy dog"
# length = 0
# for i in sentence:
#     if i != " ":
#         length = length + 1
# print(length)

# for i in range(5):
#     print(i)

# summary = 0
# for i in range(1, 101):
#     summary = summary + i
#     print(i)
#     print(summary)
# print(summary)

# count = 0
# while count < 5:
#     print("Число:", count)
#     count = count + 1

# Додавання x + y
# Віднімання x - y
# Множення x * y
# Ділення x / y
# Піднесення до степеня x ** y

# N = 10
# sum_squares = 0
# i = 1
# while i <= N:
#     sum_squares = sum_squares + i ** 2
#     i = i + 1
# print(i)
# print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")

# def say_hello():
#     print("Привіт, світ!")
# say_hello()

# def function():
#     print("Hello world!")
# function()

# def print_message(message):
#     print(message)

# print_message("Це повідомлення з функції.")

# message = "Hello world!"
# def function(message):
#     print(message)
# function(message)

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print(result)

# N = 10
# def function(N):
#     sum_squares = 0
#     i = 1
#     while i <= N:
#         sum_squares = sum_squares + i * i
#         i = i + 1
#     return(sum_squares)    
# result = function(N)
# print(result)

# my_string = "Привіт, світ!"
# print(my_string)

# first_name = "Олексій"
# last_name = "Гупало"
# full_name = first_name + " " + last_name
# print(full_name)

# first_name = "John"
# last_name = "Doe"
# def get_fullname(first_name, last_name):
#     full_name = first_name + " " + last_name
#     return(full_name)
# full_name = get_fullname(first_name, last_name)
# print(full_name)

# first_name = "John"
# last_name = "Doe"
# def get_fullname(first_name, last_name):
#     fullname = first_name + " " + last_name
#     return(fullname)
# fullname = get_fullname(first_name, last_name)
# print(fullname)

# first_name = "Олексій"
# last_name = "Гупало"
# full_name = first_name + " " + last_name
# print(len(full_name))

# first_name = "Олексій"
# last_name = "Гупало"
# full_name = first_name + " " + last_name
# length = len(full_name)
# print(full_name[0])
# print(full_name[length - 1])

# first_name = "John"
# last_name = "Doe"
# def get_initials(first_name, last_name):
#     l = len(first_name)
#     f_name = first_name[0] + "."
#     formatted_name = last_name + " " + f_name
#     return(formatted_name)
# formatted_name = get_initials(first_name, last_name)
# print(formatted_name)

# first = "Python"
# second = "python"
# def compare(first, second):
#     first_st = first.upper()
#     second_st = second.upper()
#     result = first_st == second_st
#     return(result)
# result = compare(first, second)
# print(result)

# text = "Hello, world!"
# print(text.find("world")) 
# print(text.find("Python"))

# text = "I like cats"
# new_text = text.replace("cats", "dogs")
# print(new_text)

# text = "Hello, world! Welcome to the world of Python."
# position = text.find("world")
# print(position)
# updated_text = text.replace("world", "planet")
# print(updated_text)

# name = "Олексій"
# age = 30
# greeting = f"Мене звати {name}, і мені {age} років."
# print(greeting)

# product_name = "Coffee Maker"
# product_price = 7500.50
# product_quantity = 15

# def format_product_info(product_name, product_price, product_quantity):
#     product_info = f"Product: {product_name}, Price: {product_price} UAH, Quantity: {product_quantity} pcs."
#     return(product_info)

# product_info = format_product_info(product_name, product_price, product_quantity)
# print(product_info)

# class Car:
#     vehicle_type = "Automobile"
    
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# class Dog:
#     # Атрибут класу
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Метод екземпляру
#     def description(self):
#         return f"{self.name} є {self.age} років."

#     # Інший метод екземпляру
#     def speak(self, sound):
#         return f"{self.name} каже {sound}"

# Атрибут класу
# species = "Canis familiaris"

# def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # Метод екземпляру
# def description(self):
#     return f"{self.name} є {self.age} років."

# # Інший метод екземпляру
# def speak(self, sound):
#     return f"{self.name} каже {sound}"
# print(speak)

# class Car:
#     vehicle_type = "Automobile"

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_info(self):
#         return f"{self.year} {self.make} {self.model}, Type: {self.vehicle_type}"

# class Car:
#     vehicle_type = "Automobile"

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_info(self):
#         return f"{self.year} {self.make} {self.model}, Type: {Car.vehicle_type}"

# car_ford = Car("Ford", "Mustang", 2022)
# car_toyota = Car("Toyota", "Corolla", 2021)

# print(car_ford.get_info())
# print(car_toyota.get_info())

# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# result = add_numbers(5, 10)
# print(result)  # Виведе: 15

# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!

# def is_even(num: int) -> bool:
#     return num % 2 == 0

# check_even = is_even(5)
# print(check_even)  # Виведе: True

# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал

# def modify_list(lst: list) -> None:
#     lst.append(7)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]

# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(4)
#     print(lst)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)
#     return codes
# result = string_to_codes("Hello world!")
# print(result)

# x = 50

# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50

# def func_outer():
#     x = 2
#     print(x)

#     def func_inner():
#         # nonlocal x
#         x = 5
#         print(x)

#     func_inner()
#     return x

# result = func_outer()  # 5
# print(result)

# x = 50

# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x)# Значення x складає 2

# age = 10
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# num = 5  # приклад значення для num

# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")

# x = int(input('Введіть число: '))

# if x % 2 == 0:
#     print("Число x є парним.")
# else:
#     print("Число x є непарним.")

# a = input('Введіть число')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print('Це число - нуль')

# a = input('Введіть число')
# a = int(a)

# if a > 0:
#     print('Число додатне')
# elif a == 1:
#     print('Число дорівнює 1')
# else:
#     print("a <= 0")

# money = 33
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True
# print(a is c)  # False

# num = int(input("Введіть число: "))

# length = len(str(num))

# if length == 2 and num % 2 == 0:
#     print("Парне двозначне число")
# else:
#     print("Ні")

# num = int(input("Введіть число: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#         print("Buzz")
# else: print(num)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

# result = y / x
# print(result)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

#     if x == 0:
#         print("X can`t be equal to zero")
#         x = int(input("X: "))

#         if x == 0:
#             print("X can`t be equal to zero")
#             x = int(input("X: "))

# result = y / x
# print(result)

# В цьому прикладі тричі повторюється перевірка на нерівність x нулю,
# і на кожну перевірку блок інструкцій виділяється додатковими 4-ма пробілами.
# Сенсу в додаткових перевірках немає, це зроблено тільки заради демонстрації.

# Наведемо наступний приклад вкладеності для визначення
# чвертей для координатної площини,
# щоб закріпити розуміння блоку інструкцій.
# Даний фрагмент коду реалізує визначення квадранту точки
# з координатами x та y на координатній площині:

# x = int(input("X: "))
# y = int(input("Y: "))

# if x >= 0:
#     if y >= 0:  # x > 0, y > 0
#         print("Перша чверть")
#     else:  # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:  # x < 0, y > 0
#         print("Друга чверть")
#     else:  # x < 0, y < 0
#         print("Третя чверть")

# Тернарні оператори в Python:
# is_nice = True
# state = "nice" if is_nice else "not nice"
# print(state)

# some_data = None
# msg = some_data or "Не було повернено даних"
# print(msg)

# some_data = None
# if some_data:
#     msg = some_data
# else:
#     msg = "Не було повернено даних"

# x = int(input("X: "))

# match x:
#     case _ if x > 0:
#         print(f"{x} - positive number")
#     case _ if x < 0:
#         print(f"{x} - negative number")
#     case 0:
#         print(f"{x} - zero")

# name = "Ігор"
# age = 54
# print(name)
# print(age)

# rate = 1.68
# value = int(50)
# payment = rate * value
# print(payment)

# rate = 1.68
# value_day = 5
# value_night = 10
# payment = rate * (value_day + 0.5 * value_night)
# print(payment)

# first_name = "Igor"
# last_name = "Danyliuk"
# print(first_name + " " + last_name)

# length = 2.75
# width = 1.75
# area = length * width
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# print(show)

# is_active = True
# is_delete = False
# print(is_active)
# print(is_delete)

# name = "Maxim"
# age = 34
# is_active = True
# subscription = None
# print(f"{name}, {age}, {is_active}, {subscription}")

# length = "2.75"
# width = "1.75"
# length_float = float(length)
# width_float = float(width)
# area = width_float * length_float
# show = f"With width {width_float} and length {length_float} of the room, its area is equal to {area}"
# print(show)

# name = input("Your name? ")
# email = input("Your email? ")
# age = int(input("Your age?"))
# height = float(input("Your height? "))
# is_active = input("Do You wish to receive news from the site? (yes/no): ") != ""
# print(name, email, age, height, is_active)

print("Hi ", end="")
print("there!")


