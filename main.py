#### Lecture 1 ###

print("Welcome To The Spychat ")

# Knowing whether the spy wants default name
def_name = input("Would you like a new Spy Name? y or n")

if def_name == "y":
    spy_name = input("Choose Your SpyName")

else:
    # setting default spy name
    spy_name = "Spy Singh"


if len(spy_name) > 0:
    # now we will ask for the salutation
    salutation = input("What should be your salutation Mr or Ms ")
    print("Alright " + salutation + "." + spy_name + " I'd like to know a little bit more about you...")

else:
    print("You have to enter your name to proceed.")

# asking other details
spy_age = int(input("What is your age?"))

#default rating
spy_rating = 0.0

# checking the spy eligibility
if spy_age in range(13, 51):
    spy_rating = float(input("Enter your rating."))
else:
    print("Sorry you are not suitable to be a spy.")

# Giving messages acco. to the ratings
if spy_rating > 4.5:
    print("You are Pro!!!")
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print("you are Awesome!!!")
elif spy_rating >=2.5 and spy_rating <= 3.5:
    print("You have it in you.")
else:
    print("You need to improve.")

print("So, "+salutation+"."+spy_name+", you are "+str(spy_age)+" old with a "+str(spy_rating)+" rating.")





