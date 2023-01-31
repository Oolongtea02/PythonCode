low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
answer = int(input("Press ENTER to start, enter a number"))

#print(answer)
guesses = 1
while True:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    # high_low = input("My guess is {}. Should i guess higher or lower? "
    #                  "Enter h or l, or c if my guess was correct "
    #                  .format(guess)).casefold()
    print("My guess is {}. Should i guess higher or lower? "
                      "Enter h or l, or c if my guess was correct "
                      .format(guess))

    high_low = None

    if guess < answer:
        high_low = "h"
    elif guess > answer:
        high_low = "l"
    else:
        high_low = "c"

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        pass

    guesses = guesses + 1