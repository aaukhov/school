#-------------Классы---------------

class human:
    def __init__(id, name, age, gender):
        id.name = name                               #Имя 
        id.age = age                                 #Возраст
        id.gender = gender                           #Пол

class student(human):
    def __init__(id, name, age, gender, amount, balls):
        super().__init__(name, age, gender)
        id.amount = amount                           #Количество сданных домашних работ
        id.balls = balls                             #Количество баллов за домашние работы

#---------------Основной код--------------

Bod = student('Боб', 20, 'Мужской', 6, 30)
Tom = student('Том', 21, 'Мужской', 7, 34)
Lena = student('Лена', 19, 'Женский', 6, 28)

print('Студент,',Bod.name, 'Сдал', Bod.amount, 'домашних заданий')
print('Студент,',Tom.name, 'Сдал', Tom.amount, 'домашних заданий')
print('Студентка,',Lena.name, 'Сдала', Lena.amount, 'домашних заданий')