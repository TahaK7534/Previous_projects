def input_validation(x): #purose #arguments #what it retuns
    """Determine if the value is the correct length, has no duplicates, is all lowe case, and is alpha numaric.
    A value is needed to be inputed

    Arguments:
    x -- string representing the cipher inputed

    What it retuns
    true_false -- a value of 1 or 0 depending on if the requierments are fufilled is returned.
    """
    true_flase= 0
    if len(x) == 26 and len(x) == len(set(x)):
        if x.isalnum() == True and x.isupper() == False:
            true_flase = 1
    return true_flase

def encryption(x,y):
    """Creation of a encryption dictionary.
    Two values need to be inputed for code to run

    Arguments:
    x -- string representing cipher input by user
    y -- string representing blank dictionary storage
    alphabet -- a sting containing all the letters of the alphabet
    
    What it retuns
    y -- a dictionary containing all 26 letters of the alphabet each individually assigned to a letter from the cipher is returned
    """    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(x)):
            y[alphabet[i]] = x[i]
    return y

def decryption(x,y):
    """Creation of a decryption dictionary.
    Two values need to be inputed for code to run

    Arguments:
    x -- string representing cipher input by user
    y -- string representing blank dictionary storage
    alphabet -- a sting containing all the letters of the alphabet
    
    What it retuns
    y -- a dictionary containing all 26 letters from the cipher each individually assigned to a letter from alphabet is returned
    """    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(x)):
            y[x[i]] = alphabet[i]
    return y
    
dictionary = {}        # define an empty dictionary 
result = ''            # define an empty string that us updated later on
loop = 1               # asign the value of 0 for the variable loop to later be used as a peramiter for a while loop
loop_2 = 0             # asign the value of 0 for the variable loop to later be used as a peramiter for a while loop

while loop == 1:       #the code bellow will run as long as the variable is eqaul to 1

    selection = (input('Select 1 to encode or 2 to decode your message, select 0 to quit: '))   #requst the user for an input for which option they want

    if selection == '1':        # if the selction is 1 run the code bellow

        text = input('Please enter the text to be processed:')      #request and recive an input for the processed text
        cipher = (input('Please enter the cipher text:'))           #request and recive an input for the cipher
        cipher_dictionary =encryption(cipher,dictionary)            #asign the retrun value of the fuction incription for x is cipher and y is dictionary
        validation = input_validation(cipher)                       #asign the return value of the function validation for x is cipher

        if validation == 1:                                         #if the value of validation is equal to 1 run bellow code
            while loop_2 < len(text):                               #while loop_2 is less then the value of the length of the text input run the bellow code  
                if text[loop_2] in cipher_dictionary.keys():        #if a letter in the text variable is inside the dictionary of cipher_dictionary then run the bellow code
                    result += cipher_dictionary[text[loop_2]]       #add the new letter from the dictionary
                loop_2 = loop_2 +1                                  #add a value to loop_2

            loop_2 =0                                               #reset the value of loop_2 to allow for the code to continue to run
            print('Your cipher is valid')                           #print your cipher is valid     
            print(f'Your encriped text is {result}')                #print the the encriped text
            result =''                                              #reset the value of result allowing for the code to be repeted without errors

        else:                   #else run bellow code

            print('invalid cipher')                                 #print that the cipher is invalid

    elif selection == '2':          #if the slection is 2 run the code bellow

        text = input('Please enter the text to be processed:')      #request and recive an input for the processed text
        cipher = (input('Please enter the cipher text:'))           #request and recive an input for the cipher
        cipher_dictionary =decryption(cipher,dictionary)            #asign the retrun value of the fuction incription for x is cipher and y is ciper_dictionary
        validation = input_validation(cipher)                       #asign the return value of the function m for x is cipher

        if validation == 1:                                         #if the value of apple is equal to 1 run bellow code
            while loop_2 < len(text):                               #while loop_2 is less then the value of the length of the text input run the bellow code  
                if text[loop_2] in cipher_dictionary.keys():        #if a letter in the text variable is inside the dictionary of cipher_dictionary then run the bellow code
                    result += cipher_dictionary[text[loop_2]]       #add the new letter from the dictionary
                loop_2 = loop_2 +1                                  #add a value to loop_2

            loop_2 = 0                                              #reset the value of loop_2 to allow for the code to continue to run
            print('Your cipher is valid')                           #print your cipher is valid
            print(f'Your encriped text is {result}')                #print the the encriped text
            result =''                                              #reset the value of b allowing for the code to be repeted without errors

        else:                   #else run bellow code

            print('invalid cipher')                                 #print that the cipher is invalid

    elif selection == '0':      #if the selection is 0 then run bellow code
        print('Thank you for using the encryption program!')        #print thank you for using the encryption program
        loop = 0                                                    #change the value of the variable loop to end the code
    else:                       # else run bellow code
        print('Please correctly input a value')                     #infrom the user to correctly select an option