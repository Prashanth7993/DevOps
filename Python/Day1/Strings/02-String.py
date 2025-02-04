# s='Hello how are u doing after lunch 73'
# x=s.index('are')
# x=s.index('after',7)
#print(x)

# s='Hello73' #This String should not be with spaces to find alnum or not
# print(s.isalnum())


s1='hello1234'
s2='453493874'
# print(s1.isalnum())
# print(s2.isalpha())
# print(s2.isdecimal())

s3='\u00b2'
# print(s3.isdecimal())
# print(s3.isnumeric())
# print(s3.isdigit())
# print(s3)
#print(s3.isidentifier())

print('-------x--------')
s4='1/2'
s4='\u00b2'

# print(s4.isdecimal())
# print(s4.isnumeric())
# print(s4.isdigit())


s41='10\u00b2'
# print(s41.isdecimal())
# print(s41.isnumeric())
# print(s41.isdigit())
# print(s41)


s5='hiii all'
a=['hi','how','are','you']
print(s5.islower())
s6=(' '.join(a))
print(s6.strip('ha'))
print(s6.split(' '))
print(s6.title())
print(s6.swapcase())