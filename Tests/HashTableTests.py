import sys
sys.path.append("../")

from DataStructures.HashTable import HashTable

try:
	print("\nStart Hash Table Tests ..")

	# Setup
	hash_table = HashTable()

	# Test calculate_hash_value
	# Should be 8568
	assert hash_table.calculate_hash_value('UDACITY') == 8568

	# Test lookup edge case
	# Should be -1
	assert hash_table.lookup('UDACITY') == -1

	# Test store
	hash_table.store('UDACITY')
	# Should be 8568
	assert hash_table.lookup('UDACITY') == 8568

	# Test store edge case
	hash_table.store('UDACIOUS')
	# Should be 8568
	assert hash_table.lookup('UDACIOUS') == 8568

	print("All Tests Pass Successfuly")

except AssertionError as e:
	print("Tests Fail")
except Exception as e:
	print("An Error Accoured")
	raise e