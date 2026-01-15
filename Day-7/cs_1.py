# Nested if else control statement 
# Check eligiblity of candidate for filling indian army form 
age = float(input("Enter the age of candidate : "))
if age>=18 and age<=21:
    eduction = str(input("Enter eduction of candidate (10/12/UG) : "))
    eduction = eduction.lower()
    if eduction=='10' or eduction =='12' or eduction =='ug':
        print("Eligible for Indian Army ")
    else:
        print("pass at least high school examination first")
else:
    print("Age is not matched please enter age between 17 to 21")