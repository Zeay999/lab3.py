a = ('Красный', 'Синий', 'Желтый')
c1 = input()
c2 = input()
if c1 in a and c2 in a:
    if (c1 in ('Красный', 'Синий')) and (c2 in ('Красный', 'Синий')):
        print('фиолетовый')
    if (c1 in ('Желтый', 'Синий')) and (c2 in ('Желтый', 'Синий')):
        print('Зеленый')
    if (c1 in ('Красный', 'Желтый')) and (c2 in ('Красный', 'Желтый')):
        print('Оранжевый')
else:
    print('Цвет введен неверно')
