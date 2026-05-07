class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def get_length(self):
        return self.length


    def append(self, value):
        new_node = Node(value)
        end = self.tail
        self.length += 1

        if not end:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = end
        end.next = new_node
        self.tail = new_node


    def prepend(self, value):
        new_node = Node(value)
        start = self.head
        self.length += 1

        if not start:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = start
        start.previous = new_node
        self.head = new_node

    def to_list(self):
        result = []
        current = self.head

        while current:
            result.append(current.value)
            current = current.next

        return result
