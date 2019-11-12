from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

'''
class Middle:

    def find_middle_number(self):
        # self.hare = hare
        # self.turtle = turtle

        hare = self.hare
        turtle = self.turtle

'''
'''
dll = DoublyLinkedList()


def find_middle_number(nums):
    hare = nums[0]
    turtle = nums[0]

    while hare:
        turtle = turtle.dll.next
        hare = hare.dll.next.next

    return turtle


# new_list = 1, 2, 3, 4, 6, 8, 12, 14, 16
# find_middle_number(new_list)
'''
