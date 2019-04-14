# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self):
        self.speed = '90'
        self.color = 'black'
        self.name = 'Audi'
        self.is_police = false

    def go(self):
        print(self.name, ' in motion')

    def stop(self):
        print(self.name, ' stopped')

    def turn(self, direction):
        print(self.name, 'rides to')


class SportCar:
    def __init__(self):
        self.speed = '290'
        self.color = 'orange'
        self.name = 'McLaren'
        self.is_police = false

    def go(self):
        print(self.name, ' in motion')

    def stop(self):
        print(self.name, ' stopped')

    def turn(self, direction):
        print(self.name, 'rides to')

class WorkCar:
    def __init__(self):
        self.speed = '40'
        self.color = 'black'
        self.name = 'JCB'
        self.is_police = false

    def go(self):
        print(self.name, ' in motion')

    def stop(self):
        print(self.name, ' stopped')

    def turn(self, direction):
        print(self.name, 'rides to')

class PoliceCar:
    def __init__(self):
        self.speed = '50'
        self.color = 'black'
        self.name = 'VAZ'
        self.is_police = true

    def go(self):
        print(self.name, ' in motion')

    def stop(self):
        print(self.name, ' stopped')

    def turn(self, direction):
        print(self.name, 'rides to')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(self.name, ' in motion')
    def stop(self):
        print(self.name, ' stopped')
    def turn(self, direction):
        print(self.name, 'rides to')

class TownCarSecond(Cars):
    def car(self):
        print(self.name, 'awesome')


currentcar = TownCarSecond('90', 'Black', 'Audi', 'false')
currentcar2 = TownCarSecond('40', 'Yellow', 'JCB', 'false')
print(currentcar.name)
print(currentcar.speed)
currentcar.go()
currentcar.car()
currentcar2.car()