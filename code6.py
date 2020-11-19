#    Write a random number generator that generates random numbers
#    between 1 and 6 (simulates a dice).
import random
a=['''     
  ●  
     '''

,'''     
●   ●
     '''

,'''●    
  ●  
    ●'''

,'''●   ●
     
●   ●'''

,'''●   ●
  ●  
●   ●'''

,'''● ● ●
● ● ●
● ● ●''']

n = random.randrange(1,7,1)
print(n)
print(a[n-1])