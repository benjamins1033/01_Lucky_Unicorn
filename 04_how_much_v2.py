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


how_much = num_check("How much would you"
                     "like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
