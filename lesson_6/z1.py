#----------Функции---------------
def code_func(s):
    return [i.encode() for i in s]

def decode_func(s):
    return [i.decode('utf-8') for i in s]

#------------Основной код-----------
a=['а','мир','новый']
encode_str = code_func(a)
print('Кодированный список строк:\n{}'.format(encode_str))
decode_str = decode_func(encode_str)
print('Декодированный список строк:\n{}'.format(decode_str))