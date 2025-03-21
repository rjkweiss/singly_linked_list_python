# Singly Linked List in Python

This project implements a basic **singly linked list** data structure in Python with support for efficient additions/removals from both the head and tail. It includes operations like adding, removing, accessing nodes, and getting the length of the list.

## Features

- `add_to_head(value)` — Adds a node to the front of linked list
- `add_to_tail(value)` — Adds a node to the end of linked list
- `remove_head()` — Removes head node and returns its value
- `remove_tail()` — Removes tail node and returns its value
- `get_node(position)` — Gets a node at a specific position (0-based)
- `__len__()` — Returns the number of elements in the linked list
- `__str__()` — Returns a Python string (node1 -> node2 -> None)

---

## Node Structure

```python
class Node:
    def __init__(self, val):
        self._value = val
        self._next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

  
linked_list = LinkedList()

linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.insert_value(2, 3)
linked_list.add_to_tail(4)

print(f"Length: {len(linked_list)}")       # ➝ 4
print(str(linked_list))            # ➝ [2 -> 1 -> 3 -> 4 -> None]

print(linked_list.remove_head())           # ➝ 2
print(linked_list.remove_tail())           # ➝ 4

print(str(linked_list))            # ➝ [1 -> 3 -> None]

node = linked_list.get_node(1)

if node:
    print(node._value)  # ➝ 3
else:
    print("Position out of bounds")
```
## File Structure
`| linked_list.py` - Node and LinkedList class implementation with example usage
