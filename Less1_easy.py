# Задача-1: поработайте с переменными, создайте несколько,
a = 10
b = 'privet'
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
print(a)
print(b)
c = input()
print(c)

# Задача-2: Запросите от пользователя число, сохраните в переменную,
d = int(input('Input number: '))
# прибавьте к числу 2 и выведите результат на экран.
d += 2
print(d)

# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
ag = int(input('Enter your age: '))
if ag >= 18:
    print("Доступ разрешен")
# иначе "Извините, пользование данным ресурсом только с 18 лет"
else:
    print("Извините, пользование данным ресурсом только с 18 лет")