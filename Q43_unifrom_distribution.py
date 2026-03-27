#Q43 NOrmal Distribution
import numpy  as np
mean=float(input("enter Mean:"))
sd=float(input("enter Sd:"))
n=int(input("Enter The Trials:"))
result=np.random.uniform(mean,sd,size=n)
print("Sample mean:",np.mean(result))
print("Sample variace :",np.var(result))
                 
