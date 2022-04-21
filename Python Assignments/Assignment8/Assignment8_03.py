#3.Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition.


import threading


def evenlist(No):
    Add = 0
    for i in range(len(No)):
        if(No[i] % 2 == 0):
            Add = Add + No[i]
    print("Addition of Evenlist is :",Add)


def oddlist(No):
    Add = 0
    for i in range(len(No)):
        if(No[i] % 2 != 0):
            Add = Add + No[i]
    print("Addition of Oddlist is :",Add)


def main():
    No = []
    Ele = 0
    
    Num = int(input("Enter Number of Elements :"))
    
    for i in range(Num):
        Ele = int(input("Enter List Parameters :"))
        
        No.append(Ele)
        
    print("Parameters of given list are :",No)
    
    evenlist_thread = threading.Thread(target = evenlist, args = (No, ))
    
    oddlist_thread = threading.Thread(target = oddlist, args = (No, ))
    
    evenlist_thread.start()
    oddlist_thread.start()
    
    evenlist_thread.join()
    oddlist_thread.join()



if __name__ == "__main__":
    main()