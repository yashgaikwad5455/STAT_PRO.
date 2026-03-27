from math import factorial
def ncr(n,r):
    return  factorial(n)//factorial(r)*factorial(n-r)
print("8C3",ncr(8,3))
print("12C2",ncr(12,2))
print("5C1",ncr(5,1))
