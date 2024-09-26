name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("u got a chance to study, r u gonna study?(yes or no)\n ").lower()

if answer == "no":
    answer = input(
        "u've got offered to work for someone,r u gonna work?(yes or no)\n ")

    if answer == "yes":
        print("now u gotta work as a slave ur whole life if u don't make right decisions ")
    elif answer == "no":
        print("u r out of money and gonna die in the streets if u don't change ur mind")
    else:
        print('Not a valid option. You r stupid.')

elif answer == "yes":
    answer = input("u graduated n now u got a chance to work, r u gonna work?(yes or no)\n ")

    if answer == "no":
        print("u have no savings, so most probably u gonna die.")
    elif answer == "yes":
        answer = input("it's so hard to work, r u gonna get through it? (yes/no)?\n ")

        if answer == "yes":
            print("u got promoted, so now u gonna get rich!")
        elif answer == "no":
            print("u gonna die in the streets - u r weak.")
        else:
            print('Not a valid option. u r stupid.')
    else:
        print('Not a valid option. u r stupid.')

else:
    print('Not a valid option. u r stupid.')

print("Thank you, good luck in ur life", name)