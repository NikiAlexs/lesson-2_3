# name = input("Enter your name")
# if 5 > 1:
#    print('ok')
# import this
# ctr+alt+L ===> исправление ошибок в коде связанных с отсутствием пробелов

# Цикл While
# while 1 > 0:
#   number = int(input('Введите число: '))
#    if number % 2 == 0:
#       print('Число четное')
#    else:
#        print('Число нечетное')
#        break #останавливает цикл / continue - останавливает цикл после выполнения
#        # одного условия и запускает цикл заново
# print('Цикл отключен')

# Домашняя работа по уроку "Стиль кода часть II. Цикл While
my_list = [42, 69, 322, 13, 15, 0, 99, -5, 9, 8, 7, -6, 5]
#print(len(my_list))
a = 0
while a < len(my_list):
    if my_list[a] > 0:
        print(my_list[a])
        a = a + 1
    elif my_list[a] == 0:
        a = a + 1
    else:
        break