
import math
operation = input()
if (operation == "odd_num_check"):
    number = int(input())
    if(number % 2 != 0):
        print("yes")
    else :
        print("no")
        
if (operation == "perfect_square_check"):
    num = int(input())
    if(math.sqrt(num)*math.sqrt(num) == num):
        print("yes")
    else:
        print("no")
        
if(operation == "vowel_check"):
    string = input()
    vowel = "aeiouAEIOU"
    if any(char in vowel for char in string):
        print("yes")
    else:
        print("no")
        
if(operation == "divisibility_check"):
    a = int(input())
    if(a % 2 == 0 and a % 3 == 0):
        print("divisible by 2 and 3")
    elif(a % 2 != 0 and a % 3 != 0):
        print("not divisible by 2 and 3")
    elif(a % 2 == 0 and a % 3 != 0):
        print("divisible by 2")
    else:
        print("divisible by 3")

if(operation == "palindrominator"):
    string = input()
    rev = string[::-1]
    print(string+rev[1:])
    
    
if(operation == "simple_interest"):
    principal = int(input())
    years = int(input())
    if(years < 10):
        interest = ((principal * years * 5) / 100)
        print(round(interest))
    else:
        interest = ((principal * years * 8)/ 100)
        print(round(interest))

    