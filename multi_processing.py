from multiprocessing import Process
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
    Process(target=loopa).start()
    Process(target=loopb).start()
    Process(target=loopc).start()
