# def add(number1,number2,number3):
#     # number1 = num1 (1)
#     # number2 = num2 (2)
#     # number3 = num3 (3)
#     print(number1+number2+number3)
#
#
# def greetings(name:str,last_name:str):
#     return f'Hello,{name} {last_name},U r welcome!'
#
# def get_types(var1,var2,var3):
#     return type(var1),type(var2),type(var3)
#
# def calculate(num1:int,num2:int,sign:str):
#     if sign == "+":
#         print(num1+num2)
#     elif sign == "-":
#         print(num1-num2)
#     elif sign == "*":
#         print(num1*num2)
#     elif sign == "//":
#         print(num1 // num2)
#     else:
#         print('вы вели не тот символ')
# calculate(5,5,"+")
# calculate(7,2,"-")
# calculate(9,9,"*")
# calculate(10,2,"//")
#
#
#
# def mult(number1,number2):
#     result = number1*number2
#     return result
#
#
#
#
#
#
#
#
#
#
# def register(username,email,password,check_password):
#     if password == check_password:
#        if 8<len(username)>40:
#            if 8<len(password)>16:
#                print('Регистрация')
#            else:
#                print('Пароль слишком короткий!')
#        else:
#            print('Слишком короткое имя')
#     else:
#         print('Предоставлены наверные данные!')
#
#
#
# username1 = 'lalaland123'
# email1 = 'superuser@gmail.com'
# password1 = '123456789'
#
# def auth(user_input,password):
#     if username1 == user_input and password1 == password or user_input == email1 and password == password1:
#         print('Добро пожаловать!',user_input)
#     else:
#         print('Неверный пароль')
#
# auth('superuser@gmail.com','123456789')
#
#
# def coord(x,y):
#     if x > 0:
#         if y > 0:
#              print(1)
#         else:
#             print(4)
#     elif y > 0:
#         if x < 0:
#             print(2)
#     elif y < 0:
#         print(3)
#     else:
#         print(0)
# coord(0,0)


# list1 = ['bread','milk', 'potato','tomato','smetana']
# print(list1)
#
# list1.append('ogurci')
#
# print(list1)
#
# list1.append('meat')
#
# print(list1)


import random

# number = random.sample([0,1,2,3,4,5,6,7,8,9],7)
# number.sort()
# print(number)
#
#
# mama_input = input('Мама говорит')
#
# if mama_input in list1:
#     print('Уже есть')
# else:
#     list.append(mama_input)
#     print(list1,'Хорошо куплю')

# list1 = ['petya','vasya','asdd',0,'petya',0,0,0,'daf','ytw','asdv',0,0,'almaz','mira']
# list2 = []
# i = 0
#
#
# while i < len(list1):
#     if list1[i] != 0:
#         list2.append(list1[i])
#     i += 1
# print(list1)
# print(list2)

# username ='superuser'
# password = 'gremory'
#
# rock_list = ['asdfasd','123123','superuser','asdfsad','gremory']
#
# j = 0
# i = 0
#
# while i < len(rock_list):
#
#     if rock_list[i] == username or rock_list[i] == password:
#         j += 1
#         if j == 2:
#             print(rock_list[i])
#     i += 1
#
#
# list1 = [1,2,3,4,1,2,7,8,10,11,1,13,7]
# list2 = [] # Уникальные элементы
#
# i = 0
# while i < len(list1):
#     count_i = list1.count(list1[i])
#     if count_i == 1:
#         list2.append(list1[i])
#     i += 1
# print(list1)
# print(list2)


# 1
# num1 = int(input('Please input the first number: '))
# num2 = int(input('Please input the second number: '))
# if num1 < num2:
#     print(num1)
# else:
#     print(num2)

# 4
# num1 = int(input("First: "))
# num2 = int(input("Second: "))
# num3 = int(input("Third: "))
# if num1 <= num2 and num1 <= num3:
#     print(num1)
# if num2 <= num1 and num2 <= num3:
#     print(num2)
# if num3 <= num1 and num3 <= num2:
#     print(num3)


list1 = ['yuan','som','dollar','euro','ruble','lira','tenge']
list2 = []
result = 0
i = 0
while i < len(list1):
    if i % 2 == 0:
        list2.append(list1[i])
    i += 1
print(list2)


# #5
# a,b,c =1,2,3
#
# if a == b and a == c:
#     print(3)
# elif a == b and a != c or a == c and a != b:
#     print(2)
# else:
#     print(1)

# 6
# a,b,c = 3,3,3
#
# if a > b:
#     a,b = b,a
# if b > c:
#     b,c = c,b
# if a > b:
#     a,b = b,a
# print(a,b,c)

# bd_username = 'testuser'
# bd_password = 'testpassword'
#
# def auth(tries:int):
#     count = 0
#     while count < tries:
#         username = input("Введите имя польователя: ")
#         password = input ("Введите пароль: ")
#         if username == bd_username and password == bd_password:
#             print("Добро пожаловать!")
#             break
#         else:
#             print('Ввели неверные данные!Попробуйте еще раз!')
#             count += 1
# auth(3)


# def register_to_bd(username,password,check_password):
#     if password == check_password:
#         file1 = open('datebase.txt','w')
#         result = username + '\n' + password
#         file1.write(result)
#
# register_to_bd('asdasd','123','123')


# file1 = open('datebase.txt')
# list1 = file1.readlines()
# my_input = input('Я хочу: ')
# if my_input in list1:
#     print('В наличий')
# else:
#      print('Нет в наличий!На складке!')

# with open('datebase.txt') as file1:
#     ban = 'ban_word' + '\n'
#     check_ban = ''
#     streamer_words = file1.readlines()
#     i = 0
#
#     while i < len(streamer_words):
#         if streamer_words[i] == ban:
#             check_ban = streamer_words[i]
#             print(streamer_words[i], streamer_words.index(streamer_words[i]) + 1)
#
#         i += 1
#
#     if check_ban in streamer_words:
#         print('Найдено')
#     else:
#         print('OK')

# spisok = [1,2,3,4,5,6]
#
# print(spisok[1:6:2])