#To find Number of arrangement Of letter of Word Repeated..
from math import factorial
from collections import Counter
def arr(word):
    n=len(word)
    c=Counter(word)
    demo=1
    for x in c.values():
        demo*=factorial(x);
    return factorial(n)//demo
print("Total Number of Arrangement of Word Prashant:",arr("prashant"))
print("Total Number of Arrangement of Word Success:",arr("Success"))

#Using Permutations Function
from itertools import permutations
word="prashant"
word2="Success"
arr=list(set(permutations(word)))
print("Total Number of arrangement of Word Prashant:",len(arr))
    
