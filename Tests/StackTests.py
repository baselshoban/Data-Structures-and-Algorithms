import sys
sys.path.append("../")

from DataStructures.LinkedList import Element
from DataStructures.Stack import Stack

try:
	print("\nStart Stack Tests ..")
	
	# Set up some Elements
	e1 = Element(1)
	e2 = Element(2)
	e3 = Element(3)
	e4 = Element(4)

	# Start setting up a Stack
	stack = Stack(e1)
	stack.push(e2)
	stack.push(e3)

	# Test cases
	assert stack.pop().value == 3
	assert stack.pop().value == 2
	assert stack.pop().value == 1
	assert stack.pop() == None

	stack.push(e4)
	assert stack.pop().value == 4

	print("All Tests Pass Successfuly")

except AssertionError as e:
	print("Tests Fail")
except Exception as e:
	print("An Error Accoured: ")
	raise e
