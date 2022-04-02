import cmath
import math

def sroot(x):
    s = math.sqrt(x)
    return s

def quadratic(a,b,c):
    d = (b ** 2) - (4 * a * c)
    s1 = (-b - cmath.sqrt(d)) / (2 * a)
    s2 = (-b + cmath.sqrt(d)) / (2 * a)
    a = s1,s2
    return a

def celtofah(c):
    f = (1.8*c)+32
    return f

def povandneg(x):
    if x>0:
        return "Positive number"
    elif x==0:
        return "zero number"
    else:
        return "Negative number"

def recsum(x):
    if x<1:
        return x
    else:
        return x + recsum(x-1)

if __name__=="__main__":
    # x = int(input("\nEnter number to find the square root:"))
    # print(sroot(x))
    #
    # print("\nQuadratic equation>")
    # a=int(input("Enter the a value:"))
    # b=int(input("Enter the b value:"))
    # c=int(input("Enter the c value:"))
    # print(quadratic(a,b,c))
    #
    # c = float(input("\nEnter the Celsius (°C) value:"))
    # print(c,"(°C) in Fahrenheit (°F)", celtofah(c))

    # x = int(input("\nEnter the number to check whether positive / negative / zero number:"))
    # print(povandneg(x))

    x = int(input("\nEnter a value to find the sum:"))
    print(recsum(x))