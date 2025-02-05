##finding most Reapting char or element in the list or Array Usinf Functions
def mostReaptingElem(ar):
    Vdic = {}
    Value = 0
    for num in ar:
        if num in Vdic:
            Vdic[num] += 1
        else:
            Vdic[num] = 1

    for var in Vdic:
        if Vdic[var] > 1:  # Check if the element appears more than once
            Value += 1  # Increase the count

    return Value

arr1= [1,2,3,4,5,6,6,3,2]
print(mostReaptingElem(arr1))




##
word_arr = ['abck','adef','fefwe','efwefe','sdfregr','srereger']
print(word_arr[1:5])
print(word_arr[1:-1])
print(word_arr[::5])
print(word_arr[:3])
word_arr.pop(0)
print(word_arr)
word_arr.append('adfnd')
print(word_arr)
word_arr.insert(3,'adjdk')
print(word_arr)
word_arr[3]='afewf'
del word_arr[3]
print(word_arr.count('fefwe'))
n =len(word_arr)
mid= n//2
print(word_arr[mid:mid+1])
