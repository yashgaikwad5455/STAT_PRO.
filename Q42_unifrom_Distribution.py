#Q42 Unform Distribution
import numpy as np
a=int(input("Enter lower Limit:"))
b=int(input("Enter upper Limit:"))
n=int(input("Enter Numbeers of Trils:"))
result=np.random.uniform(a,b,size=n)
print("Mean:",np.mean(result))
print("Var:",np.var(result))
print("Therotical Mean:",(a+b)/2)
print("Therotical Variance:",(b-a)**2/12)
