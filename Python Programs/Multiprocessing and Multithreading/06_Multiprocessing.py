import os
import multiprocessing


def square(No):
    print("PID is :",os.getpid())
    return No*No


def main():
    data = [5,3,1,4,8,2]

    p = multiprocessing.Pool()

    result = list()

    result = p.map(square,data)

    print("Result is :",result)


if __name__ == "__main__":
    main()