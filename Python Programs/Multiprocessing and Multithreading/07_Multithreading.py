import os
import threading

def fun(X):
    print("PID of fun :",os.getpid())
    print("PPID of fun :", os.getppid())
    print("Inside fun")

    for i in range(X):
        print("fun :",i)

def gun(X):
    print("PID of gun :",os.getpid())
    print("PPID of gun :",os.getppid())
    print("Inside gun")

    for i in range(X):
        print("gun :",i)

def main():
    No = 5
    print("PID of parent process:",os.getpid())

    thread1 = threading.Thread(target = fun, args = (No,))
    thread2 = threading.Thread(target = gun, args = (No,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End of main")

if __name__ == "__main__":
    main()