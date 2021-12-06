def print_data(data, num):
	num_numbers = len(data)
	num = min(num, num_numbers)
	print("First {} (from a total of {}) binary numbers:".format(num, num_numbers))
	for code in data[:num]:
		print(code)


def get_processed_input(input_path, data):
	"""The data is a square matrix. Each row is a binary number"""
	with open(input_path, "rt") as f:
		input = f.read()
		lines = input.split("\n")
		data += [[int(n) for n in word] for word in lines]
		print_data(data, 10)



def binary_to_decimal(binary):
	dec = 0
	exp = 0
	for digit in binary[::-1]:
		if digit:
			dec += 2**exp
		exp += 1
	return dec


def part_a(data):
	num_numbers = len(data)
	sums = [num for num in data[0]]
	#sums = data[0]
	for number in data[1:]:
		for i in range(len(number)):
			sums[i] += number[i]
	gamma_rate = [0 for i in range(len(sums))]
	epsilon_rate = [0 for i in range(len(sums))]
	for i in range(len(sums)):
		digit = sums[i]
		if digit > num_numbers / 2:
			gamma_rate[i] += 1
		else:
			epsilon_rate[i] += 1
	e_rate_dec = binary_to_decimal(epsilon_rate)
	g_rate_dec = binary_to_decimal(gamma_rate)
	return e_rate_dec * g_rate_dec, epsilon_rate, gamma_rate



def part_b(data):
	pass


def main():
	data = []
	input_path = "input.txt"
	get_processed_input(input_path, data)

	sol_a, epsilon_rate, gamma_rate = part_a(data)
	print("======================\nSOL A: [{}] is the result of multiplying {} ({}) of epsilon rate and {} ({}) of gamma rate".format(
		sol_a, epsilon_rate, binary_to_decimal(epsilon_rate),  gamma_rate, binary_to_decimal(gamma_rate)))


if __name__=="__main__":
	main()