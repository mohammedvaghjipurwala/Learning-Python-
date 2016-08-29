#######################################################################################
#
#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Make sure to ask the user to enter the number of numbers in the sequence to generate
#
#######################################################################################

num = int(input("Enter a number to generate Fibonacci: "))
def gen_Fibo():
    i = 2
    Num1 = 1
    Num2 = 1
    LST = []
    if num == 1:
        LST.append(Num1)
    elif num == 2:
        LST.append(Num1)
        LST.append(Num2)
    elif num > 2:
        
        while i < num:
            sum = Num1 + Num2
            LST.append(sum)
            Num1 = Num2
            Num2 = sum
            i += 1
    return LST
New_LIST=gen_Fibo()

print (New_LIST)
