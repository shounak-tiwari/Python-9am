# multiply all the elements of list from 2 and store in a resultant list 
a = [2,3,4,5,6,7,8,9,10]
result = [x*2 for x in a]
print(result)
# cleaner code : combines loopinf filtering and transformation in a single line 
# exection often fast then equivalent fot loops 
# more readable : its avoid verbose loops and temp variable 
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(mat)
res = [val for row in mat for val in row]
print(res)