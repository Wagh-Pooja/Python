def main():
    print("Enter the file name that you want to Open : ")
    name = input()

    fd = open(name, "rb")

    data = fd.read(5)

    fd.seek(3,1)

    data = fd.read()

    print(data)

if __name__ == "__main__":
    main()




    #0 Begining
    #1 Current
    #2 End