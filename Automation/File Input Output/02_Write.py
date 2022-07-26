def main():
    print("Enter the file name that you want to Open : ")
    name = input()

    fd = open(name, "w")

    print("Enter the data that you want to Write in the file : ")
    data = input()

    fd.write(data)

    fd.close()


if __name__ == "__main__":
    main()