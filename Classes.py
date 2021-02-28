# class Person:
#     pass
# p = Person()
# print(p)

# def sayHI(a):
#     print(f"hi {a}")
#
# sayHI("Dfcz")
#
# class Person:
#     def sayHI(self):
#         print("hi")
#
# p = Person()
# p.sayHI()
# Person().sayHI()

# class Testclass:
#     def __init__(self, name):
#         self.name3 = name
#
#     def sayhi(self):
#         print("Текст", self.name3)
#
# Testclass("3424234234").sayhi()

class Robot:
    '''Класс для создания и удаления роботов с определенными именами'''
    population = 0

    def __init__(self, robot_name):
        '''Создаёт экземляр робота с указанным именем'''
        self.r_name = robot_name
        print(f"Инициализация {robot_name}")
        Robot.population += 1

    def __del__(self):
        print(f"{self.r_name} уничтожен")
        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.r_name} был последним")
        else:
            print(f"Осталось {Robot.population:d} работающих роботов")

    def Hi(self):
        print(f"Привет! меня зовут {self.r_name}")

    @staticmethod
    def Howmany():
        print('У нас {0:d} роботов.'.format(Robot.population))

    # Howmany = staticmethod(Howmany)


# robot1 = Robot("r1d1")
# robot1.Hi()
# Robot.Howmany()
#
# robot2 = Robot("r2d2")
# robot1.Hi()
# Robot.Howmany()
#
# del robot1
# del robot2
#
# Robot.Howmany()
