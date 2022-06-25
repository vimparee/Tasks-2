login = input('Введите логин: ')
if '@' in login:
    print("Некорректный логин")
else:
    mail = input('Введите резервную почту: ')
    if '@' in mail:
        print('OK')
    else:print("Некорректный адрес")