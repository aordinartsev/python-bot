def greet(bot_name, birth_year): # add name and birth_year bot
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

def remind_name(): # add username
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

def guess_age(): # math example сalculation of the year of birth
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count(): # count to any number
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test(): #choise answer
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = input()
    while answer != "2":
        print("Please, try again.")
        answer = input()
    print('Completed, have a nice day!')

def end(): #end phrase
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # main programm
remind_name()
guess_age()
count()
test()
end()
