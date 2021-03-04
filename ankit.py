# This pulls randint, the function you need, directly from random, simplifying usage. Saying as means you don't have
# to type randint each time, just rn.
from random import randint as rn

# This section gathers the input and makes an answer variable
name = input('Enter Name: ')
question = input('Enter question: ')
answer = ''

# This gets the random number
ANSID = rn(1, 9)

answers = ['Yes, definitely', 'It is decidedly so', 'Without a doubt', 'Reply hazy, try again', 'Ask again later', 'Better if I do not tell you now.', 'Outlook not so good', 'My sources say no', 'very doubtful']
answer = answers[ANSID]
# Here, the elif (THIS ISNT WHAT ELIFS DO ITS A BAISC PRICIPAL OF PROGRAMMING AFTER THE FIRST IF ALL THE OTHERS ARE 'Else if' 'elif' is just a conbination of those IT CANNOT SERVE THE FUNCTION OF AN ELSE STATEMENT it only runs if it wasnt the previous if statement and it is equal to in this case 9 ) combines if and else. So if there is a number that's not 1 - 9, it will output this. Putting
# multiple could lead to errors.



# This function gives you an answer
# You might notice I put curly brackets in and have an f at the beginning. This is called f-string formatting.
# You simply put f at the beginning and can put the variable in curly brackets.
# This is a really simple way to put variables in without using + and all of that.
# it is much more efficient.
def return_answer():
    if name == '':
        print(f'Question: {question}')
    else:
        print(f'\n{name} has asked: {question}')
        print(f'\nIt is decided. The answer you seek is: {answer}')


# This returns an error if you do not put anything. If you don't it moves on to return_answer
def QCheck():
    if question == '':
        return 'The magic 8-ball cannot answer silence.'
    else:
        return_answer()


# This runs the answer getting part.
QCheck()
