#Addition of N numbers 
def Add(*N):
    calcSum =0
    for x in N:
        calcSum+=x
    return calcSum

# Substraction of N number
def Sub(*N):
    calcSub = 0 
    for x in N:
        calcSub-=x
    return calcSub

# Multiplication of N numbers 
def Mul(*N):
    calcMul = 0 
    for x in N:
        calcMul*=x
    return calcMul
