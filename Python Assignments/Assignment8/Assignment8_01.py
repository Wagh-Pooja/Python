#1.Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.

import os
import threading

def Even(No):
    print("First 10 Even Numbers :")

    Num = 20

    for i in range(1,Num+1):
        if i % 2 == 0:
            print(i)


def Odd(No):
    print("First 10 Odd Numbers :")

    for i in range(1,11):
        print(2 * i - 1)


def main():
    No = 10
    
    thread1 = threading.Thread(target = Even, args = (No,))
    thread2 = threading.Thread(target=Odd, args=(No,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()