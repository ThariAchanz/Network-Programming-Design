import sys
import os

count=100
total=0
dis=0
price="10%"
total=float(total)
while(1==1):
    try:
        item=str(input("enter the item value:"))
        units=str(input("enter the number of units:"))
        if(item =="" or units==""):
            break
        item=float(item)
        units=float(units)
        tot=item*units
        total=total+tot
    except ValueError as e:
        print(e)

if(total>5000):
    dis=total*30/100
    price="30%"
elif(total>3000):
    dis=total*20/100
    price="20%"
elif(total>1000):
    dis=total*10/100
    price="10%"
elif(total<1000):
    dis=0
    price="0%"
total=total-dis
print("Discount (",price,") is Rs:",+dis)
print("total is Rs:",+total)
