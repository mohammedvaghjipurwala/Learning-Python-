##########################################################################################
'''
http://openbookproject.net/pybiblio/practice/wilson/piglatin.php
'''
##########################################################################################

import os
def Translator(Str,vowels):
    cnt = 0
    newsplit1 = ''
    newsplit2 = ''
    while cnt < len(Str):
        if Str[cnt] in vowels:
            newsplit1 = Str[cnt:len(Str)]
            break
        else:
            newsplit2 += Str[cnt]
        cnt += 1
    FinalStr = newsplit1 + newsplit2
    translatedStr = AddAy(FinalStr)
    return(translatedStr)
    
def AddAy(ConvStr):
    return (ConvStr + "ay ")
    
if __name__ == "__main__":
    os.system('clear')  # for Linux/OS X
    vowels = ['a', 'e', 'i', 'o', 'u']
    outputStr = ''
    print ("Welcome to English to pig latin translator !!!\n")
    print ("Type 'exit' to exit the translator...\n")
    Sentence = ''
    while True:
        Sentence = input(">>>> ").lower().split(' ')
        if Sentence != 'exit':
            for i in Sentence:
                outputStr += Translator(i,vowels)
            print (outputStr[0].upper() + outputStr[1:])
            outputStr = ''
        else:
            break
