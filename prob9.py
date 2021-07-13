"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def Main():

	for i in range(1,500):
		for j in range(1,500):
			for k in range(1,500):
				if i + j + k == 1000:

					if i**2 + j**2 == k**2:

						print(i*j*k)


if __name__ == "__main__":

	Main()