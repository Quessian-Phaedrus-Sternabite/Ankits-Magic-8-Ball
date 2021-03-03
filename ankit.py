# This pulls randint, the function you need, directly from random, simplifying usage. Saying as means you don't have
# to type randint each time, just rn.
from random import randint as rn

# This section gathers the input and makes an answer variable
name = input('Enter Name: ')
question = input('Enter question: ')
answer = ''

# This gets the random number
ANSID = rn(1, 9)

if ANSID == 1:
    answer = 'Yes, definitely'
if ANSID == 2:
    answer = 'It is decidedly so'
if ANSID == 3:
    answer = 'Without a doubt'
if ANSID == 4:
    answer = 'Reply hazy, try again'
if ANSID == 5:
    answer = 'Ask again later'
if ANSID == 6:
    answer = 'Better if I do not tell you now.'
if ANSID == 7:
    answer = 'Outlook not so good'
if ANSID == 8:
    answer = 'My sources say no'
# Here, the elif combines if and else. So if there is a number that's not 1 - 9, it will output this. Putting
# multiple could lead to errors.
elif ANSID == 9:
    answer = 'very doubtful'


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
