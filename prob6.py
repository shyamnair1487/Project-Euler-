"""
The sum of the squares of the first ten natural numbers (1^2 + 2^2 + 3^2 + .... 10^2) is 385,

The square of the sum of the first ten natural numbers (1 + 2 + 3.....10)^2 is 55^2 = 3025,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025-385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--num", type=int, default=10, help="The number of natural numbers you want to compute")

args = parser.parse_args()


def sum_squared_difference(num):

	sum_square = sum([i**2 for i in range(1,num+1)])

	square_of_sum = (sum([i for i in range(1, num+1)]))**2

	return square_of_sum - sum_square

def Main():

	num = args.num

	print(sum_squared_difference(num))

	


if __name__ == '__main__':

	Main()