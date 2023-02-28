# checks user response is yes / no to a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Displays the instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# checks users enter an integer between a low and high number
def num_check(question, low, high):
    error = "please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:

            response = int(input(question))

            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


played_before = yes_no("Have you played the "
                       "game before? ")

if played_before == "no":
    instructions()

print("Program continues")

how_much = num_check("How much would you "
                     "like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
