# Dictionary comprehension
# Create a dictionary where store 1 to 5 keys and their squares 
lst = {x:x*x for x in range(1,100) if x %2 == 0 }
print(lst)