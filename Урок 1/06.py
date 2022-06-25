question1 = input('Любите ли вы котиков?: ')
if question1 != 'Да' and question1 != 'Нет':
    print('Ошибка')
    exit()
question2 = input('Умеете ли вы программировать?: ')
if question2 != 'Да' and question2 != 'Нет':
    print('Ошибка')
    exit()
else:
    if 'Да' in question1 and 'Да' in question2:
        print('Вы самый уникальный человек на Земеле!')
    elif 'Нет' in question1 and 'Нет' in question2:
        print('Вы, совершенно точно, гений.')
    elif 'Да' in question1 and 'Нет' in question2:
        print('Вы достойный человек.')
    elif 'Нет' in question1 and 'Да' in question2:
        print('Вы прекрасны! Пожалуйста, держитесь подальше от нормальных людей.')