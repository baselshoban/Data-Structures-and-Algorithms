def recursion_fibonacci(position):
	if position < 0:
		return -1
	if position == 0 or position == 1:
		return position
	return recursion_fibonacci(position-1) + recursion_fibonacci(position-2)
