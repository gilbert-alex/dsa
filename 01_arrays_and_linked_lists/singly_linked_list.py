from typing import Any, Optional


class Node:
    def __init__(self, value: Any) -> None:
        '''
        An object to maintain values and pointers for Nodes in a Singly Linked List.
        '''
        self.value = value
        self.next: Optional[Node] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0


    def __repr__(self):
        # This isn't a true repr string but rather a debug string for this DSA case
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
        O(1) time and O(1) space
        No list traversal is necessary because a head pointer is maintained.
        '''
        new_node = Node(value)
        self.length += 1
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node


    def append_slow(self, value: Any) -> None:
        ''' 
        Add a new Node to the tail of the linked list.
        O(n) time and O(1) space
        Without using self.tail pointer, you must traverse the ll to append.
        '''
        new_node = Node(value)
        self.length += 1
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        current = self.head

        while current:
            if not current.next:
                current.next = new_node
                '''
                self.tail wouldn't typically be in an object that only supports
                O(n) time insertion; but, as this object is used for education
                and reference, I am maintaining the tail pointer here so that
                it does not go stale for other methods.
                '''
                self.tail = new_node
                return
            else:
                current = current.next


    def append_fast(self, value: Any) -> None:
        '''
        Add a new Node to the tail of the linked list.
        O(1) time and O(1) space
        No list traversal is necessary because a tail pointer is maintained.
        '''
        new_node = Node(value)
        self.length += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node


    def delete(self, value: Any) -> None:
        ''' 
        Delete first node with a given value. 
        O(n) time and O(1) space
        Time complexity cannot be reduced without a way to randomly access nodes.
        '''
        current = self.head
        previous = None

        if not current:
            raise ValueError('List is empty.')

            
        while current:
            if current.value == value:
                if not previous and not current.next:
                    self.head = None
                    self.tail = None
                    current = current.next
                elif not previous:
                    self.head = current.next
                    current = current.next
                elif not current.next:
                    previous.next = None
                    self.tail = previous
                    current = current.next
                else:
                    previous.next = current.next 
                    current = current.next
                self.length -= 1
                return
            else:
                previous = current
                current = current.next

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


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append_fast(1)
    sll.append_fast(2)
    print(sll)
    print(repr(sll))
    print(len(sll))
