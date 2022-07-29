def main():
    print("Enter the file name that you want to Open : ")
    name = input()

    fd = open(name, "r")

    fd.seek(3,0)

    data = fd.read()

    print(data)

if __name__ == "__main__":
    main()




    #0 Begining
    #1 Current
    #2 End