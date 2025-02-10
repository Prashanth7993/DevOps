def Sum_num(x):
    return sum(x)

def Higher_orderFunction(f,lst): #f = Sum_num
    var = f(lst)
    return var

result = Higher_orderFunction(Sum_num,[1,2,3,4,5])
# print(result)

