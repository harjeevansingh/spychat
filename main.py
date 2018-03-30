# Let the spying begin xD
from spy_details import spy

friends = []


print("Welcome To The Spychat ")

# Knowing whether the spy wants default name
def_name = input("Would you like to continue with default  Spy profile? (y/n)")

if def_name.upper() == "N":
    spy["name"] = input("Choose Your SpyName")
    if len(spy["name"]) > 0:
        # now we will ask for the salutation
        spy["salutation"] = input("What should be your salutation Mr or Ms ")
        print("Alright %s.%s I'd like to know a little bit more about you..." % (spy["salutation"], spy["name"]))

        # asking other details
        spy["age"] = int(input("What is your age?"))

        # checking the spy eligibility
        if spy["age"] in range(13, 51):
            spy["rating"] = float(input("Enter your rating."))
        else:
            print("Sorry you are not suitable to be a spy.")
            exit()
    else:
        print("You have to enter your name to proceed.")
        exit()
else:
    pass

print('''\nWelcome %s.%s to the Spy Chat. So, you are %d old with a %.1f rating.
        ''' % (spy["salutation"], spy["name"], spy["age"], spy["rating"]))

# Giving messages acco. to the ratings
if spy["rating"] > 4.5:
    print("According to your Spy Rating, You are a Pro!!!")
elif spy["rating"] > 3.5 and spy["rating"] <= 4.5:
    print("According to your Spy Rating, you are perfect!!!")
elif spy["rating"] >= 2.5 and spy["rating"] <= 3.5:
    print("According to your Spy Rating, You can do better.")
else:
    print("Sorry, %s your rating is too low to be a spy." % spy_name)
    exit()


def app_menu(spy_name, spy_age, spy_rating ):
    show_menu = True
    current_status_message = None

    # giving the menu options to the user
    menu_choices = "Select the option. \n 1. Add a Status Update \n 2. Add a Friend \n 3. Send a Secret Message \n 4. Read a Secret Message \n 5. Read chats from a 'User' \n 6. Close application"
    while show_menu:
        choice = input(menu_choices)
        if choice == "1":
            current_status_message = add_status(current_status_message)
        elif choice == "2":
            print("You have ", add_friend(), "friends.\n")
        else:
            show_menu = False


# Setting the status updates
status_updates = ["Hey, there!!", "Available", "Sleeping"]


def add_status(current_status_message):
    if current_status_message == None:
        print("You don't have any current status.")
    else:
        print("Your current status message is "+'"'+current_status_message+'"')

    # Providing the old status updates
    status_change = input("Would you like to choose from old status updates?  (y/n)")
    if status_change.upper() == "Y":
        j = 1
        for i in status_updates:
            print(j, ". ", i)
            j += 1
        status_num = int(input("Select the position of the status from above list."))
        current_status_message = status_updates[status_num-1]
        print('"'+current_status_message+'"', " is the current status message.\n")
        return current_status_message
    else:
        current_status_message = input("Add the desired Status Message.")
        if len(current_status_message) > 0:
            print(current_status_message, " is the current status message.\n")
            status_updates.append(current_status_message)
            return current_status_message
        else:
            print("Invalid status!!")
# Adding friends to the profile
#friends_name = []
#friends_rating = []
#friends_are_online = []


friend = {}


def add_friend():
    new_name = input("Enter the friend's name.")
    new_salutation = input("Salutation for friend's name.")
    friend["age"] = int(input("What's the friend's age?"))
    friend["rating"] = float(input("Enter the friend's rating."))
    friend["name"] = new_name+"."+new_salutation

    # checking the friend's eligibility
    if len(friend["name"]) > 0 and friend["age"] in range(13, 51) and friend["rating"] > spy["rating"]:
        friends.append(friend)
    else:
        print("Sorry, your friend is not eligible to be a spy. \n")
    return len(friends)


def select_a_friend():
    friend_num = 1
    for friend_name in friends:
        print("Enter the number for the respective friend.\n %d. %s" % (friend_num, friend_name))
        return input()


app_menu(spy["name"], spy["age"], spy["rating"])

