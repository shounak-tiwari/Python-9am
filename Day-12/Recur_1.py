def Fact(num):
    if num ==0 or num ==1:
        return 1
    return num*Fact(num-1)

print(f"The factorial of 5 is : {Fact(5)}")