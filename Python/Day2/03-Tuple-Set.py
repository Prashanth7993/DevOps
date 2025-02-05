data_tuple = ('mon','tuesday','wed')
#print(data_tuple[0:2])
data_tuple1=('thur','fri','sat')
# print(data_tuple1[0])
data_tuple2=tuple('thur')
# print(data_tuple2)
# print(data_tuple + data_tuple1)
# print(type(list(data_tuple)))

##Set
data_set = set()
for i in range(1,8):
    data_set.add(i)

for i in range(1,8):
    print(data_set.pop())
   

print(len(data_set))