import sys

def power_great(a, n):

	product = 1

	while n:

		if n & 1:
			product = product * a

		n >>= 1 # a = int(a / 2)
		a = a * a

	return product


def power(a, n):
	a = int(a)
	n = int(n)

	if a == 0:
		return 0
	if n < 0:
		return -1
	if n == 0:
		return 1
	if n == 1:
		return a

	a_power = []
	a_power.append(1) # a^0
	a_power.append(a) # a^1

	# 2^0, 2^1, 2^2, 2^4, 2^8
	binary_index = []
	binary_index.append(0)
	binary_index.append(1)

	num = 2
	accum = a * a

	'''
	Get binary_index of 2^power:
		 0, 2^0, 2^1, 2^2, 2^3
	power of a:
		 1, a^(2^0), a^(2^1), a^(2^2), a^(2^3)
	'''

	while n > num:
		binary_index.append(num)
		a_power.append(accum)
		accum *= accum
		num *= 2

	product = 1
	index = len(binary_index) - 1
	while n >= 1 and index > 0:
		if n < binary_index[index]:
			index -= 1
			continue

		times = int(n / binary_index[index])
		for i in range(times):
			product *= a_power[index]
		n = n % binary_index[index]

	return product



if __name__ == '__main__':
	a = int(sys.argv[1])
	n = int(sys.argv[2])

	print(power(a, n), pow(a, n), power_great(a, n))