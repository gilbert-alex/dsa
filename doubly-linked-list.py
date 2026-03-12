# doubly linked list in python

class Node:
    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        new_node.previous_node = self.head
        self.head.next_node = new_node
        self.head = new_node


#-----
dll = DoublyLinkedList()
dll.insert(1)
print(dll.head)
dll.insert(2)
print(dll.head)
dll.insert(3)
print(dll.head)
