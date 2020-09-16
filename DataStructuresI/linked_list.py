# linear data structure made up of nodes and refs to the next node

# lets make some node class
class Node:
    def __init__(self, value, next_node = None):
        # A value that the node is holding
        self.value = value
        # A reference to the next node in the chain
        self.next_node = next_node

    def get_value(self): # This is a getter
        """
        Method to get the value of a node
        """
        return self.value

    def get_next(self): # This is a getter
        """
        Method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next): # This is a setter
        """
        Method to update the node's "next_node" to the new_next
        """      
        self.next_node = new_next


# now lets think of how we can make nodes interact in a way that consolidates their pieces together

# lets make a LinkedList class
# think of the idea of having a head and a tail like a snake 
# where the snake can grow based upon having more links in it

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a new node.
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the oist must have at least one item in there
        else:
            # update the last node's "next_node" to the new node
            self.tail.set_next(new_node) # (last node in chain).next_node = new_node
            # update the "self.tail" to point to the new node that we just added.
            self.tail = new_node

    def remove_tail(self):
        """
        Remove the last node in the chain and return its value
        """
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        # check if there's only 1 node
        if self.head == self.tail:
            # store the value of the node that we're going to remove
            value = self.tail.get_value()
            # remove the node
            # set the head and the tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        # otherwise
        else:
            # store the value of the node that we're going to remove
            value = self.head.get_value()
            # we need to set the "self.tail" to the second to Last node
            # we can only do this by traversing the whole list from beginning to end

            # starting form the head
            current_node = self.head

            # keep iterating unitl the node after "current_node" id the tail.
            while current_node.get_next() != self.tail:
                # keep looping
                current_node = current_node.get_next()
            # at the end of the iteration set "self.tail" to the current_node
            self.tail = current_node
            # set the new tail's "next_node" to None
            self.tail.set_next(None)
            # return value
            return value



    def remove_head(self):
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        if self.head == self.tail:
            # store value of the node that we are going to remove
            value = self.head


# This is how we could implement to call the linked list
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.set_next(n4)
n1.get_value() # => 2



# ===============================================
print(n1.get_next().get_value()) # => I'm using the methods getters and setters
print(f"{n1.next_node.value}, {n4}")  # I'm not using the methods, using the variables on the initializer.

# l = LinkedList()
# l.add_to_tail(4)
# print(l.tail.value)
# l.remove_tail()
# print(l.tail.value)
# print(l.tail)

