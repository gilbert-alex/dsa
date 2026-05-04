# Use this as a premitive to implement a LL backed stack using prepend
# Add a append to allow for a ll backed queue


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
	
	def __repr__(self):
		return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = None
		self.length = 0

	def prepend(self, value):
		new_node = Node(value)
		self.length += 1

		if not self.head:
			self.head = new_node
			return

		new_node.next = self.head
		self.head = new_node

	def append(self, value):
		pass

	def delete(self, value):
		current = self.head
		previous = None

		if not current:
			return

		#[40, 30, 20, 10]
		while current:
			if current.value == value:
				previous.next = current.next
			else:	
				previous = current
			current = current.next
		return	

	def search(self, value):
		pass

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

