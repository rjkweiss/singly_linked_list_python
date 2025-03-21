
# Node class -- has value and next properties
class Node:
    def __init__(self, val):
        self._value = val
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    # returns the node at a given position e.g. position = 0 returns head node
    def get_node(self, position):

        # edge case: negative position or positions greater than current length
        if position < 0 or position >= self._length:
            return None

        current = self._head
        for _ in range(position):
            current = current._next

        return current

    # add a new node with value to linked list
    def add_to_tail(self, value):

        # create new node
        new_node = Node(value)

        # if tail is empty, set both the tail and head
        if not self._head:
            self._head = self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node

        # update length
        self._length += 1

    def add_to_head(self, value):
        # create new node
        new_node = Node(value)

        # empty head
        if not self._head:
            self._head = self._tail = new_node
        else:
            new_node._next = self._head
            self._head = new_node

        # update length
        self._length += 1

    def remove_head(self):
        # edge case: empty list
        if not self._head:
            return None

        # removed val
        removed_val = self._head._value

        # remove head node
        self._head = self._head._next

        # update tail if head is empty (list is empty)
        if not self._head:
            self._tail = None

        # updated length
        self._length -= 1

        return removed_val

    def remove_tail(self):
        # edge case:  list is empty
        if not self._head:
            return None

        # save value to be removed (current tail)
        removed_val = self._tail._value


        # if we have one node
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            # iterate to find
            current_node = self._head
            while (current_node._next != self._tail):
                current_node = current_node._next

            # set tail to curr
            current_node._next = None
            self._tail = current_node

        self._length -= 1
        return removed_val

    def __len__(self):
        return self._length

    def contains_value(self, target):
        current_node = self._head

        while (current_node):
            # if target is found, return immediately
            if (current_node._value == target):
                return True

            current_node = current_node._next

        # we exited the loop without returning, so target was not found
        return False

    def insert_value(self, position, value):
        # if position is invalid, return False
        if position < 0 or position > self._length:
            return False

        # if position is 0, insert at the head
        if position == 0:
            self.add_to_head(value)
            return True
        # add to tail
        elif position == self._length:
            self.add_to_tail(value)
            return True

        prev_node = self._head

        while prev_node and position > 1:
            # adjust position -- > 1 so that we stop at the node, right before insertion
            position -= 1
            prev_node = prev_node._next

        # create node to be inserted
        new_node = Node(value)

        # new node points to what prev node is pointing to
        new_node._next = prev_node._next

        # update prev node to point to the new node
        prev_node._next = new_node

        # update length
        self._length += 1
        return True

    # update a node's value if it is found in the linked list
    def update_value(self, position, value):
        # get node to be updated
        node = self.get_node(position)

        # return's false if the node at position has not been found
        if not node:
            return False

        # otherwise, update the value and return true
        node._value = value
        return True

    # removes node from any position that is valid (0 -> len(linked_list) - 1)
    def remove_node(self, position):
        # return none if position provided is invalid
        if position < 0 or position >= self._length:
            return None
        # remove from head
        elif position == 0:
            return self.remove_head()
        # remove from tail
        elif position == self._length - 1:
            return self.remove_tail()

        # remove from anywhere else in the linked list
        prev_node = self._head

        while prev_node and position > 1:
            position -= 1
            prev_node = prev_node._next

        # update the prev_node's next to its next's next
        removed_val = prev_node._next._value
        prev_node._next = prev_node._next._next

        self._length -= 1
        return removed_val

    # convert linked list to a str: node1 -> node2 -> Node for easy testing and debugging
    def __str__(self):
        if not self._head:
            return 'Empty List'

        # str to store the node's values: 1 -> 2 -> None
        linked_list = ''
        current_node = self._head

        while current_node:
            linked_list += str(current_node._value) + ' -> '
            current_node = current_node._next

        # add None to signal the end of list
        linked_list += 'None'

        return linked_list
