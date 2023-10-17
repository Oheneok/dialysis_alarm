import math
def number_of_cans(length, width, coverage):
    num_cans = (length * width)/coverage
    return num_cans
run = True

while run:
    l = float(input("What is the length?"))
    w = float(input("What is the width?"))
    c = float(input("What is the coverage?"))

    Num_cans = number_of_cans(l, w, c)
    print(f"You will need {math.ceil(Num_cans)}")

    choice = input("Run again? (y/n):")

    if choice == 'y':
            run = run
    else:
        run = False


