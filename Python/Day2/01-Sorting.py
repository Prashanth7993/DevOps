
##Sorting the list using Sorted()
list = ['apple','orange','pineapple','grapes','bananna']
s=sorted(list,reverse=True)
print(s)

##Finding Secound largest element using for if else
list1 = [2,3,5,63,1,45]
largest = max(list1)
secound_largest = max(list1)
for i in range(0,len(list1)):
    if list1[i] < secound_largest:
        secound_largest = largest
        largest = list1[i]
    elif(list1[i] > secound_largest):
        if(list1 != largest):
            secound_largest = list1[i]
print(secound_largest)

##Finding Secound smallest element using for if else
smallest = float('inf')
secound_Smallest = float('inf')
for i in range(0,len(list1)):
    if list1[i] < smallest:
        secound_Smallest = smallest
        smallest = list1[i]
    elif(list1[i] < secound_Smallest):
        if list1 != smallest:
            secound_Smallest = list1[i]
print(secound_Smallest)


##Finding Secound largest element using function
def FindingSecoundLargest(ls):
    largNum = max(ls)
    scndLargNum = max(ls)
    for num in ls:
        if num < scndLargNum:
            scndLargNum = largNum
            largNum = num
        elif num > scndLargNum:
            if num != largNum:
                scndLargNum = num
    return scndLargNum
print(FindingSecoundLargest(list1))


##Finding Secound Smallest element using function
def FindingSecoundSmallestNum(ls1):
    SmNum = max(ls1)
    SendSmNum = max(ls1)
    for i in ls1:
        if i < SmNum:
            SendSmNum = SmNum
            SmNum = i
        elif i < SendSmNum:
            if SendSmNum != SmNum:
                SendSmNum = i

    return SendSmNum
print(FindingSecoundSmallestNum(list1))
