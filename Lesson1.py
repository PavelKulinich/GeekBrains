# Задание первое. Работа с переменными
a = 5
b = 10
print(a+b)
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(f'Введенное число a:{a}')
print(f'Введенное число b:{b}')

# Задание второе.
sec = int(input('Введите время в секундах: '))
hours = sec // 3600
minutes = (sec // 60)-(hours*60)
seconds = sec % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

# Задание третье
n = input('Ввдедите число n: ')
nn = n+n
nnn = n+n+n
print(f'n:{n},nn:{nn},nnn:{nnn}')
result = int(n)+int(nn)+int(nnn)
print(result)

# Задание четвертое
n = int(input('Введите целое положительное число: '))

if int(n) > 0:
    max_digit = n % 10
    if max_digit == 9:
        print(f'Максимальное цифра в числе {n} - {max_digit}')
    else:
        num = n // 10
        while num > 0:
            last_digit_num = num % 10
            if last_digit_num > max_digit:
                max_digit = last_digit_num
            elif last_digit_num == 9:
                max_digit = last_digit_num
                break
            else:
                num = num // 10
        print(f'Максимальное цифра в числе {n} - {max_digit}')
else:
    print('Необходимо ввести целое положительное число')

# Задание пятое
rev = int(input('Введите выручку компании: '))
exp = int(input('Введите расходы компании: '))

if rev > exp:
    print(f'Ваша компания работает с прибылью. Прибыль составила: {rev-exp}. Рентабельность: {(rev-exp)/rev*100}%')
    chisl = int(input('Введите численность сотрудников компании: '))
    print(f'Прибыль на одного сотрудника - {(rev-exp)/chisl}')
elif rev < exp:
    print(f'Ваша компания работает в убыток. Убыток составил: {exp - rev}')
else:
    print(f'Нулевой баланс')

# Задание шестое
a = int(input('Введите результат первого дня: '))
b = int(input('Введите целевой результат : '))
days = 1
while True:
    a = a+(a*10/100)
    print(f'День: {days}, результат: {a:.2f}')
    if a >= b:
        print(f'Результат достигнут на день {days}')
        break
    else:
        days += 1






