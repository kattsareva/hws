class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return(f'{self.name} тронулась с места')

    def show_speed(self):
        return(f'\n Ваша скорость {self.speed}')

    def turn(self, direction):
        return(f'\n{self.name} повернула {direction}')

    def stop(self):
        return(f'\n{self.name} остановилась.')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость. Вы движетесь со скоростью {self.speed}'
        else:
            return f'{self.name} движется с разрешённой скоростью.'

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость. Вы движетесь со скоростью {self.speed}'
        else:
            return f'{self.name} движется с разрешённой скоростью.'

town = TownCar('Mercedez', 55, 'black', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Porsche', 200, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('Opel', 40, 'green', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Lada', 70, 'blue', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('left'), work.stop())