def proc1():
    a = int(input())
    if a>54:
        print('Неверное место')
        quit()
    if a in range(37,55):
        print('Ваше место боковое')
    else:
        if a % 2 == 0:
            print('Ваше место верхнее в купе')
        else:
            print('Ваше место нижнее в купе')
proc1()


