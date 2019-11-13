from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # max number of nodes it can hold
        self.limit = limit
        # current number of nodes its holding
        self.size = 0
        # doubly linked list w/ key-value entries in correct order
        self.order = DoublyLinkedList()
        # fast access to node stored in cache
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Key is present
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None
        # Key is not present
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):  # {"item1": node} ---- node.value == {item1, 1}
        # cases to handle

        # does the key already exist in the cache
        if key in self.storage:
            # key is here so we should replace the value
            # yes?
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

            # no? //not necessary

            # are we at a cap or not
        if self.size == self.limit:
            # yes? -dump the oldest item
            # dumpt the oldest item
            # remove from head /order
            #########option 1#############
            # del self.storage[self.order.head.value[0]]
            # self.order.remove_from_head()

            ##############option 2###########
            # del self.storage[self.order.remove_from_head().value[0]] //had to take out .value
            del self.storage[self.order.remove_from_head()[0]]

            self.size -= 1
            # no?
        # how do we put stuff into the cache?

        # if cache not full and key not present
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1


'''
__init__:
# max number of nodes it can hold
        self.limit = limit
        # current number of nodes its holding
        self.size = 0
        # doubly linked list w/ key-value entries in correct order
        self.order = DoublyLinkedList()
        # fast access to node stored in cache
        self.storage = dictionary()

set:
# Add a key-value to the cache
            # need to

        # keep track of the newest add

        # keep track of the oldest add

        # if the cache is full, get rid of oldest add

        # update keys with newer values


set:
// When receiving an input, we check first if the input exists already in our LRU
// If the input exists, we update the value in the dictionary with the new given value
// then move the item to the tail (most recently accessed) of the linked list
// if the input does not exist in our LRU
// check if LRU is full
// if not full, add to dictionary
// then add to tail (most recently accessed) in the linked list
// finally, increment count by 1
// if LRU is full
// delete head of linked list
// add input to tail of linked list (most recently accessed)
// delete previous head of linked list (key) from the dictionary
// add new value to the dictionary

'''
