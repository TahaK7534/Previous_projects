# calculator.py
# Taha Khan  30145085, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.

First_value = int(input('Enter the first value: '))     # Prompt the user to input the first integer value and save the integer value in the variable First_Value  

First_op = str(input('Enter the first operator: '))     # Prompt the user to input the first opperation and save the first opperation in the variable First_op as a string 

Second_value = int(input('Enter the second value: '))   # Prompt the user to input the second integer value and save the second integer value in the variable Second_Value

Second_op = str(input('Enter the second operator: '))   # Prompt the user to input the Second opperation and save the Second opperation in the variable Second_op as a string

Third_value = int(input('Enter the third value: '))     # Prompt the user to input the third integer value and save the third integer value in the variable Third_Value

Wrong_Value = ''                                        # This value is used to prevent errors from occuring

# The code bellow is used to determine if the first or second operation is either multiplication or division and save it in the correct variable

if First_op == '*':     # if the First opperator is multiplication then create a variable MD_First and save the value as True  
    MD_First = 'True' 
    
elif First_op == '/':   # if the First opperator is division then create the same variable MD_First and save the value as True
    MD_First = 'True'

else:
    MD_First = ''       # and if neither of the frist two statements are true then create the same variable MD_First and save the value as blank


if Second_op == '*':    # if the Second opperator is multiplication then create a variable MD_Second and save the value as True  
    MD_Second = 'True'

elif Second_op == '/':  # if the Second opperator is division then create the same variable MD_Second and save the value as True  
    MD_Second = 'True'

else:
    MD_Second = ''      # and if neither of the frist two statements are true then create the same variable MD_Second and save the value as blank



if First_op == '+' and MD_Second != 'True':     # if the first operation is addition and MD_Second is not '*/' then add the first two input vlaues and save it in the variable First_calculation
    First_Calculation = int(First_value + Second_value)   

elif First_op == '-'and MD_Second != 'True':    # if the first operation is subtraction and MD_Second is not '*/' then subtract the first two input vlaues and save it in the variable First_calculation
    First_Calculation = int(First_value - Second_value)

elif First_op == '/' :                           # if the first operation is division then divide the first two input vlaues and save it in the variable First_calculation
    First_Calculation = int(First_value // Second_value)

elif First_op == '*':                            # if the first operation is multiplication then multiply the first two input vlaues and save it in the variable First_calculation
    First_Calculation = int(First_value * Second_value)

elif Second_op == '/' and MD_First != 'True':    # if the second operation is division and MD_First is not '*/' then 
    First_Calculation = Second_value // Third_value      # divide the second value from the third vlaue and save it in the variable First_calculation

elif Second_op == '*' and MD_First != 'True':   # if the second operation is division and MD_First is not '*/' then
    First_Calculation = Second_value * Third_value       # multiply the second and third value and save it in the variable First_calculation




if Second_op == '+' and MD_First == 'True':                     # if the second operation is addition and MD_Second is '*/' then 
    Final_Answer = First_Calculation + Third_value              # add the First_calculation with the third value and save it in the variable Final_Answer

elif Second_op == '-'and MD_First == 'True':                    # if the second operation is subtraction and MD_Second is '*/' then
    Final_Answer = First_Calculation - Third_value              # subtract the First_calculation with the third value and save it in the variable Final_Answer

elif Second_op == '/' and MD_First == 'True':                   # if the second operation is division and MD_Second is '*/' then
    Final_Answer = First_Calculation // Third_value             # divide the First_calculation with the third value and save it in the variable Final_Answer

elif Second_op == '*' and MD_First == 'True':                  # if the second operation is multiplication and MD_Second is '*/' then
    Final_Answer = First_Calculation * Third_value             # multiply the First_calculation with the third value and save it in the variable Final_Answer

elif First_op == '+' and MD_Second == 'True':                  # if the first opperation is addition and the MD_Second is '*/'
    Final_Answer = int(First_value + First_Calculation)        # add the frist value and First_calculation and save it in the variable Final_Answer

elif First_op == '-'and MD_Second == 'True':                   # if the First opperation is subtraction and MD_second is not '*/' then
    Final_Answer = int(First_value - First_Calculation)        # subtract first value from First_calculation and save it in the variable Final_Answer

elif Second_op == '+' and MD_First != 'True':                  # if the Second_op is addition and MD_First is not 'True' then 
    Final_Answer = int(First_Calculation + Third_value)        # add the First_Calculation to the third_value and save it in the variable Final_Answer

elif Second_op == '-' and MD_First != 'True':                  # if the Second_op is addition and MD_First is not 'True' then
    Final_Answer = int(First_Calculation - Third_value)        # add the First_Calculation to the third_value and save it in the variable Final_Answer

else:                                                          # if none of the above statments are true print the values were input incorrectly 
    print('Your values were input incorrectly')                
    Wrong_Value = 1                                            # make Wrong_Value equal 1 

if Wrong_Value  != 1:                                          # if Wrong_Value dose not equal 1 then print the expression and final answer
    print(f'Entered expression: {First_value} {First_op} {Second_value} {Second_op} {Third_value}' )   # print the entered expression
    print(f'Your final answer = {Final_Answer}')     # print the final answer
