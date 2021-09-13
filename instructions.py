

# Functions goes here...
def yes_no(question):
    valid = false
    while not valid:
            response = input("Have you played this game before ?").lower().strip()

            if response == "yes" or response == "y":
                response = "yes"
                return response
            elif response == "no" or response == "n":
                response = "no"
                return response
            else:
                print("Please answer yes / no")


# Main routine goes here...

show_instructions = ""
while show_instructions != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before ?").lower().strip()
    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error.

    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")
    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")
    else:
        print("Please answer yes/no")

