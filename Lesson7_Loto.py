#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random

class CreateCard:
    def __init__(self, name, ai):
        self.list2 = []
        self.dic1 = [[],    #лист хранящий числовые карты
                 [],
                 []]
        self.name = name
        self.pr_dic = [[],  #лист для вывода данных на экран
                  [],
                  []]
        self.count_num = 0
        self.ai = ai
        self.win = ''
    def load_2(self):
        for i in range(90):
            self.list2.append(i+1)
            # print(i+1)
        j = 0
        for j in range(3):
            check_dec = []
            while len(check_dec) < 5:
                num_in_card = random.sample(self.list2, 5)
                num_in_card.sort()
                check_dec = list(map(lambda x: x // 10, num_in_card))
                check_dec = sorted(set(check_dec))

            self.list2 = [b for b in self.list2 if b not in num_in_card]
            # del_from_bag(self.list2, num_in_card)
            # print('new:', list2)
            self.dic1[j] = num_in_card
            j += 1

        print(f'------ {self.name} карточка -----')
        c = 0
        for k in self.dic1:
            line = ''
            line_dic = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
            for p in k:
                ind = 8 if p // 10 == 9 else p // 10
                line_dic[ind] = str(p).rjust(3, ' ')
            for key, val in line_dic.items():
                if val == '':
                    line_dic[key] = '   '
            for key, val in line_dic.items():
                line += val
            self.pr_dic[c] = line_dic
            c += 1
            print(line)

    def has_number_in_card(self, barrel):
        dn = 0 #dic num
        check1 = ''
        check2 = 0
        if self.ai == False:
            check1 = input('Боченок есть на карточке? (y/n)')
        for x in self.dic1:
            for q in x:
                if q == barrel[0]:
                    self.pr_dic[dn][8 if q // 10 == 9 else q // 10] = ' --'
                    self.count_num += 1
                    check2 = 1
                    break
            dn += 1
        # print(f'AI: {self.ai} check2 {check2} check1 {check1}')
        if self.ai == False and check2 == 1 and check1 != 'y':
            print('Ты проиграл!!!')
            self.count_num = 15
            self.win = False
        elif self.ai == False and check2 == 0 and check1 == 'y':
            print('Ты проиграл!!!')
            self.count_num = 15
            self.win = False
        line = ''
        print(f'~~~~~~~ {self.name} карточка ~~~~~~~')
        for k in self.pr_dic:
            # print(k)
            # c = 0
            for j in k:
                line += k[j]
            line = line + '\n'
        print(line)

class Player(CreateCard):
    pass

class Computer(CreateCard):
    pass


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.bag = []

    def load_bag(self):
        for i in range(90):
            self.bag.append(i+1)
        print(f'В мешке: {len(self.bag)} бочонков')

    def start_game(self):
        # while True:
        while len(self.bag) > 0:
            barrel = random.sample(self.bag, 1)
            self.bag = [b for b in self.bag if b not in barrel]
            print(f'------ Боченок --> {barrel[0]} <-- Осталось в мешке {len(self.bag)} -----')
            if self.player.win != False and self.computer.win != False:
                self.player.has_number_in_card(barrel)
                self.computer.has_number_in_card(barrel)
            else:
                break
            if self.player.count_num == 15 and self.player.win != False:
                print(f'{self.player.name} выиграл ')
                break
            if self.computer.count_num == 15 and self.computer.win != False:
                print(f'{self.computer.name} выиграл ')
                break

player = Player('Tom', True)
computer = Computer('Jerry', False)

player.load_2()
computer.load_2()

game = Game(player, computer)
game.load_bag()
game.start_game()




