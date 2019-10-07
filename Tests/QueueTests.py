import sys
sys.path.append("../")

from DataStructures.Queue import Queue

try:
	# Setup
	q = Queue(1)
	q.enqueue(2)
	q.enqueue(3)

	# Test peek
	# Should be 1
	assert q.peek() == 1

	# Test dequeue
	# Should be 1
	assert q.dequeue() == 1

	# Test enqueue
	q.enqueue(4)
	# Should be 2
	assert q.dequeue() == 2
	# Should be 3
	assert q.dequeue() == 3
	# Should be 4
	assert q.dequeue() == 4
	q.enqueue(5)
	# Should be 5
	assert q.peek() == 5

	print("All Test Pass Successfuly")

except AssertionError as e:
	print("Test Fail")
except Exception as e:
	print("An Error Accoured: ")
	raise e
