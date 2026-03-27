from itertools import permutations,product
digits="0123456789"
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res1=list(product(digits,repeat=2))
res2=list(product(alpha,repeat=2))
for i in res1:
    for j in res2:
        print("".join(i+j))

