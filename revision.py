import numpy as np
N=int(input("enter simulations of die:"))
sample=[1,2,3,4,5,6]
result=(np.random.choice(sample,size=N))
print("FACE\t frequency\tprobablity")
for i in range(1,7):
    freq=np.sum(result==i)
    prob=freq/N
    print("i","\t",freq,"\t",prob)