import my_func as ar

print("Данная программа произведет арифметические действия с двумя числами.")
try:
    a=float(input('Введите первое число: '))
    b=float(input('Введите второе число: '))
    print(a,'+',b,'=',ar.sum(a,b))
    print(a,'-',b,'=',ar.min(a,b))
    print(a,'*',b,'=',ar.um(a,b))
except ValueError:
    print('Ошибка: Введено не число')