'''
Description: 
Author: CANYONl7
Date: 2021-10-23 13:05:29
LastEditTime: 2021-10-23 13:10:40
LastEditors: CANYONl7
'''

def greatest_Common_Divisor_least_Common_Multiple(x, y) :
    product = x * y
    while (x % y !=0) :
        x,y = y,x % y
    return (y, product//y)

a,b = map(int,input().split(','))
print('GCD:%d, LCM:%d'%greatest_Common_Divisor_least_Common_Multiple(a,b))