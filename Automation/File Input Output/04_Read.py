def main():
    print("Enter the file name that you want to Open : ")
    name = input()

    fd = open(name, "r")

    data = fd.read(5)

    print("Data from file is : ", data)

    fd.close()


if __name__ == "__main__":
    main()