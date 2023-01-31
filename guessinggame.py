import random

numberofguess = 0
highest = 10
answer = random.randint(1, highest)
# print(answer) # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    numberofguess += 1
    while True:
        guess = int(input("Please guess number between 1 and {}: ".format(highest)))
        if guess == 0:
            print("You quit")
            break
        if guess < answer:
            print("Please guess higher")
        elif guess > answer:
            print("Please guess lower")
        # guess = int(input("Please guess number between 1 and {}: ".format(highest)))
        else:
            print("Well done, you guessed it")
            break
        # else:
            # print("Sorry, you have not guessed correctly")



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#      print("You got it first time")

# tree1 = 'put your first tree name here'
# tree2 = 'put your second tree name here'
#
# # add the code to compare the trees
# if tree1 == tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different")
#
# x = 5
# y = 7
#
# if x > y:
#     print("x is greater than y")
# elif y > x:
#     print("y is greater than x")
# else:
#     print("x equals y")
#
# print(guess)