Group_1 = {"Samrath", "Vinay", "Vinay Waskel", "CNG" , "petrol" ,"lpg", "disel"}
Group_2 = {"Billu", "Pillu", "Barood", "Angaar", "Samrath", "Vinay","Vinay Waskel"}
# Print different elements of Group - 1
result = Group_1.difference(Group_2)
# print the result 
print(result)
# Print different elements of Group - 2
result = Group_2.difference(Group_1)
# print the result 
print(result)
# Print different elements of Group 1 & 2 
result = Group_1.symmetric_difference(Group_2)
print(result)
# print all common elements in both sets 
result = Group_1.intersection(Group_2)
print(result)