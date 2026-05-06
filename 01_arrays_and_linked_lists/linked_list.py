# --- Future DSA Uses --- 
# Use this as a premitive to implement a LL backed stack using prepend
# Add a append to allow for a ll backed queue

#TODO: add append method and probably flip tests
#TODO: make sure that the delete method decrements the len counter

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __repr__(self):
		return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def prepend(self, value):
		new_node = Node(value)
		self.length += 1
		
		if not self.head:
			self.head = new_node
			return

		new_node.next = self.head
		self.head = new_node

	def append_slow(self, value):
		''' For DSA's sake, this will traverse the list and add to the tail.
			It's O(n).
		'''
		current = self.head
		
		if not current:
			self.head = Node(value)
			self.length += 1
			return

		while current:
			if not current.next:
				current.next = Node(value)
				self.length += 1
				return
			else:
				current = current.next

	def append_fast(self, value):
		''' DO NOT USE -- THIS IS INCOMPLETE
			Wanting to accomplish insertion at O(1) with a tail pointer.
			The issue is that the tail pointer will have to be updated \
			in a few different places (prepend, append_*, delete, ...) and this \
			will cause tightly coupled methods. My first thought is to isolate \
			the maintance of the tail pointer to a helper func but...
			- removing an element means the tail moves to previous node
			- this is a singly-linked list and does not track previous nodes
			- therefore, this is only accomplished with O(n) traversal which is pointless
			- stopping here and moving on to doubly-linked list. 
		'''
		new_node = Node(value)
		self.length += 1

		current = self.head

		if not current: 
			self.head = new_node
		else:
			self.tail = new_node


	def delete(self, value):
		''' Will delete all matched elements in list. '''
		current = self.head
		previous = None

		if not current:
			return

		while current:
			if current.value == value:
				if not previous:
					# if target is first element in list
					self.head = current.next
				else:
					# if any other element in list
					previous.next = current.next 
				self.length -= 1
			# keep stepping through
			previous = current
			current = current.next

	def search(self, target):
		''' Returns zero or a count of the times target is found in the list.
			I wanted to do something more useful like return an index of the \
			target's position but that isnt helpful if search is only \ 
			available in O(n).
			Without a doubly-linked list I can only linear search.
			I'll do something more meaningful with this in a double-linked list.
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

	def get_length(self):
		return self.length

	def to_list(self):
		result = []
		current = self.head
		while current:
			result.append(current.value)
			current = current.next
		return result


if __name__ == "__main__":
	ll = LinkedList()
	for i in [10, 20, 30, 40, 50]:
		ll.prepend(i)

	ll.delete(40)
	print(ll.to_list())

