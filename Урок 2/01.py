city1 = input()
city2 = input()
if city1 == city2:
    print('НЕТ')
elif city1 == "Тула" or "Пенза" and city2=="Тула" or city2=="Пенза":
    print("НЕТ")
elif city1 == "Пенза":
    print("НЕТ")
elif city2=="Тула":
    print("НЕТ")
else:
    print("ДА")