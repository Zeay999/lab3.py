def proc1():
    print("Ноль в качестве знака операции** \n завершит работу операции")
    while True:
        s = input("Знак (+,-.*,/):")
        if s== '0':
            break
        if s in ('+','-','*','/'):
            x = float(input("x="))
            y = float(input("y="))
            if s=='+':
                print("%.2f" % (x+y))
            elif s=='-':
                print("%.2f" % (x-y))
            elif s=='*':
                print("%.2f" % (x*y))
            elif s=='/':
                if y!= 0:
                    print("%.2f" % (x/y))
                else:
                    print("Делить на ноль нельзя")
        else:
            print("Неверный знак операции")
proc1()

