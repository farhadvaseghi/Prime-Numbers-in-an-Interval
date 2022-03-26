import math


a = int(input("pleas enter the first number of you'r interval "))
b = int(input("pleas enter the second number of you'r interval "))

def is_prime(n):
    i=2
    prime = True
    while i<=math.floor(math.sqrt(n)):
        if n%i==0:
            prime = False
            break
        else:
            i+=1
    return prime      

prime_list=[]
for i in range(a,b+1):
    if is_prime(i):
        prime_list.append(i)

print("[INFO] list of prime numbers in range {}-{} is: ".format(a,b), prime_list)

        
