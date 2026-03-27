#To find No. Numbers of By using Digits With Repetation
from math import factorial 
digits=[1,2,3,4,5,6]
print("With Repetation=>")
def count(digits,length):
    n=len(digits)
    return n**length
print("Total 4-digits Number Can Form:",count(digits,4))
print("Total 6-digits Number Can Form:",count(digits,6))

print("Without repetations=>")
#To find No. Numbers of By using Digits Without Repetation
def wcount(digits,length):
    n=len(digits)
    return factorial(n)//factorial(n-length)
print("Total 4-digits Number Can Form:",wcount(digits,4))
print("Total 6-digits Number Can Form:",wcount(digits,6))
