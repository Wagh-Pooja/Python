def outer():
    print("Inside Outer Function")

    def Inner():
        print("Inside Inner Function")

    #Inner()

def main():
    outer()

if __name__ == "__main__":
    main()