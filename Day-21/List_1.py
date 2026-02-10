# List Comprehensions 
# WAP to create a list of 1 to n even numbers
# def EvenNumberList(n:int,x=list()):
#     while n !=0:
#         if n%2==0:
#             x.append(n)
#         n-=1
#     return x[::-1]
# print(EvenNumberList(10))

evenList = [x for x in range(1,10) if x % 2 ==0 ]
print(evenList)
