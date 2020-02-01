'''
How do you reverse a singly linked list without recursion?  You may not store the list, or it’s values, in another data structure.  The linked list is constructed only using the class below.  You may modify the class as you see fit to solve the problem, but the list has already been constructed.

'''

# UNDERSTAND

# How do you reverse a singly linked list without recursion?

# You may not store the list, or it’s values, in another data structure.

# The linked list is constructed only using the class below.

# You may modify the class as you see fit to solve the problem, but the list has already been constructed.

#PLAN

# variables for currently is, previous value, next value

    #prev value =  None
    #current value = 
    # 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def reverse(self)
        current = self
        next_value = current.next
        current.next = None
        previous_value = None
        while next_value != None:
            previous_value = current
            current = next_value
            next_value = current.next

            
