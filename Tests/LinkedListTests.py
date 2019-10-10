import sys
sys.path.append("../")

from DataStructures.LinkedList import LinkedList,Element

try:
	print("Start LinkedList Tests ..")
	
	# Set up some Elements
	e1 = Element(1)
	e2 = Element(2)
	e3 = Element(3)
	e4 = Element(4)

	# Start setting up a LinkedList
	ll = LinkedList(e1)
	ll.append(e2)
	ll.append(e3)

	# Test cases
	
	# Should print 3
	assert ll.head.next.next.value == 3

	# Test get_position
	# Should print 3
	assert ll.get_position(3).value == 3

	# Test insert
	ll.insert(e4,3)
	# Should print 4 now
	assert ll.get_position(3).value == 4

	# Test delete
	ll.delete(1)
	# Should print 2 now
	assert ll.get_position(1).value == 2
	# Should print 4 now
	assert ll.get_position(2).value == 4
	# Should print 3 now
	assert ll.get_position(3).value == 3

	print("All Tests Pass Successfuly")

except AssertionError as e:
	print("Tests Fail")
except Exception as e:
	print("An Error Accoured: ")
	raise e
