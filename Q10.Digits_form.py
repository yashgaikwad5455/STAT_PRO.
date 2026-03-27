#To find No. Numbers of By using Digits With Repetation
#To find 4 Digits numbers..
digits=[1,2,3,4,5,6]
def count(digits,length):
    n=len(digits)
    return n**length
print("Total 4-digits Number Can Form:",count(digits,4))
print("Total 6-digits Number Can Form:",count(digits,6))
