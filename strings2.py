#
parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])

# splitSpring = ("w\ne\n\nw\ni\nn")
#splitString = "we win"
#for i in range(1,6):
#  print(splitString[i])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3-14])
print(parrot[4-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])

# use the colon : to slice
print(parrot[0:6]) # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[:6])
        #  01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[:3])
# print(letters[-4:-12])
print(letters[16:13:-1])
# slice the string to produce edcba
print(letters[4::-1])
# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])
print(letters[25::-1])
print(letters[:])
print(letters[::])
empty = ""
print(empty[:10])

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for i in range(0, len(quote)):
    if quote[i].isupper():
        print(quote[i])

