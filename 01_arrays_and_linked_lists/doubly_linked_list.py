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


    def to_list(self):
        result = []
        current = self.head

        while current:
            result.append(current.value)
            current = current.next

        return result


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


    def delete_first(self, value, from_end=False):
        current = self.head

        while current:
            if current.value == value:
                if not current.previous and not current.next:
                    self.head = None
                    self.tail = None
                elif not current.previous:
                    self.head = current.next
                    self.head.previous = None
                elif not current.next:
                    self.tail = current.previous
                    self.tail.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.length -= 1
                return
            else:
                current = current.next
        
        #TODO: replace this with an exception
        return 'value not found'


    def delete_all(self, value):
        current = self.head

        while current:
            if current.value == value:
                if not current.previous and not current.next:
                    self.head = None
                    self.tail = None
                elif not current.previous:
                    current.next.previous = None
                    self.head = current.next
                elif not current.next:
                    current.previous.next = None
                    self.tail = current.previous
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.length -= 1
                current = current.next
            else:
                current = current.next


