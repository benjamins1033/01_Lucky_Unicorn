show_instructions = input("Have you played this game" "before? ").lower()

if show_instructions == "yes":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")

else:
    print("Please answer yes / no")