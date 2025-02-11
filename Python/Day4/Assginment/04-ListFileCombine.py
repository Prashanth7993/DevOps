# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
 
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

ist_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list=[number for row in ist_of_lists for number in row]
print(flat_list)