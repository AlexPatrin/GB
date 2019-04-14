# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.

class Person:
    def __init__(self, name, attack, health, armor):
        self.name = str(name)
        self.attack = attack
        self.health = health
        self.armor = armor

    def calc_attack(self, player):
        attack = self.attack / player.armor
        player._calc_damage(attack)

    def _calc_damage(self, attack):
        self.health -= int(attack)
        print(f'{self.name} HP: {self.health}')

# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Player(Person):
    pass

class Enemy(Person):
    pass

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def battle(self):
        i = 0
        while True:
            i += 1
            print(f'-----Round: {i}')
            self.player.calc_attack(self.enemy)
            self.enemy.calc_attack(self.player)

            if self.player.health <= 0:
                print(self.enemy.name, ' win')
                break
            elif self.enemy.health <= 0:
                print(self.player.name, ' win')
                break


player = Player('Tom', 130, 101, 13)
enemy = Enemy('Jerry', 50, 50, 14)

game = Battle(player, enemy)
game.battle()
