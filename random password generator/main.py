from random import choice

class Generate():
    def __init__(self):
        self.upper="ABCEDFGHIJKLMNOPQRSTUVWXYZ"
        self.lower="abcedfghijklmnopqrstuvwxyz"
        self.number="0987654321"
        self.symbols="!@#$%^&*()"

    def number_pass(self,length:int) -> str:
        self.password=""
        for i in range(length):
            self.password+=choice(self.number)
        return self.password
    
    def alpha_pass(self,length:int) -> str:
        self.password=""
        self.all=self.upper+self.lower
        for i in range(length):
            self.password+=choice(self.all)
        return self.password

    def symbol_pass(self,length:int) -> str:
        self.password=""
        for i in range(length):
            self.password+=choice(self.symbols)
        return self.password
    
    def all_pass(self,length:int) -> str:
        self.password=""
        self.all=self.upper+self.lower+self.number+self.symbols
        for i in range(length):
            self.password+=choice(self.all)
        return self.password
    
if __name__=="__main__":
    passwords : Generate = Generate()
    try:
        n : int = int(input("\tMenu : \n1.Number Password\n2.Alphabet Password\n3.Symbol Password\n4.Number + Alpha + Symbol Password \n Enter a Choice : "))
        lens : int = int(input("Enter Your Password Length : "))
        if n==1:
            print("Here Your Password : ",passwords.number_pass(lens))
        elif n==2:
            print("Here Your Password : ",passwords.alpha_pass(lens))
        elif n==3:
            print("Here Your Password : ",passwords.symbol_pass(lens))
        elif n==4:
            print("Here Your Password : ",passwords.all_pass(lens))
        else:
            print("Invaild Choice.Please Enter Value Between 1 and 4")
    except ValueError:
        print("Invaild Choice")

