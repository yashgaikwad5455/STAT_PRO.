#To find Number of Arrangement Of word With Letter Repeated..
from math import factorial
from collections import Counter
def Arr(word):
    n=len(word)
    feq=Counter(word)
    demo=1
    for i in feq.values():
        demo*=factorial(i)
    return factorial(n)//demo
print(Arr("prashant"))
