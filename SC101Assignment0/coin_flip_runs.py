"""
File: coin_flip_runs.py
Name: DK
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	This program can show the user the coin flips with the number of runs input by users.
	"""
	print("Let's flip a coin!")
	num_run = int(input("Number of runs: "))
	roll1 = random.randrange(2)  # for the first data of the coin flip
	flip = ""
	if roll1 == 0:
		flip += "H"
	else:
		flip += "T"
	runs = 0
	cont = False
	while True:
		if runs == num_run:  # condition for the end
			print(flip)
			break
		roll2 = random.randrange(2)
		if roll1 == roll2:
			if cont is False:  # to check if it is the first time to meet continuous run.
				flip = judge(roll2, flip)
				runs += 1
				cont = True
			else:
				flip = judge(roll2, flip)
		else:
			flip = judge(roll2, flip)
			cont = False
		roll1 = roll2


def judge(roll2, flip):  # check roll2 is "H" or "T"
	if roll2 == 0:
		flip += "H"
	else:
		flip += "T"
	return flip


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
