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

# print("Hi ", end="")
# print("there!")

# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")
# name1 = input("Input Your name? please: ")
# greet(name1)

# def greet(name, age, message="Привіт"):
#     print(f"{message}, {name}! You are {age} years old.")

# name1 = input("Input your name: ")
# age1 = int(input("Input your age: "))

# greet(name1, age1)

# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)

# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)

# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)

# def real_cost(base: int, discount: float = 0) -> float:
#     return base * (1 - discount)

# def greet(name: str) -> float:
#     print(f"Hello, {name}")
# greet("RRR")

# def print_all_args(*args):
#     for arg in args:
#         print(arg)

# print_all_args(1, 'hello', True)

# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))

# def concatenate(*strings) -> str:
#     result = ""
#     for arg in strings:
#         result += arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=25)

# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(7)) # виведе 120

# def fibonacci(n):
#     if n <= 1: # базовий випадок
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

# print(fibonacci(10)) # виведе 55

# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1:
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"

# num = int(input("Enter integer number: "))

# if num > 0:
#     if num % 2 != 0:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num > 0:
#     sum = sum + num
#     num = num - 1
# print(sum)

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == search:
#         result += 1
# print(result)

# my_list = []
# my_list.insert(0, 2024)
# my_list.append("Python")
# my_list.insert(2, 3.12)
# print(f"{my_list[0]}, {my_list[1]}, {my_list[2]}")

# my_list.extend(some_data)
# my_list.insert(1, "Python")
# my_list.reverse()
# print(my_list)

# data = {}
# data["year"] = 2024
# data["lang"] = "Python"
# data["version"] = 3.12
# print(data)

# cat = {}
# info = {"status": "vaccinated", "breed": True}
# cat["nick"] = "Simon"
# cat["age"] = 7
# cat["characteristics"] = ["лагідний","кусається"]
# age: int
# age = cat["age"]
# print(age) 
# cat.update(info)
# print(cat)

# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
# except ZeroDivisionError:
#     print('Divide by zero completed!')
# print(f"Size of SMS pack is {chunk}")

# def greeting():
#     print("Hello world!")
# print(greeting())

# def invite_to_event():
#     username = input("Please? input Your USERNAME: ")
#     print(f"Dear {username}, we have the honour to invite you to our event")
# invite_to_event()

# username = input("Please input Your USERNAME: ")
# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"
# invite_to_event(username)

# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"

# def discount_price(price, discount: float):
#     def apply_discount():
#         return price * (1 - discount)

#     return apply_discount()

# print(discount_price(10, 0.2))

# def get_fullname(first_name, last_name, middle_name = ""):
#     if middle_name == "":
#         print(f"{first_name} {last_name}")
#     else:
#         print(f"{first_name} {middle_name} {last_name}")
# get_fullname("Igor", "Danylyuk", "Andriyovych")

# def get_fullname(first_name, last_name, middle_name = ""):
#     if middle_name == "":
#         print(f"{first_name} {last_name}")
#     else:
#         print(f"{first_name} {middle_name} {last_name}")
# first = input("Please input Your First Name: ")
# last = input("Please input Your Last Name: ")
# middle = input("Please input Your Middle Name: ")
# get_fullname(first, last, middle)

# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name == "":
#         return f"{first_name} {last_name}"
#     return f"{first_name} {middle_name} {last_name}"

# def format_string(string:str,length:int):
#     if len(string) < length:
#         indent = (length - len(string)) // 2
#         string = " " * indent + string + " " * indent
#     print(string)
#     return string
# # s = input("Input word: ")
# format_string("abba", 15)

# def format_string(string:str,length:int):
#     if len(string) < length:
#         indent = (length - len(string)) // 2
#         string = " " * indent + string
#     return string

# def first(size, *args):
#     return size + len(args)


# def second(size, **kwargs):
#     return size + len(kwargs)

# print(first(5, "first", "second", "third"))  
# print(first(1, "Alex", "Boris"))             
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))

# import datetime
# now = datetime.datetime.now()
# print(now)

# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)

# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())



# import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"


# import datetime

# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7)

# print(specific_date)  # Виведе "2020-01-07 00:00:00"


# import datetime

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

# import datetime

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)

# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання номера дня тижня
# day_of_week = now.weekday()

# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")  


# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2


import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)

# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())

import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# import datetime

# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7)

# print(specific_date)  # Виведе "2020-01-07 00:00:00"

# import datetime

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

# import datetime

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)

# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання номера дня тижня
# day_of_week = now.weekday()

# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")  

# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0

# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(now)
# print(future_date)

# from datetime import datetime, timedelta

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020)
# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

# from datetime import datetime

# # Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")

# from datetime import datetime

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)
# days_since = current_date - napoleon_burns_moscow
# print(days_since)

# from datetime import datetime

# # Поточний час
# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу
# print(now.toordinal())

# from datetime import datetime

# # Припустимо, є timestamp
# timestamp = 1617183600

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)  # Виведе відповідний datetime

# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)

# from datetime import datetime

# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)

# from datetime import datetime

# iso_date_string = "2023-03-14T12:39:29.992996"

# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()

# print(f"Сьогодні: {day_of_week} ISO format")  # Поверне число від 1 до 7, що відповідає дню тижня
# print(f"Сьогодні: {now.weekday()} usual format")

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# import time
# current_time = time.ctime()
# print(current_time)
# print("Початок паузи")

# time.sleep(5)
# current_time = time.ctime()
# print(current_time)
# print("Кінець паузи")

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")

# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")

# import time

# # Записуємо час на початку виконання
# start_time = time.perf_counter()

# # Виконуємо якусь операцію
# for _ in range(1_000_000):
#     pass  # Просто проходить цикл мільйон разів

# # Записуємо час після виконання операції
# end_time = time.perf_counter()

# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time} секунд")

# import random

# dice_roll = random.randint(1, 6)
# print(f"Ви кинули {dice_roll}")

# import random

# num = random.random()
# print(num)

# import random

# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")

# import random
# print(random.randrange(10))  # Верхня межа є 10, але не включається

# import random

# target = random.randrange(1, 11, 2)
# print(f"Ціль: {target}")

# import random

# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

# random.shuffle(cards)

# print(f"Перемішана колода: {cards}")

# import random

# fruits = ['apple', 'banana', 'orange']
# print(random.choice(fruits))

# import math

# # Вихідне число
# x = 3.7

# # Використання різних методів округлення
# ceil_result = math.ceil(x)  # Округлення вгору
# floor_result = math.floor(x)  # Округлення вниз
# trunc_result = math.trunc(x)  # Відсікання дробової частини

# print(ceil_result, floor_result, trunc_result)

# import math

# # Використання констант
# print(math.pi)  # Виведе приблизне значення π

# # Тригонометрія
# angle = math.radians(60)  # Конвертація з градусів у радіани
# print(math.sin(angle))  # Синус кута

# # Корінь числа
# print(math.sqrt(9))  # Квадратний корінь з 9

# # Логарифми
# print(math.log(10, 2))  # Логарифм 10 за основою 2

# print(0.1 + 0.2 == 0.3)  # Це повертає False
# print(0.1 + 0.2)

# import math

# r = math.isclose(0.1 + 0.2, 0.3)
# print(r)  # Це поверне True

# import math

# r = math.isclose(0.1, 0.10000000009)
# print(r)  # Це поверне True

# this_is_string = "Hi there!"

# the_same_string = 'Hi there!'

# this_is_string == the_same_string# True
# print(this_is_string == the_same_string)

# text = """This is first line
# And second line
# Last third line"""

# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# print(text)
# print(song)

# ("spam " "eggs") == "spam eggs"
# print(("spam " "eggs") == "spam eggs")

# one_line_text = ("Textual data in Python is handled with str objects,"
#                 " or strings. Strings are immutable sequences of Unicode"
#                 " code points. String literals are written in a variety "
#                 " of ways: single quotes, double quotes, triple quoted.")
# print(one_line_text)

# query = ("SELECT * "
#          "FROM some_table "
#          "WHERE condition1 = True "
#          "AND condition2 = False")
# print(query)

# query = ("SELECT * "
#          "FROM some_table "
#          "WHERE condition1 = True "
#          "AND condition2 = False")

# Спеціальні символи Python
# https://uk.wikipedia.org/wiki/%D0%9A%D0%B5%D1%80%D1%83%D0%B2%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0_%D0%BF%D0%BE%D1%81%D0%BB%D1%96%D0%B4%D0%BE%D0%B2%D0%BD%D1%96%D1%81%D1%82%D1%8C

# print("Hello\nWorld")

# print("Hello\tWorld")

# print("Hello my little\rsister")

# print("Hello\bWorld")

# print("Hello\\World")

# print('It\'s a beautiful day')
# print("He said, \"Hello\"")

# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5
# print(s.find("q")) # -1

# s = 'Some words'

# print(s.find("o"))
# print(s.rfind('o'))

s = 'Some words'

# print(s.find("q"))
# print(s.rindex('o'))

# text = 'hello world'
# result = text.split()
# print(result)  # Виведе: ['hello', 'world']

# text = "apple,banana,cherry"
# result = text.split(',')
# print(result)  # Виведе: ['apple', 'banana', 'cherry']

# list_of_strings = ['Hello', 'world']
# result = ' '.join(list_of_strings)
# print(result)  # Виведе: 'Hello world'

# elements = ['earth', 'air', 'fire', 'water']
# result = ', '.join(elements)
# print(result)  # Виведе: 'earth, air, fire, water'

# print('   spacious   ')
# clean = '   spacious   '.strip()
# print(clean) # spacious

# text = "Hello world"
# print(text)
# new_text = text.replace("world", "Python")
# print(new_text) 

# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace("fish", "bird", 2)
# print(new_text)

# text = "Hello, world!"
# new_text = text.replace(" world", "")
# print(new_text)

# print('TestHook'.removeprefix('Test')) # Hook
# print('TestHook'.removeprefix('Hook')) # TestHook

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)

# number = "12345"
# print(number.isdigit())  # Виведе: True

# text = "Number123"
# print(text.isdigit())  # Виведе: False

# user_input = input("Введіть число: ")
# if user_input.isdigit():
#     print("Це дійсно число!")
# else:
#     print("Це не число!")

# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")

# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# str = "This is string example"
# print(str.translate(trantab))

# intab = "aeiou"
# trantab = str.maketrans('', '', intab)

# str = "This is string example"
# print(str.translate(trantab))

# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# result = zip(a, b)
# print(list(result))

# names = ["Anna", "Oleh", "Ihor"]
# scores = [90, 85, 78]

# for name, score in zip(names, scores):
#     print(name, score)

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)

morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v

# string = "Hello world"

# result = ""

# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}

# # Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v

# string = "Hello world"

# result = ""

# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)

# Наприклад, вивести числа від 0 до 7 в десятковому, шістнадцятковому,
# вісімковому і двійковому представленні можна наступним чином:
# for i in range(8):
#     s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
#     print(s)

# price = 19.99
# quantity = 3
# total = f"Total: {price * quantity:.2f}"
# print(total)



# <: Вирівнювання вмісту по лівому краю.
# >: Вирівнювання вмісту по правому краю.
# ^: Вирівнювання вмісту по центру.
# =: Використовується для вирівнювання чисел, 
# при цьому знак (якщо він є) відображається зліва, 
# а число - по правому краю поля.
# width = 5
# for num in range(12):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')

# name = "Alice"
# formatted = f"{name:>10}"
# print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)

# completion = 0.756
# formatted = f"{completion:.1%}"
# print(formatted)  # Виведе: '75.6%'

# progress = 0.5
# formatted = f"{progress:.0%}"
# print(formatted)

# В Python вбудована своя міні-мова форматування рядків: 
# https://docs.python.org/3/library/string.html#format-specification-mini-language

# import re

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match.group())
# else:
#     print("Не знайдено.")

# import re

# text = "Вивчення Python може бути веселим."
# pattern = r"в\w*м"
# match = re.search(pattern, text, re.IGNORECASE)

# if match:
#     print("Знайдено:", match.group())

# import re

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())

# import re

# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)

# import re

# text = "Рік 2023 був складнішим, ніж 2022"
# print(text)
# pattern = r"\d+"
# matches = re.findall(pattern, text)

# print(matches)

# import re

# text = "Python - це проста, але потужна мова програмування."
# print(text)
# pattern = r"\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе список всіх слів у рядку

# import re

# text = "Контакти: example1@example.com, example2@sample.org"
# print(text)
# pattern = r"\w+@\w+\.\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе всі знайдені електронні адреси

# import re

# file_name = "Мій документ Python.txt"
# print(file_name)
# pattern = r"\s"
# replacement = "_"
# formatted_name = re.sub(pattern, replacement, file_name)

# print(formatted_name)

# import re

# text = "Python - потужна, універсальна; мова!"
# print(text)
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)

# print(modified_text)  

# import re

# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# print(formatted_phone)

# import re

# text = "Python - це проста, але потужна мова програмування."
# print(text)
# pattern = r"\s+"
# words = re.split(pattern, text)

# print(words)  # Виведе список слів у рядку

# import re

# text = "Python - потужна; проста, універсальна: мова!"
# print(text)
# pattern = r"[;,\-:!\s]+"
# elements = re.split(pattern, text)

# print(elements)  # Виведе список частин, розділених пунктуацією
# print(elements[:-1:])

# # Результат роботи коду:
# # ['Python', 'потужна', 'проста', 'універсальна', 'мова', '']
# # ['Python', 'потужна', 'проста', 'універсальна', 'мова']

# import re

# text = "apple#banana!mango@orange;kiwi"
# pattern = r"[#@;!]"
# fruits = re.split(pattern, text)

# print(fruits)

