import z2

def test_sum_2_2():                    #Сложение двух чисел
    assert z2.sum(2, 2) == 4.0

def test_min_2_2():                    #Вычитание двух чисел
    assert z2.min(2, 2) == 0.0

def test_um_2_2():                     #Умножение двух чисел
    assert z2.um(2, 2) == 4.0

def test_de_2_2():                     #Деление двух чисел
    assert z2.de(2, 2) == 1.0

def test_de_2_0():                     #Деление на ноль
    assert z2.de(2, 2) == None

def test_kv_2_2():                     #Степень числа
    assert z2.kv(2, 2) == 4.0

def test_os_2_2():                     #Остаток
    assert z2.os(2, 2) == 0.0

def test_os_2_0():                     #Деление на ноль
    assert z2.os(2, 0) == None

def test_cel_2_2():                    #Целое численное деление 
    assert z2.cel(2, 2) == 1.0

def test_cel_2_0():                    #Деление на ноль
    assert z2.cel(2, 0) == None