valid = False

while not valid:
    try:
        n=int(input("Enter a number: "))
        while n%2 == 0:
            print("bye")
        valid = True

    except ValueError:
        print("There is an error in the value you put.")


    
