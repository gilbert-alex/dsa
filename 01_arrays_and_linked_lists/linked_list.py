class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


	def get_value(self):
		return self.value


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0


	def get_length(self):
		return self.length


	def prepend(self, value):
		'''
		O(1) time and O(1) space
		Because no traversal is necessary and self.head pointer is maintained.
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
				# self.tail wouldn't normally be here if only O(n) time 
				self.tail = new_node
				return
			else:
				current = current.next


	def append_fast(self, value):
		'''
		O(1) time and O(1) space
		Thanks to the use of self.tail pointer, no traversal is necessary.
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
		Delete all values in a list. 
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
				if not previous:
					self.head = current.next
					current = current.next
				else:
					previous.next = current.next 
					current = current.next
			else:
				previous = current
				current = current.next


	def search(self, target):
		''' 
		Returns count of the times target is found in the list.
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


	def to_list(self):
		result = []
		current = self.head
		while current:
			result.append(current.value)
			current = current.next
		return result


if __name__ == "__main__":
	pass
