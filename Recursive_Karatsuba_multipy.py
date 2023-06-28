def multi(num1 , num2):
    
    count1 = int(len(num1) / 2)
    count2 = int(len(num2) / 2)

   # assign a,c the left half of num1,num2 respectively and b,d the right half of num1,num2
    a = num1[ :count1] 
    b = num1[count1 : ]
    c = num2[ :count2]
    d = num2[count2: ]
    
    # consider the base case of when both the numbers are single digit
    # then it returns multiplication of both
    if(len(num1)== 1 or len(num2) == 1):
        return int(num1) * int(num2)

    # recursively calls function multi(num1,num2) until the number a or b or c or d is a single digit
    #then first executes the base caes and then executes the recursive calls
    return ((10**int(len(num1)))* multi(a ,c)) + ((10**int((len(num1)/2))) * (multi(a ,d) + multi(b,c))) + multi(b ,d)

#ENTER TWO NUMBERS TO MULTIPLY
x = input("Enter the first number: ")
y = input("Enter the second number: ")
print(multi(x,y))
