#Q38 Simulate 1000 Coin Filips At time  Calculate Probability Of Getting Head and Tail
import numpy as np 
N=int(input("Enter Total Number Of Simulation:"))
filips=np.random.choice(('H','T'),size=N)
head=np.sum(filips=='H')
tail=np.sum(filips=='T')
print("Total Number of Heads:",head)
print("Total Number of Tails:",tail)
print("Probability of Getting Head:",head/N)
print("Probability of Getting Tail:",tail/N)


  