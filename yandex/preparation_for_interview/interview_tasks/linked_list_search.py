from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def _get_last(self):
        if self.head is None:
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        return last_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self._get_last()
        last_node.next = new_node


llist = LinkedList()

llist.append(1)
llist.append(27)
llist.append(9)
llist.append(14)
llist.append(15)
# [1 -> 27 -> 9 -> 14 -> 15]

slow_cursor = llist.head
fast_cursor = llist.head

while fast_cursor and fast_cursor.next:
    slow_cursor = slow_cursor.next
    fast_cursor = fast_cursor.next.next

print(slow_cursor.data)
