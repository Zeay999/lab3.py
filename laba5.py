import random


def proc1():
    s = [10, 8, 18, 3, 9]
    print("Угадайте число от 1 до 20")
    a = int(input())
    if a in s:
        print("Вы угадали число!")
    elif a in s:
        print("Вы угадали число!")
    elif a in s:
        print("Вы угадали число!")
    elif a in s:
        print("Вы угадали число!")
    elif a in s:
        print("Вы угадали число!")
    else:
        print("Вы не угадали число")
        print("Список загаданных чисел.")
        print(s)

def proc2():
    s = [10, 12, 20, 2, 8, 8, 4, 23, 9]
    r = [x for i, x in enumerate(s) if x in s[:i]]
    print(r)

def proc3():
    s = ['Понедельник','Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    print("Сколько выходных вы хотите?")
    a = int(input())
    print("Ващи выходные дни")
    print(s[:a])
    print("Ваши рабочие дни")
    print(s[a:])

def proc4():
    s = ['Васильев', 'Мухин', 'Ахмедов', 'Иванов', 'Петров', 'Вершинин', 'Коротков', 'Коннов', 'Ботев', 'Бобков']
    s1 = ['Леонов', 'Макаров', 'Иванов', 'Козлуков', 'Грибов', 'Куокканен', 'Турченков', 'Мандросов', 'Николаев', 'Рахимов']
    s2 = random.sample(s, 5) + random.sample(s1, 5)
    r = len(s2)
    print("Первая группа", s)
    print("Вторая группа", s1)
    print("Команда", s2)
    print("Кол-во людей в команде", r)
    s2.sort()
    print("Команда по алфавиту", s2)
    if 'Иванов' in s2:
        k = s2.count('Иванов')
        print("Да, людей с фамилей Иванов в команде", k)
    else:
        print("Нет, Иванов не входит в команду")
proc4()