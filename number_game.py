def number_game():
    
    #prompt the user for value of x
    x = int(input('x:'))
    #prompt the user for value of y
    y = int(input('y: '))
    #Check if x is greater than y
    if x>y:
        #Display the numbers the user provided
        print("Even numbers between %d and %d" %(y,x))
        #Iterate between the smallest number and the largest number
        #I added +1 to the  stop value in the range to be able to perform operation on all the numbers
        for i in range(y,(x)+1):
            #Get the modulus  of each of the number in the range
            if i % 2 == 0:
                #display the numbers that the modulus equals 0
                print(i)
    #when x is less than y
    else:
        print("Odd numbers between %d and %d" %(x,y))
        for i in range(x,(y)+1):
            if i % 2 != 0:
                print(i)
#Call the function
number_game()