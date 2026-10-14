n = int(input("enter number : "))
result = 1
for i in range(1,n +1 ):
        result = result * i
print(result)
#using as function
def f(n) :
      result = 1
      for i in range(1,n +1 ):
        result = result * i
      return result
print(f(5))
