print("PLease choose your option from the list below:\n "
               "1. Learn Python\n 2. Learn Java\n 3. Go swimming\n 4. Have dinner\n "
               "5. Go to bed\n 0. Exit\n")
choice = int(input("Your choice: "))
# while int(choice) > 0:
#     if int(choice) > 6:
#         print("Your choice is invalid, please try again")
#         print("PLease choose your option from the list below:\n "
#                 "1. Learn Python\n "
#                 "2. Learn Java\n "
#                 "3. Go swimming\n "
#                 "4. Have dinner\n "
#                 "5. Go to bed\n "
#                 "0. Exit\n")
#     else:
#         print("Your choice is " + choice)
#     choice = input("Your next choice is ")
# else:
#     print("quit")

while True:
    if choice == 0:
        print("You quit")
        break
    elif str(choice) in "12345":
        print("Your choice is {}".format(choice))
    else:
        print("Your choice is invalid, please try again")
        print("PLease choose your option from the list below:\n "
                "1. Learn Python\n "
                "2. Learn Java\n "
                "3. Go swimming\n "
                "4. Have dinner\n "
                "5. Go to bed\n "
                "0. Exit\n")
    choice = int(input("Your next choice is "))




