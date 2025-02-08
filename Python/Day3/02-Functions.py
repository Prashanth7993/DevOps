def hello_world():
    print("hello world")

# hello_world()

#Parameter
def hello_world(message):
    print(message)

# hello_world("parameter")

#sum
def Sum(num1,num2):
    print(num1 + num2)

# Sum(2,3)


#Suming up a list
def Sum1(nums):
    sum=0
    for i in nums:
        sum+=i
    print(sum)

# Sum1([1,2,3,4,5,5,6])



#Check Prime
def check_prime(num):
    for i in range(2,num//2):
        if num%i==0:
            print("not prime")
            return
    print("prime")

#check_prime(32)


##check first repeating num
def findrepeatingnum(Rnum):
    store = set()
    for i in Rnum:
        if i in store:
            return i
        store.add(i)

# print(findrepeatingnum([1,2,3,4,5,6,7,7,7,2]))

