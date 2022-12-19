from itertools import cycle
#-----------Функции----------------
def xor_crypt(data, key):
    encode_string = ''
    for (x,y) in zip(data, cycle(key)):
        encode_string += chr(ord(x) ^ ord(y))
    return encode_string
#---------Основной код--------------------------
print('Данная программа берет текст из файла, шифрует и расшифровывает его. Ключ находится в теле кода')

key='school' #Кодовое слово
with open("secret_letter.txt", 'r', encoding="utf-8") as f:
    secret_data = f.read()

encode_data = xor_crypt(secret_data, key)
decode_data = xor_crypt(encode_data, key)

print("Шифрованный текст: {}\n".format(encode_data))
print("Расшифрованный текст: {}".format(decode_data))

with open("secret_letter_output.txt", 'w', encoding="utf-8") as f:
    f.write("Шифрованный текст: {}\n".format(encode_data))
with open("secret_letter_output.txt", 'a', encoding="utf-8") as f:
    f.write("Расшифрованный текст: {}".format(decode_data))