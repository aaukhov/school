#-----Функции---------

def passtest(pas):
    """Функция проверки пароля.
    Принимает:
    pas - Пароль в типе str
    Возвращает:
    True - если пароль безопасен
    Folse - если пароль не безопасен"""
    v = True
    if len(pas) < 6:
        v = False
    if pas.isdigit():
        v = False
    if not any(ch.isdigit() for ch in pas):
        v = False
    st=pas.lower()
    if 'password' in st:
        v = False
    return v

#------основной код------

print('Программа для проверки пароля на: пароль больше 6-ти символов, содержит хотя бы одну цифру, не из цифр, нет слова password')

pas = input('Введите пароль: ')
x = passtest(pas)
print(x)
