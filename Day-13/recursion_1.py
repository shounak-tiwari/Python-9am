# Function call by it self 
# fabo. sequence
def Fabo(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    return Fabo(n-1)+Fabo(n-2)

for x in range(10):
    print(Fabo(x))