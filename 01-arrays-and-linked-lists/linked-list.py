class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def __repr__(self):
		return str(self.data)


class LinkedList:
	def __init__(self):
		self.head = None
		self.length = 0

	def prepend(self, data):
		new_node = Node(data)
		self.length += 1

		if not self.head:
			self.head = new_node
			return

		new_node.next = self.head
		self.head = new_node

	def get_length(self):
		return self.length


if __name__ == "__main__":
	ll = LinkedList()
	print(ll.get_length())
	ll.prepend(50)
	print(ll.head)
	print(ll.get_length())

# This seems trivially similar to a Stack, just without \
# a contigious series of bits shared by the Nodes.
# I need to read more about this and see if there is a \
# better example of how this may be used as a primitive.
