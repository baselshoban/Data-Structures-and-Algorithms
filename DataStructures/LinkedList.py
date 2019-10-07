class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        element = self.head
        counter = 1
        
        if position < 1:
            return None
            
        while element and counter <= position:
            if counter == position:
                return element
            element = element.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        element = self.head
        counter = 1

        if position > 1:
            while element and counter < position:
                if counter == position -1:
                    new_element.next = element.next
                    element.next = new_element
                element = element.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        
        if current.value == value:
            self.head = self.head.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next