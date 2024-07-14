"""
File: class_reviews.py
Name: DK
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


EXIT = -1


def main():
    """
    This program can record the grade of the class of SC001 & SC101, and indicate the highest, lowest and average of
    each class.
    """
    x = input("Which class? ").upper()
    if x == str(EXIT):
        print("No class scores were entered")
    else:
        maximum_sc001 = -1
        minimum_sc001 = -1
        total_sc001 = 0
        n_sc001 = 0
        maximum_sc101 = -1
        minimum_sc101 = -1
        total_sc101 = 0
        n_sc101 = 0
        while True:
            if x == str(EXIT):
                break
            elif x == "SC001":
                score = int(input("Score: "))
                if maximum_sc001 == -1:  # initial condition for the first data input
                    maximum_sc001 = score
                    minimum_sc001 = score
                elif score > maximum_sc001:
                    maximum_sc001 = score
                elif score < minimum_sc001:
                    minimum_sc001 = score
                total_sc001 += score
                n_sc001 += 1
            elif x == "SC101":
                score = int(input("Score: "))
                if maximum_sc101 == -1:  # initial condition for the first data input
                    maximum_sc101 = score
                    minimum_sc101 = score
                elif score > maximum_sc101:
                    maximum_sc101 = score
                elif score < minimum_sc101:
                    minimum_sc101 = score
                total_sc101 += score
                n_sc101 += 1
            x = input("Which class? ").upper()
        print("=============SC001=============")
        if n_sc001 != 0:
            print("Max (001): " + str(maximum_sc001))
            print("Min (001): " + str(minimum_sc001))
            print("Avg (001): " + str(total_sc001/n_sc001))
        else:
            print("No score for SC001")
        print("=============SC101=============")
        if n_sc101 != 0:
            print("Max (101): " + str(maximum_sc101))
            print("Min (101): " + str(minimum_sc101))
            print("Avg (101): " + str(total_sc101 / n_sc101))
        else:
            print("No score for SC101")


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
