# Create a Node class to create a node
from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


# Create a LinkedList class
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

    def pop(self):
        if self.head:
            current_node = self.head
            next_node = current_node.next

            if not next_node:
                removed_item = current_node.data
                self.head = None
                return removed_item

            while current_node:
                if not next_node.next:
                    removed_item = current_node.next.data
                    current_node.next = None
                    return removed_item

                current_node = current_node.next
                next_node = current_node.next

            last_node = current_node
            return last_node
        else:
            raise Exception("Empty list")

    def len(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0

    def print(self):
        current_node = self.head
        print("[", end="")
        while current_node:
            print(current_node.data, end=" -> " if current_node.next else "")
            current_node = current_node.next
        print("]")


llist = LinkedList()

llist.append(1)
llist.append(27)
llist.append(9)

llist.print()

llist.pop()

llist.print()

llist.pop()

llist.print()

llist.pop()

llist.print()
