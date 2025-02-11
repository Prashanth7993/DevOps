import re
String = "Good$morning Gowri"
String1 = "Good$morning UST,good morning everyon, good morning team"
#match=re.search("morning",String,re.I) #It will also find all the words in the String. ( Index )
#match=re.findall("morning",String,re.I) #It will find all the words in the String ( object )
match=re.match("Good",String,re.I) #It will find only starting word in String

# print(match)

# if match:
#     print("Mataching",match.group(0))

# match1 = re.findall("(?i)Morning",String)
# print(match1)

match2 = re.findall("good.morning",String,re.I | re.DOTALL)
# print(match2)

match3 = re.search("good.morning",String,re.I | re.DOTALL)
var = match3.span()
# print(var)

match4 = re.findall("good",String1,re.I | re.DOTALL)
# print(match4)

l=[]
for i in re.finditer(re.escape("good"),String1,re.I):
    l.append(i.span())
    # print(i)
# print(l)


String2 = "Good morning UST,good morning everyon, good morning team"

match5 = re.sub("(?i)Good","Awesome",String2)
# print(match5)
# print(String2)


String4 = '''Good morning UST,
good morning everyon,
good morning team'''

match6 = re.split("\n",String4)
# print(match6)

pattern = r'[t].[a]' #?= 0 or 1 *= 0 or multi
match7 = re.findall(pattern,String4)
print(match7)