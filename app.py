from threading import *
import time


class Demo:
    def num(self):
        for i in range(1, 6):
            print(i)
            time.sleep(1)

    def double(self):
        for i in range(1, 6):
            print(2*i)
            time.sleep(1)

    def square(self):
        for i in range(1,6):
            print(pow(i, 2))
            time.sleep(1)


obj = Demo()

t1 = Thread(target=obj.num)
t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

print("This is the main thread")
