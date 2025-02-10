def Sum(a,b):
    return a+b
print(Sum(2,4))

#
mySum = lambda a,b: a+b
print(mySum(2,10))

#
print((lambda a,b: a+b) (2,4))

#
#Example of lambda function in another function
def power(x): #First parameter ie:(4)
    return lambda n: x**n #Secound parameter ie:(2)

print(power(4)(2))

