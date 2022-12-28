#-----Функции-------

def sum(a, b):
    return a + b

def min(a, b):
    return a - b

def um(a, b):
    return a * b

def de(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return None

def kv(a, b):
    return a ** b

def os(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return None
        
def cel(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return None

#------Основной код---------

print("Данная программа из второго задания: произведет арифметические действия с двумя числами.")
print('Разработано через TDD')
print()

try:

    a=float(input('Введите первое число: '))
    b=float(input('Введите второе число: '))

    print(a,'+',b,'=', sum(a, b))
    print(a,'-',b,'=', min(a, b))
    print(a,'*',b,'=',um(a, b))
    print(a,'/',b,'=', de(a, b))
    print(a,'**',b,'=', kv(a, b))
    print(a,'%',b,'=', os(a, b))
    print(a,'//',b,'=', cel(a, b))

except ValueError:
    print()
    print('Введено не число.')

