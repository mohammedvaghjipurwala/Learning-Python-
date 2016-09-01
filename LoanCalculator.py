#################################################################
'''
Loan and payment calculator

Description

The interest due on a loan can be calculated according to the simple formula: 



I = P × R × T 

where I is the interest paid, P is the amount borrowed (principal), R is the interest rate, and T is the length of the loan. 

It is common for loans to be amortized which allows the lendor to collect their interest early in the loan period. We will ignore amortization for the purpose of this program. For bonus points, figure out how to do amortization and print an amortization schedule with the payment schedule. There is an excellent explanation of the amortization formula at Interest.com. 

Write a program that calculates the interest due on a loan and prints a payment schedule. Make sure you round the output to two decimal places. For bonus points, figure out how to calculate amortization and print an amortization schedule. It will be your responsibility to find an appropriate format for the amortization printout. 

Make sure you handle the dollars correctly! Floating point numbers in Python (and other programming languages) are subject to rouding errors when doing floating point arithmetic. For an explanation of this phenomenon, see the  floating point arithmetic section of the Python tutorial. One of the most common strategies to solve the problem is to do all money-related calculations in pennies, converting back to dollars when the results are displayed. If you don't handle this issue correctly, your program won't give correct answers in all cases. 

'''
#################################################################
 
 def CalculateInterest(P,R,T):
    return (P * R * T)/100
    
def PrintEMI(Interest,Principle,Time):
    print("           Amount     Remaining")
    print("Pymt#       Paid       Balance")
    print("-----      -------    ---------")
    Months = Time * 12
    Anu_Amt = Interest + Principle
    Payment = round(Anu_Amt / Months,2)
    for i in range(0,Months+1):
        if i == 0:
            print ("%d        $0.00      $%.2f" %(i,Anu_Amt))
        elif i == Months:
            print ("%d        $%.2f      $0.00" %(i,final))
        else:
            print ("%d        $%.2f      $%.2f" %(i,Payment,Anu_Amt))
            final = Anu_Amt
            
        Anu_Amt -= Payment
        
if __name__ == "__main__":
    
    print ("Loan calculator\n")
    prin = int(input("Amount borrowed: "))
    Rate = float(input("Interest rate: "))
    Term = int(input("Term (years): "))
    
    print("Amount borrowed:   $",prin)
    Interest = CalculateInterest(prin,Rate,Term)
    print("Total interest paid: $",Interest)
    
    PrintEMI(Interest,prin,Term)
