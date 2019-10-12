"""HashTable stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash = self.calculate_hash_value(string)
        if self.table[hash]:
            self.table[hash].append(string)
        else:
            self.table[hash] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash = self.calculate_hash_value(string)
        if self.table[hash]:
            for item in self.table[hash]:
                if item == string:
                    return hash
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return (ord(string[0]) * 100) + ord(string[1])