# Let the spying begin xD
from spy_details import spy_age, spy_name, salutation, spy_rating

print("Welcome To The Spychat ")

# Knowing whether the spy wants default name
def_name = input("Would you like to continue with default  Spy profile? y or n")

if def_name == "n":
    spy_name = input("Choose Your SpyName")
    if len(spy_name) > 0:
        # now we will ask for the salutation
        salutation = input("What should be your salutation Mr or Ms ")
        print("Alright %s.%s I'd like to know a little bit more about you..." % (salutation, spy_name))
        # asking other details
        spy_age = int(input("What is your age?"))

        # checking the spy eligibility
        if spy_age in range(13, 51):
            spy_rating = float(input("Enter your rating."))
        else:
            print("Sorry you are not suitable to be a spy.")
            exit()

    else:
        print("You have to enter your name to proceed.")
        exit()


else:
    pass


# Giving messages acco. to the ratings
if spy_rating > 4.5:
    print("You are a Pro!!!")
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print("you are perfect!!!")
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print("You have it in you.")
else:
    print("You need to improve.")

print("So, %s.%s, you are %d old with a %.1f rating." % (salutation, spy_name, spy_age, spy_rating))









