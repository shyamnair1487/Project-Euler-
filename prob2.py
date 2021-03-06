# Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

import argparse 

parser =argparse.ArgumentParser()

parser.add_argument("-l", "--limit", type=int, default=4000000)

args = parser.parse_args()

limit = args.limit

def fib(limit):
    
    a = 1
    b = 2
    evens = [2]
    while b < limit:
        c = a + b
        if c > limit:
            break
        else:
            a = b
            b = c
            if b % 2 == 0:
                evens.append(b)
    return sum(evens)


def Main():

	print(fib(limit))



if __name__ == "__main__":

	Main()