print('В данной программе вы будете складывать и убирать предметы из рюкзака, общий вес рюкзака не должен превышать 10 кг.')
i=1
v=0
R=[]
while i>0:
    v=0
    n=len(R)
    for run in range(n):
        x=R[run]
        v=v+x
    d=input('Что вы хотите сделать: Положить-p, Удалить-u, Просмотерь рюкзак-v, Выйти-q: ')
    if d=='p':
        p=input('Положить 1-Меч 2-Шлем 3-Аптечку: ')
        if (p=='1' and (v+3)<=10):
            R.append(3)
        elif (p=='2' and (v+2)<=10):
            R.append(2)
        elif (p=='3' and (v+1)<=10):
            R.append(1)
        else:
            print('Предмет не из списка или вы превысили вес 10 кг.')
    elif d=='u':
        p=input('Убрать 1-Меч 2-Шлем 3-Аптечку: ')
        x=0
        if p=='1':
            x=3
        elif p=='2':
            x=2
        elif p=='3':
            x=1
        if x in R:
            R.remove(x)
        else:
            print('Такого предмета нет в рюкзаке')
    elif d=='v':
        n=len(R)
        v=0
        print('В вашем рюкзаке находится: ')
        for run1 in range(n):
            x=R[run1]
            if x==3:
                print('Меч с весом',x,'кг.')
            elif x==2:
                print('Шлем с весом',x,'кг')
            elif x==1:
                print('Аптечка с весом',x,'кг')
            v=v+x
        print('Общий вес',v,'кг')
    elif d=='q':
        break
    else:
        print('Неверная команда!!!')
print('END')
