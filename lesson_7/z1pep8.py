#-----Функции-------

def sum(args):
    m = (args)
    s = 0
    for i in range(len(m)):
       s = s+int(m[i])
    return s
#-----Основной код----

mas=list(input("Введите список целых чисел через пробел, которые требуется сложить: ").split())

x=''
for i in range(len(mas)):
    x = x+(mas[i])

if not x.isdigit():
    print('Введены не целые числа, либо строка содержит символы, либо значение не введено')
else:
    s = sum(mas)
    print('Сумма чисел равна:',s)