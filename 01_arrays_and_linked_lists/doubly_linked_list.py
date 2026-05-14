from typing import Any, Optional


class Node:
    '''
    An object to maintain values and pointers for Nodes in a Doubly Linked List.
    '''
    def __init__(self, value: Any) -> None:
        self.value = value
        self.previous: Optional[Node] = None
        self.next: Optional[Node] = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0


    def __repr__(self):
        parts = [str(v) for v in self.to_list()]
        parts.append('None')

        return (
            f'LinkedList('
            f'head={self.head},'
            f'tail={self.tail},'
            f'length={self.length},'
            f'parts={" -> ".join(parts)}'
        )


    def __str__(self):
        parts = [str(v) for v in self.to_list()]
        parts.append('None')
        return f'Parts= {" -> ".join(parts)}'


    def __len__(self):
        return self.length


    def prepend(self, value: Any) -> None:
        '''
        Add a new Node to the head of the linked list.
        O(1) time and O(1) space.
        No list traversal is necessary because a head pointer is maintained.
        '''
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


    def append(self, value: Any) -> None:
        '''
        Add a new Node to the tail of the linked list.
        O(1) time and O(1) space.
        No list traversal is necessary because a tail pointer is maintained.
        '''
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


    def delete_first(self, value: Any, from_end: bool = False) -> None:
        '''
        Delete the first occurance of a value starting from the linked list
        head, by default. search will start from the
        head of the linked list unless "from_end" is set to True.
        O(n) time and O(1) space.
        Time complexity cannot be reduced without a way to randomly access nodes.

        API Node: A separate delete_last method would be better than a bool
        flag to change behavior; but I wanted to try this with turnary operators
        and what the test suite would look like. 
        '''
        current = (self.head if not from_end else self.tail)

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
                current = (current.next if not from_end else current.previous)
        
        raise ValueError(f'{value} not found.')


    def delete_all(self, value: Any) -> None:
        '''
        Delete all nodes with a given value.
        O(n) time and O(1) space.
        Time complexity cannot be reduced without a way to randomly access nodes.
        '''
        current = self.head
        initial_length = self.length

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

        if self.length == initial_length:
            raise ValueError(f'{value} not found.')

    def count(self, target: Any) -> int:
        ''' 
        Returns count of the times target is found in the list.
        O(n) time and O(1) space
        Reducing time complexity would require maintaining an additinal data structure.
        '''
        current = self.head
        counter = 0

        if not current:
            return counter

        while current:
            if current.value == target:
                counter += 1
            current = current.next

        return counter


    def positions_of(self, target: Any) -> list[int]:
        ''' 
        Returns list of indices where target is found in the list.
        O(n) time and O(1) space
        Time complexity cannot be reduced without a way to randomly access nodes.
        '''
        current = self.head
        counter = 0
        indices = []

        if not current:
            return indices

        while current:
            if current.value == target:
                indices.append(counter)
            counter += 1
            current = current.next

        return indices


    def to_list(self) -> list[Any]:
        '''
        Returns a List of the LinkedList Node values.
        O(n) time and O(n) space
        '''
        result = []
        current = self.head

        while current:
            result.append(current.value)
            current = current.next

        return result


    def _build_parts(self) -> list[str]:
        #TODO: implement from __repr__ and __str__ and to_list()
        pass


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    print(dll)
    print(repr(dll))
    print(len(dll))
