#-------------Классы---------------

class human:
    def __init__(self, name, age, gender):
        self.name = name                               #Имя 
        self.age = age                                 #Возраст
        self.gender = gender                           #Пол

class student(human):
    def __init__(self, name, age, gender, amount, balls):
        super().__init__(name, age, gender)
        self.amount = amount                           #Количество сданных домашних работ
        self.balls = balls                             #Количество баллов за домашние работы
    
    #Перезагружаем операторов сравнения
    
    def __gt__(self, other):
        return int(self.amount) > int(other.amount)

    def __eq__(self, other):
        return int(self.amount) == int(other.amount)

    def __ne__(self, other):
        return int(self.amount) != int(other.amount)
    
    
#---------------Основной код--------------

Bod = student('Боб', 20, 'Мужской', 6, 30)
Tom = student('Том', 21, 'Мужской', 7, 34)
Lena = student('Лена', 19, 'Женский', 6, 28)

print('Студент,',Bod.name, 'Сдал', Bod.amount, 'домашних заданий')
print('Студент,',Tom.name, 'Сдал', Tom.amount, 'домашних заданий')
print('Студентка,',Lena.name, 'Сдала', Lena.amount, 'домашних заданий')
print('Лена сдала заданий больше, чем Том:',Lena > Tom)
print('Том сдал меньше заданий, чем Боб:', Tom < Bod )