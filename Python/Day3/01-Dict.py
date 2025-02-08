person = {"fname":"prashanth",
          "age":21,
          "Aid":123456,
          "friends":["skc","ak"],
          "skills":{
              "backed_skills": ["nodejs", "ruby"],
              "database":["redis","mysql","postgress"]
          }
        }
person["address"]="mathura"
# print(person)
# print(person.get("skills").get("backed_skills"))
# print(person.get("address"))
# print("address" in person)
# print(person.pop("address"))
# print(len(person))
# del person["friends"]
# print(len(person))
# print(person["skills"]["backed_skills"])
# person["skills"]["database"].append("mongodb")
# print(person["skills"]["database"])






person_copy = person.copy()
# print(person)
# del person
# print(person_copy)
# print(person_copy.keys())

keys = person_copy.keys()
# for i in keys:
#     print("\n")
#     print(person_copy[i])
#     print("\n")


## Number to find num is grater than 10 or less than 5
num = int(input("please  enter a number"))
# if num <= 5:
#     print("num is less than 10")
# elif num >= 10:
#     print("num is greater than 10")
# else:
#     print("num out of range")


##Table to print using while loop.
# i=1
# while i<=10:
#     print(num*i)
#     i=i+1
# else:
#     print("table printing done")


##
i=1
while i<=10:
    if i==5:
        pass
    else:
        print(num*i)
    i+=1
    
