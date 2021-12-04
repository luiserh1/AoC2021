def print_data(data, num):
	num_measurements = len(data)
	num = min(num, num_measurements)
	print("First {} (from a total of {}) measurements:".format(num, num_measurements))
	for depth_m in data[:num]:
		print(depth_m)


def get_processed_input(input_path, data):
	with open(input_path, "rt") as f:
		lines = f.readlines()
		data += [int(depth_m) for depth_m in lines]
		num_measurements = len(data)
		print_data(data, 10)


def part_a(data):
	increases = 0
	for i in range(1, len(data)):
		increases += (1 if data[i] > data[i-1] else 0)
	return increases


def part_b(data, window_size):
	increases = 0
	if window_size > len(data):
		return increases
	window_sum = sum(data[:window_size])
	for i in range(window_size, len(data)):
		last_window_sum = window_sum
		window_sum += data[i] - data[i - window_size]
		increases += (1 if window_sum > last_window_sum else 0)
	return increases


def main():
	data = []
	input_path = "input.txt"
	get_processed_input(input_path, data)
	num_measurements = len(data)

	sol_a = part_a(data)
	print("======================\nSOL A: [{}] increases out of {} steps".format(sol_a, num_measurements - 1))

	window_size = 3
	sol_b = part_b(data, window_size)
	print("======================\nSOL B: [{}] increases out of {} steps with a {}-sized window".format(
		sol_b, num_measurements -window_size , window_size))




if __name__=="__main__":
	main()