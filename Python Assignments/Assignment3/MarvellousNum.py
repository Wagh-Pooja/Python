def ChkPrime(No):
    Cnt = 0;
    
    for i in range(2,No):
        if(No%i == 0):
            Cnt = Cnt + 1;
            
    if(Cnt != 0):
        print("Number Is Not Prime");
    else:
        print("Number Is Prime");