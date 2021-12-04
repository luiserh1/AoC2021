def main():
	# Read and process the input
	data = []
	with open("input.txt", "rt") as f:
		lines = f.readlines()
		data = [int(depth_m) for depth_m in lines]
	num_measurements = len(data)

	# Print some data
	print("First 10 (from a total of {}) measurements:".format(num_measurements))
	for depth_m in data[:10]:
		print(depth_m)

	# Do the calculations
	increases = 0
	for i in range(1, num_measurements):  # REMEMBER: The second parameter is not included!
		increases += (1 if data[i] > data[i-1] else 0)

	# Print  the solution
	print("======================\nSOL: [{}] increases out of {} steps".format(increases, num_measurements - 1))


if __name__=="__main__":
	main()