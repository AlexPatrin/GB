# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player = {'name': input('Player: '), 'health': 200, 'damage': 50, 'armor': 1.2}
enemy = {'name': input('Enemy: '), 'health': 150, 'damage': 80, 'armor': 1.6}

def attack(person1, person2):
    person2['health'] -= person1['damage']
    return person1, person2

attack(player, enemy)
print(enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
def attack_armor(person1, person2):
    loss = float(person1['damage'])/float(person2['armor'])
    return loss
print('Loss: ', attack_armor(player, enemy))

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
file_names = []
def save_file(*args):
    for arg in args:
        name = arg['name']
        with open(f'{name}.txt', 'w') as file:
            for key, val in arg.items():
                file.write(f'{key}:{val}\n')
        file_names.append(name)
save_file(player, enemy)
print(file_names)

# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
gm = {}
tg = {}
def load_profile(*args):
    j = 0
    for fn in file_names:
        with open(f'{fn}.txt', 'r') as file2:
            for i in file2.readlines():
                key, val = i.strip().split(':')
                if j == 0:
                    gm[key] = val
                elif j == 1:
                    tg[key] = val
            j+=1

load_profile(file_names)
print('gm: ', gm)
print('tg', tg)
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,


k = 1
if input('Run battle? (y/n)') == 'y':
    while float(tg['health']) > 0 and float(gm['health']) > 0:
        tg['health'] = str(float(tg['health']) - attack_armor(gm, tg))
        print(f'Round {k}\n {gm}\n {tg}\n')
        gm, tg = tg, gm
        k += 1
    print('Win', tg['name'], 'with', tg['health'])
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

