import os
import multiprocessing

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
        print("gun :", i)

def main():
    No = 5
    print("PID of parent process:",os.getpid())
    process1 = multiprocessing.Process(target = fun, args = (No,))
    process2 = multiprocessing.Process(target = gun, args = (No,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("End of main")

if __name__ == "__main__":
    main()