#c2H5(OH)
print('Программа берет количество атомов из файла input.txt проверяет, сколько молекул спирта можно получить и записывает данные в файл output.txt')
with open("input.txt","r") as f:
    c,h,o=f.read().split(",")
c=int(c)
h=int(h)
o=int(o)
s=0
i=1
while i>0 :
    c=c-2
    h=h-6
    o=o-1
    if not (c < 0 or h<0 or o<0) :
        s=s+1
    else:
        break
print('Молекул спирта можем получить:',s)
with open("output.txt",'w') as f:
    f.write(f"Молекул спирта можем получить: {s}")
