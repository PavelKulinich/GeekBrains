# coding : utf-8

# __author__ = 'Кулинич П.В.'

# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

# код пишем тут...

print('*****Первая задача:*****')
input('Нажмите любую клавишу, чтобы начать')

chislo = input('Введите произвольное число: ')
i = 0
while i<len(chislo):
    print(chislo[i])
    i+=1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print('*****Вторая задача:*****')
input('Нажмите любую клавишу, чтобы начать')

a = input('Введите значение переменной a: ')
b = input('Ыыедите значение переменной b: ')
print('Меняем значения переменных местами...')
tmp = a
a = b
b = tmp
print('Текущее значение переменной a: ',a)
print('Текущее значение переменной b: ',b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print('*****Третья задача:*****')
input('Нажмите любую клавишу, чтобы начать')
age = int(input('Введите Ваш возраст: '))
if age < 18:
    print('Извините, пользование данным ресурсом только с 18 лет')
else:
        print('Доступ разрешен')