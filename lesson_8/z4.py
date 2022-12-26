import time

#-----------Декораторы------------
def log(func, x):
    def wrapper():
        start = time.time()
        print('Старт функции')
        time.sleep(x)
        func()
        end = time.time()
        print('Функция выполнена, время выполнения:',(end - start))
    return wrapper

#-----------Функции---------------

def mir():
    for i in range(5):
        print('Привет мир!!!')


#-----------Основной код----------

x = 3            #Время Задержки

mir_log = log(mir, x)
mir_log()