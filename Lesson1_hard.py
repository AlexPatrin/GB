# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.

# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

#   -----------------------Medical

name = input('Имя: ')
surname = input('Фамилия: ')
age = int(input('Возраст: '))
weight = int(input('Вес: '))

# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
if age < 30:
    if weight >= 50:
        if weight < 120:
            print('Ваше состояние хорошее')
    else:
        print('Ваше состояние не очень')
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
elif age >= 30:
    if age < 40:
        if weight < 50:
            print('Требуется начать вести правильный образ жизни')
        elif weight >= 120:
            print('Требуется начать вести правильный образ жизни')
        else:
            print('Ваше состояние хорошее')
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
    elif age >= 40:
        if weight < 50:
            print('Требуется врачебный осмотр')
        elif weight >= 120:
            print('Требуется врачебный осмотр')
        else:
            print('Ваше состояние хорошее')
