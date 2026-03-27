#Q41 Poisson Distribution
import numpy as np
m=int(input("Enter The Average times occurs:"))
N=int(input("Enter Total Number Times simulate:"))
result=np.random.poisson(m,size=N)
n=np.max(result)
print("x \t Freq \t Probability")
for x in range(n+1):
    freq=np.sum(result==x)
    pro=freq/N
    print(x,"\t",freq,"\t",pro)
print("mean of poisson distribution:",np.mean(result))
print("var of poisson distribution:",np.var(result))
