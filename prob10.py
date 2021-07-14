"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', "--num", default=2000000, type=int, help="number below which to find summation of all primes")

args = parser.parse_args()

def Main():

	num = args.num
	print(num)


if __name__ == "__main__":

	Main()