pass1 = input("Введите пароль: ")
pass2 = input("Повторите пароль: ")
l1 = len(pass1)
l2 = len(pass2)
if l1<8:
    print("Короткий!")
elif l1>8 and l1==l2:
    print("OK")
else:
    print("Различаются.")