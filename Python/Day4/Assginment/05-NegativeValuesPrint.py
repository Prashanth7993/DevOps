# Filter only negative and zero in the list using list comprehension
 
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst5 = [ row for row in numbers if row<=0] 
print(lst5)