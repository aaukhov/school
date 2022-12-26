#-----Классы----------
class animsls:
    def __init__(name, size, weight, eats):
        name.size = size                                                     #Размер
        name.weight = weight                                                 #Вес
        name.eats = eats                                                     #Употребляет в пищу

class mammals(animsls):
    def __init__(name, size, weight, eats, wool, claws, ears):
        super().__init__(size, weight, eats)
        name.wool = wool                                                     #Наличие шерсти
        name.claws = claws                                                   #Наличие когтей
        name.ears = ears                                                     #Наличие ушных раковин 

class human(mammals):
    def __init__(name, size, weight, eats, wool, claws, ears, age, speciality, nationalit):
        super().__init__(size, weight, eats, wool, claws, ears)
        name.age = age                                                       #Возраст
        name.speciality = speciality                                         #Специальность 
        name.nationalit = nationalit                                         #Национальность 

class cat(mammals):
    def __init__(name, size, weight, eats, wool, claws, ears, colour, tray, breed):
        super().__init__(size, weight, eats, wool, claws, ears)
        name.colour = colour                                                 #Цвет
        name.tray = tray                                                     #Лоток
        name.breed = breed                                                   #Порода

class dog(mammals):
    def __init__(name, size, weight, eats, wool, claws, ears, collar, training, toy):
        super().__init__(size, weight, eats, wool, claws, ears)
        name.collar = collar                                                 #Ошейник
        name.training = training                                             #Дрессированный
        name.toy = toy                                                       #Любимая игрушка


#-----Основной код-------

Barsik = cat('25 см', '5 кг', 'Мышей', 'Покрывает все тело', 'Маленькие', 'На макушке', 'Рыжий', 'Приучен', 'Мей-кун')
Bob = human('173 см', '75 кг', 'Пиццей', 'Волосы', 'Аккуратные', 'Обычные', '30 лет', 'Программист', 'Англичанин')
Rem = dog('70 см', '30 кг', 'Сухим кормом', 'Покрывает все тело', 'Большие', 'На макушке', 'Строгий', 'Дрессирован', 'Мяч')

print('О коте Барсике')
print('Вес Барсика:', Barsik.weight)
print('У Барсика когти:', Barsik.claws)
print('Цвет Барсика:', Barsik.colour)
print()

print('О человеке Боб')
print('Рост Боба:', Bob.size)
print('Уши Боба:', Bob.ears)
print('Возраст Боба:', Bob.age)
print()

print('О собаке Рэм')
print('Рэм ест:', Rem.eats)
print('Шерсть Рема:', Rem.wool)
print('Ошейник у Рэма:', Rem.collar)
