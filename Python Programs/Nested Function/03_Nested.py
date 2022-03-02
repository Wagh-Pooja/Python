def fun():
    print("Inside fun")

def gun(func_name):
    print("Inside gun")
    func_name()         #fun()

def main():
    gun(fun)

if __name__ == "__main__":
    main()