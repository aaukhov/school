import os

print("Имя вашей операционной системы:",os.name)
print("Имя вашего пользователя:",os.getlogin())
print("Ваши файлы и папки",os.listdir())