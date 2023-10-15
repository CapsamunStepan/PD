x = input('Введите число от 1 до 9: ')
try:
    x = int(x)
except ValueError:
    print('Вы не ввели число!')

if x in range(1, 4):
    s = input('Введите строку: ')
    n = int(input('Введите число повторений: '))
    for i in range(n):
        print(s)
elif x in range(4, 7):
    m = int(input('Введите степень в которое хотите возвести число: '))
    print(f'Вы возвели число {x} в степень {m} и получили {x ** m}')
elif x in range(7, 10):
    for i in range(10):
        print(x)
        x += 1
else:
    print('Ошибка ввода!!!')

