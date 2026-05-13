class Node:
    '''
    An object to maintain values and pointers for Nodes in a Singly Linked List.
    '''
	def __init__(self, value):
		self.value = value
		self.next = None


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0


	def __repr__(self):
		parts = []
		current = self.head
		while current:
			parts.append(str(current.value))
			current = current.next
		parts.append('None')
		
		return (
			f'LinkedList('
			f'head={self.head},' 
			f'tail={self.tail},' 
			f'length={self.length},'
			f'parts={" -> ".join(parts)}'
		)


	def __str__(self):
		parts = []
		current = self.head
		while current:
			parts.append(str(current.value))
			current = current.next
		parts.append('None')
		return f'Parts= {" -> ".join(parts)}'


	def __len__(self):
		return self.length


	def prepend(self, value):
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


	def append_slow(self, value):
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


	def append_fast(self, value):
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


	def delete(self, value):
		''' 
		Delete all nodes with a given value. 
		O(n) time and O(1) space
		Time complexity cannot be reduced without a way to randomly access nodes.
		'''
		current = self.head
		previous = None

		if not current:
			return

		while current:
			if current.value == value:
				self.length -= 1
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
			else:
				previous = current
				current = current.next


	def count(self, target):
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


	def search(self, target):
		''' 
		Returns list of indicies where target is found in the list.
		O(n) time and O(1) space
		Time complexity cannot be reduced without a way to randomly access nodes.
		'''
		current = self.head
		counter = 0
		indicies = []

		if not current:
			return indicies

		while current:
			if current.value == target:
				indicies.append(counter)
			counter += 1
			current = current.next

		return indicies


	def to_list(self):
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
