

'''
How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two “middle” nodes. You may not store the nodes in another data structure.
'''


#Do we have a tail, head?
    # We know the head
    # We do not know the tail

# UNDERSTAND

# how do you find and return the middle node of a singly linked list in one pass?
# You do not have access to the length of the list.
# We can keep variables, but not data structures 

# There can be multiple nodes with the same value

# PLAN

# Make an array with some nums in it

# find_middle = [1, 2, 3, 4, 5]
'''
# We need a function that only traverses onces
def find_middle(head):
    # define a slow and fast pointer.  
    # They will both be self.head, the first item in the list
    slow_pointer = head
    fast_pointer = head

    # A while loop will have while fast pointer is not None, the fast pointer is going to increment by next.next the slow will be .next.  When the loop has completed the slow will be half the value of the fast pointer.  
    while fast_pointer.next.next != None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
    
    # return slow_pointer
    return slow_pointer
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def find_middle(self.head):
        # define a slow and fast pointer.
        # They will both be self.head, the first item in the list
        slow_pointer = self.head
        fast_pointer = self.head

    # A while loop will have while fast pointer is not None, the fast pointer is going to increment by next.next the slow will be .next.  When the loop has completed the slow will be half the value of the fast pointer.
        while fast_pointer.next.next != None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        # return slow_pointer
        return slow_pointer
    


