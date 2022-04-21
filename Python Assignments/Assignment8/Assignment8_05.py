#5.Design python application which contains two threads named as thread1 and thread2. Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. After execution of thread1 gets completed then schedule thread2.


import threading


def Digits():
    for i in range(1,50+1):
        print(i, end = '  ')
        
        
def Number():
    i = 50
    
    while(i >= 1):
        print(i, end = '  ')
        i = i - 1
        

def main():
    thread1 = threading.Thread(target = Digits)
    thread2 = threading.Thread(target = Number)
    
    thread1.start()
    thread1.join()
    
    print("\n")
    thread2.start()


if __name__ == "__main__":
    main()