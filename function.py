'''
Created on May 19, 2020

@author: samsung
'''
def computepay(h,r):
    h=float(hrs)
    r=float(rate)
    if h>40:
        extra=h-40
        return 40*r+(extra*r*1.5)
    else:
        return h*r 
   
hrs = input("Enter Hours:")
rate =input("Enter Rate:")

p = computepay(hrs,rate)
print("Pay",p)