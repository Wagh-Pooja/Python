import os
import threading

def fun(X):
    print("PID of fun :",os.getpid())
    print("PPID of fun :", os.getppid())
    print("Thread name of fun :",threading.current_thread().name)
    print("Inside fun")

    for i in range(X):
        print("fun :",i)

def gun(X):
    print("PID of gun :",os.getpid())
    print("PPID of gun :",os.getppid())
    print("Thread name of gun :",threading.current_thread().name)
    print("Inside gun")

    for i in range(X):
        print("gun :",i)

def main():
    No = 5
    print("PID of parent process:",os.getpid())
    print("Thread name of main is :",threading.current_thread().name)

    thread1 = threading.Thread(target = fun, args = (No,), name = "funthread")
    thread2 = threading.Thread(target = gun, args = (No,), name = "gunthread")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End of main")

if __name__ == "__main__":
    main()