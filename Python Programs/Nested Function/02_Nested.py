def outer():
    print("Inside Outer Function")

    def Inner():
        print("Inside Inner Function")

    return Inner

def main():
    func_name = outer()     #its call to outer function
    func_name()             #its call to inner function #Inner()

if __name__ == "__main__":
    main()