from threading import Thread
import time


def loopa():
    print("LOOP A",end="  ")
    i = 0
    while True:
        print("LOOP A", i, end="  ")
        i = i + 2
        time.sleep(2)


def loopb():
    print("LOOPB",end="  ")
    i = 0
    while True:
        print("LOOP B", i,end="  ")
        i += 3
        time.sleep(3)


def loopc():
    print("LOOPC",end="  ")
    i = 0
    while True:
        print("LOOP C", i)
        i += 4
        time.sleep(4)


if __name__ == '__main__':
    t1 = Thread(target=loopa, name='t1')
    t2 = Thread(target=loopb, name='t2')
    t3 = Thread(target=loopc, name='t3')

    t1.start()
    t2.start()
    t3.start()
