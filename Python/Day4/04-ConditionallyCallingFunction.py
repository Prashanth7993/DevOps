def square(x):
    return x**2
def cube(a):
    return a**3
def absolute(b):
    if b >= 0:
        return b
    else:
        return -(b)
    
def Hof(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    else:
        return absolute
    
res = Hof('square')
res = Hof('cube')
res = Hof('absolute')
print(res(-5))