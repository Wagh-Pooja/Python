#4.Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. Display id and name of each thread.


import threading
import os


def small(str):
    print("\n Thread name of small is :",threading.current_thread().name)
    
    print("\n PID of small is :",os.getpid())
    
    cnt = 0
    i = 0
    
    for i in range(len(str)):
        if(str[i] >= "a" and str[i] <= "z"):
            cnt = cnt + 1
        
    print("\n Count of small letters in given string is :",cnt)


def capital(str):
    print("\n Thread name of capital is :",threading.current_thread().name)
    
    print("\n PID of capital is :",os.getpid())
    
    cnt = 0
    
    for i in range(len(str)):
        if(str[i] >= "A" and str[i] <= "Z"):
            cnt = cnt + 1
        
    print("\n Count of capital letters in given range is :",cnt)


def digits(str):
    print("\n Thread name of digits is:",threading.current_thread().name)
    
    print("\n PID of digits is :",os.getpid())
    
    cnt = 0
    
    for i in range(len(str)):
        if(str[i] >= '0' and str[i] <= '9'):
            cnt = cnt + 1
        
    print("\n Digits count of given string is :",cnt)


def main():
    Data = input("Enter Name Here :")
    
    small_thread = threading.Thread(target = small, args = (Data, ), name = 'SmallThread')
    
    capital_thread = threading.Thread(target = capital, args = (Data, ), name = 'CapitalThread')
    
    digits_thread = threading.Thread(target = digits, args = (Data, ), name = 'DigitsThread')
    
    small_thread.start()
    small_thread.join()
    
    capital_thread.start()
    capital_thread.join()
    
    digits_thread.start()
    digits_thread.join()
    

if __name__ == "__main__":
    main()
