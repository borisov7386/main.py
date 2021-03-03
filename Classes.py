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

# class Robot:
#     '''Класс для создания и удаления роботов с определенными именами'''
#     population = 0
#
#     def __init__(self, robot_name):
#         '''Создаёт экземляр робота с указанным именем'''
#         self.r_name = robot_name
#         print(f"Инициализация {robot_name}")
#         Robot.population += 1
#
#     def __del__(self):
#         print(f"{self.r_name} уничтожен")
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print(f"{self.r_name} был последним")
#         else:
#             print(f"Осталось {Robot.population:d} работающих роботов")
#
#     def Hi(self):
#         print(f"Привет! меня зовут {self.r_name}")
#
#     @staticmethod
#     def Howmany():
#         print('У нас {0:d} роботов.'.format(Robot.population))

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


class SchoolMember:
    """Позволяет добавлять участников в группу"""
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        SchoolMember.population += 1
        print(f"Создан участник группы с именем {name}")

    def tell(self):
        """Выводит информацию об участнике группы"""
        print(f"Имя {self.name} Возраст {self.age}", end=" ")

    @staticmethod
    def howmany():
        print(f"Всего участников {SchoolMember.population}")


class Teacher(SchoolMember):
    """Представляет преподавателя"""
    teacher_population = 0

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        Teacher.teacher_population += 1
        print(f"Создан Teacher: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary {self.salary}")

    @staticmethod
    def howmany():
        print(f"Всего учителей {Teacher.teacher_population}")


class Student(SchoolMember):
    """Представляет студента"""
    student_population = 0

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        Student.student_population += 1
        print(f"Создан студент: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Оценки {self.marks}")

    @staticmethod
    def howmany():
        print(f"Всего студентов {Student.student_population}")


t1 = Teacher("Ivanov Ivan", 35, 40000)
s1 = Student("Petrov Petr", 19, 75)

t1.tell()
# s1.tell()

SchoolMember.howmany()
Teacher.howmany()
Student.howmany()
