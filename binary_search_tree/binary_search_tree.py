
import sys
sys.path.append('../queue_and_stack')
from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # this is a good example of a problem to use recursion on
        # <go left
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        #  >= go right

        # Return True if the tree contains the value
        # False if it does not

    def contains(self, target):
        # to search a given in bianry search tree we first comparit with too,
        # if the key is present at root, we return root.  If key is greater >= right is key
        # we recure for right subtree of root node. Other wise we recure for left subtree
        if self.value == target: #base case
            return True
        
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # go right undtil you can go right no further
        if not self.right:
            return self.value
        return self.right.get_max()
    '''
    return self.right.get_max() if self.right else self.value
    '''

    '''
    def get_max(self):
        # Go right until you can't go right any more
        while self.right is not None:
            self = self.right

        return self.value
    '''
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you cant anymore, then
        # go back and go right
        # in here somewhere, you want to call cb(node)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make queue
        # push root into queue
        # while queue not empty
            # if left
                # add left to back
            # if right
                # add right to back
                # pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #make stack
        # put the root in the stack
        # while stack is not empty
            #Pop the top item in the stack
            #look right
            #push right to the stack
            #look left
            #if there is a left, push to stack

        # call function on root
            #if left
                #call on left
            #if right
                #call on right
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
