import threading


class Calculator:

    def __init__(self, name):
        self.calName = name

    def cal(self):
        count = 0
        for i in range(1, int(self.calName)+1):
            count += i
        print("1+2+3+.....+"+str(self.calName)+' = ' + str(count))


first = Calculator(1000)
second = Calculator(10000)
third = Calculator(100000)

th1 = threading.Thread(target=first.cal())
th2 = threading.Thread(target=second.cal())
th3 = threading.Thread(target=third.cal())

th1.start()
th2.start()
th3.start()