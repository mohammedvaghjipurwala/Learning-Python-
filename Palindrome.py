#################################################
#
#Ask the user for a string and print out whether this string is a palindrome or not. 
#
#################################################
Str = input("Enter a string: ").lower()

### Reverse the string 

Rev_str = Str[::-1]

#condition if palindrome

if Str == Rev_str:
    print ("""%s is a palindrome"""%Str)
else:
    print ("""%s is not a palindrome"""%Str)
