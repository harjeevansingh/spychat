# Let the spying begin xD
from spy_details import spy_age, spy_name, salutation, spy_rating

status_updates = ["Hey, there!!", "Available", "Sleeping"]


print("Welcome To The Spychat ")

# Knowing whether the spy wants default name
def_name = input("Would you like to continue with default  Spy profile? (y/n)")

if def_name.upper() == "N":
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

print("So, %s.%s, you are %d old with a %.1f rating." % (salutation, spy_name, spy_age, spy_rating))

# Giving messages acco. to the ratings
if spy_rating > 4.5:
    print("You are a Pro!!!")
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print("you are perfect!!!")
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print("You have it in you.")
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
        else:
            show_menu = False

def add_status(current_status_message):
    if current_status_message == None:
        print("You don't have any current status.")
    else:
        print("Your current status message is "+current_status_message)

    # Providing the old status updates
    status_change = input("Would you like to choose from old status updates?  (y/n)")
    if status_change.upper() == "Y":
        j = 1
        for i in status_updates:
            print(j, ". ", i)
            j += 1
        status_num = int(input("Select the position of the status from above list."))
        current_status_message = status_updates[status_num-1]
        print(current_status_message, " is the current status message.")
        return current_status_message
    else:
        current_status_message = input("Add the desired Status Message.")
        if len(current_status_message) > 0:
            print(current_status_message, " is the current status message.")
            status_updates.append(current_status_message)
            return current_status_message





app_menu(spy_name, spy_age, spy_rating)
