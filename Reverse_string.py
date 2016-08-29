##########################################################################################
#
#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#  My name is Michele
#
#Then I would see the string:
#
#  Michele is name My
#
#shown back to me.
#
#
##########################################################################################

Sentence = input("Enter a long sentence delimited by spaces only : ")
def reverse_str():
    List = Sentence.split(" ")
    i = 1
    New_List = []
    while i <= len(List) :
        New_List.append(List[len(List) - i])
        i += 1
    return " ".join(New_List)

def reverse_str_WO():
    List = Sentence.split(" ")
    return " ".join(List[::-1])

print (reverse_str())

print (reverse_str_WO())
