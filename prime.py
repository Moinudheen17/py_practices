num = int(input("enter number"))
if num <= 1 :
    print("not prime")
else :
    isPrime= True
for i in range (2, (num//2) +1) :
    if num % i== 0:
        isPrime = False
        break
if isPrime == True :
    print("prime")
else :
    print("not prime")
