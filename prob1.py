# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
import argparse

parser = argparse.ArgumentParser(description="sum of multiples of 3 and 5 below a default of 1000 unless other argument passed in.")

parser.add_argument("-l", "--limit", type=int, default=1000)

args = parser.parse_args()

limit = args.limit

def three_five_mult(limit=1000):

	return sum([x for x in range(limit) if x % 3 == 0 or x % 5 == 0])


def Main():

	if args.limit:

		print(three_five_mult(limit=args.limit))

	else:

		print(three_five_mult())

	



if __name__ == "__main__":
	Main()

