FORWARD = 0
UP = 1
DOWN = 2


def print_data(data, num):
	num_commands = len(data)
	num = min(num, num_commands)
	print("TYPES:\nFORWARD -> 0\tUP -> 1\t DOWN -> 2\t")
	print("First {} (from a total of {}) commands:\n\nTYPE\t-\tDISTANCE\n=========================".format(
		num, num_commands))
	for full_command in data[:num]:
		print("{}\t-\t{}".format(full_command[0], full_command[1]))


def get_processed_input(input_path, data):
	"""The data is a List of Tuples where the first member represents the command and the second represents the distance"""
	with open(input_path, "rt") as f:
		lines = f.readlines()
		for line in lines:
			full_command = line.split(" ")
			distance = int(full_command[1])
			command_type = full_command[0]
			if command_type == "forward":
				data.append((FORWARD, distance))
			elif command_type == "up":
				data.append((UP, distance))
			elif command_type == "down":
				data.append((DOWN, distance))
		print_data(data, 10)


def part_a(data):
	h_pos = depth = 0
	for command in data:
		if command[0] == FORWARD:
			h_pos += command[1]
		elif command[0] == UP:
			depth -= command[1]
		elif command[0] == DOWN:
			depth += command[1]
	return h_pos * depth, h_pos, depth


def part_b(data):
	h_pos = depth = aim = 0
	for command in data:
		if command[0] == FORWARD:
			h_delta = command[1]
			h_pos += h_delta
			depth += h_delta * aim
		elif command[0] == UP:
			aim -= command[1]
		elif command[0] == DOWN:
			aim += command[1]
	return h_pos * depth, h_pos, depth, aim


def main():
	data = []
	input_path = "input.txt"
	get_processed_input(input_path, data)

	sol_a, h_pos_a, depth_a = part_a(data)
	print("======================\nSOL A: [{}] is the result of multiplying {} of depth and {} of horizonal position".format(
		sol_a, depth_a, h_pos_a))

	sol_b, h_pos_b, depth_b, aim = part_b(data)
	print("======================\nSOL B: [{}] is the result of multiplying {} of depth and {} of horizonal position.Final aim: {}".format(
		sol_b, depth_b, h_pos_b, aim))


if __name__=="__main__":
	main()