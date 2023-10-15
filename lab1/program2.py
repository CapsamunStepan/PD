print('Общество в начале XXI века')
age = int(input('Введите свой возраст: '))

if age in range(0, 7):
    print("Вам в детский сад")
elif age in range(7, 18):
    print("Вам в школу")
elif age in range(18, 25):
    print("Вам в профессиональное учебное заведение")
elif age in range(25, 60):
    print("Вам на работу")
elif age in range(60, 120):
    print("Вам предоставляется выбор")
else:
    for i in range(5):
        print("Ошибка! Это программа для людей!")