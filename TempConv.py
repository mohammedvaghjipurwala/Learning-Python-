##############################################################################
'''
Temperature converter

Description

Write two functions that will convert temperatures back and forth from the Celsius and Fahrenheit temperature scales. The formulas for making the conversion are as follows: 
  Tc=(5/9)*(Tf-32)
  Tf=(9/5)*Tc+32


where Tc is the Celsius temperature and Tf is the Fahrenheit temperature. More information and further descriptions of how to do the conversion can be found at  this NASA Webpage. If you finish this assignment quickly, add a function to calculate the wind chill. 

Input

Your program should ask the user to input a temperature and then which conversion they would like to perform. 

Sample session
Temperature converter

Enter a temperature: 20
Convert to (F)ahrenheit or (C)elsius? F

20 C = 68 F
'''
##############################################################################

def Cel2Fah(Tc):
    return (9/5)*Tc+32
    
def Fah2Cel(Tf):
    return (5/9)*(Tf-32)
    
if __name__ == "__main__":
    print ("Temperature converter \n")
    temperature = int(input("Enter a temperature: "))
    if str(input("Convert to (F)ahrenheit or (C)elsius? ")) == 'F':
        print (Fah2Cel(temperature))
    else:
        print (Cel2Fah(temperature))
