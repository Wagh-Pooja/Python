class Arithmetic:
    def __init__(self,a,b):      
        print("Inside init (Constructor)")
        self.no1 = a             
        self.no2 = b            
        
    def Addition(self):          
        ans = self.no1 + self.no2
        return ans  


def main():
    
    obj1 = Arithmetic(10,11)
    ret = obj1.Addition()
    print("Addition is :",ret)
    
    
    obj2 = Arithmetic(5,6)
    ret = obj2.Addition()
    print("Addition is :",ret)
    

if __name__ == "__main__":
    main()