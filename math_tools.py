from math import isqrt
def Prime_numbers(num) -> list:
    prime_numbers = []
    for i in range(2,num+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers
def logarithm(test,insert="string",) ->(int and str):
    #string -> log2(16) , commant <<logarithm("log2(16)", insert = "string")>>
    #number -> 16,2     , commant <<logarithm((16,2), insert="numbers")>> 
    if insert == "string":
        temp = test.replace("log","")
        temp = temp.replace(")","")
        temp1  = temp.split("(")
        try:
            base = int(temp[0])
        except:
            base = 10
        num = int(temp1[1])
        for i in range(16):
            if base**i == num:
                v = i
                return v 
            else:
                if i ==15:
                    v = f"ln({num})/ln({base})"
                    return v
                else:
                    pass

    elif insert =="numbers": 
        num , base = test
        for i in range(16):
            if base**i == num:
                v = i
                return v 
            else:
                if i ==15:
                    v = f"ln({num})/ln({base})"
                    return v
                else:
                    pass
class Integrate: 
    def __init__(self,text):
        self.text = text
        self.calculation()
        
    def calculation(self):
        if "^" in self.text:
            temp = self.text.split("^")
            self.exp = int(temp[1])

        else:
            self.exp = 1
        temp = self.text.split("x")

        if temp[0] == " ":
           self.num = 1

        else:
            self.num = int(temp[0])
        
        self.num1 = self.exp + 1 
        
    def __str__(self) -> str:
        if self.num%self.num1 == 0:
            if self.num/self.num1 ==1:
                return f"x^{self.num1}"
            else:
                return f"{int(self.num/self.num1)}x^{self.num1}"
        else:
            return(f'{int(self.num)}(x^{self.num1}/{self.num1})')
def find_prime(n) -> list[int]:
    if n<=2:
        return []

    is_prime = [True] *n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for x in range(i*i,n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]
def is_prime(n) ->bool: 
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False

    for i in range(2, isqrt(n+1)):
        if prime[i]:
            if n%i == 0:
                return False
            else:
                for x in range(i*i,n+1,i):
                    prime[x] = False
                
    return True
def bionomial_coefficient(n, k)-> int:
    a = 1 
    p = 1
    ap = 1
    for i in range(1,n+1):
        a *=i
    for j in range(1,k+1):
        p *=j
    for l in range(1,n-k+1):
        ap *=l
    return a/(p*ap)

if is_prime(100):
    print("True")
else:
    print("False")


print(find_prime(13))


