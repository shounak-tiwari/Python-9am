try:
    Name = "Akash"
    print(Name)
    # accessing elements using index positive indexing 
    print(Name[0])
    print(Name[1])
    # trying to modify string using index 
    Name[0] = 'P'
    print(Name)
except TypeError as e:
    print(f"Some error is came {e}")