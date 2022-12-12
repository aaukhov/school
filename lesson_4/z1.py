mas=list(input("Введите список цифр через пробел для сортировки методом пузырика: ").split())
n=len(mas)
x=0
for run in range(n-1):
    for i in range(n-1):
        if mas[i]>mas[i+1]:
            x +=1
            mas[i],mas[i+1] = mas[i+1],mas[i]
print('Отсортированый список:',*mas)
print('Выполнено количество замен:',x)
print('Количество элементов в списке:',n)