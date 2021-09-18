class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'SLLNode object: data={}'.format(self.data)

    def get_data(self):
        """ Return the self.data attritbute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attritbute with new_data parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attritbute with new_next parameter."""
        self.next = new_next


class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return 'SLL object: head={}'.format(self.head)

    def is_empty(self):
        """ Returns True if the Linked List is empty otherwise it returns False."""
        return self.head is None

    def add_front(self, new_data):
        """Add a node whose data is the new_data argument to the front of the Linked List"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """This function traverses the Linked List and returns the integer value representing the number of nodes in
        the Linked Lists.

        Time Complexity is 0(n) because every node in the Linked List must be visited in order to calculate the size
        of the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None: # While there are still nodes left to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """It traverses the Linked List and returns True if the data searched for is present in one of the nodes
        otherwise, it returns False.


        Time Complexity is O(n) because the worst case scenario is that we have to go through every node to locate
        the node we are searching for.

        """
        if self.head is None:
            return "Linked List is empty. No Nodes to search."

        current = self.head
        while current is not None:
            # Two Cases we are looking for
            # The Node's data matches what we're looking for
            if current.get_data() == data:
                return True
            # The Node's data doesn't match
            else:
                current = current.get_next()
        return False

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument as its self.data variable. Returns
        Nothing.

        The time complexity is O(n) because in the worst case we have to visit every Node before we find the one we
        need to remove.
        """
        if self.head is None:
            return 'Linked List is empty. No nodes to remove.'

        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return 'A node with that data value is not present.'
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next())



