def proc1():
    n = int(input())
    result = []
    for i in range(n):
        result.append(input())
    word = ' '.join(result)
    print(word)

def proc2():
    words = []
    while (new_word := str(input())) != "stop":
        words.append(new_word)
    print(" ".join(words))

def proc3():
    words = []
    while (new_word := str(input())) !="stop":
        if "ф" in new_word or "Ф" in new_word:
            print('Ого, это редкое слово!')
        else:
            print('Это обычно слово')
        words.append(new_word)
    print(" ".join(words))
proc3()
proc2()
proc1()
