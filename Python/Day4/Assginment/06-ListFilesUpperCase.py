# Flatten the following list to a new list: 
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output =  [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# print(type(countries))
# print(type(countries1))


lr = [y.upper() for lst in countries for x in lst  for y in x]
# lr = [x.upper() for lst in countries for x in lst ]
for i in range(0,len(lr),2):
    content = lr[i][:3]
    lr.append(content)
print(lr)