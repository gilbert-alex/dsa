# dsa: linked list in python

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)

		if not self.head:
			self.head = new_node
			return

		self.head.next = new_node
		self.head = new_node

	def get_length(self):
		print(self.data.length())




#-----
ll = LinkedList()
ll.append(1)
print(ll.head)
ll.append(2)
print(ll.head)
ll.append(3)
print(ll.head)
# ll.get_length()	# expect 3 but fails because there isnt a python primitive under this.


# This seems trivially similar to a Stack, just without \
# a contigious series of bits shared by the Nodes.
# I need to read more about this and see if there is a \
# better example of how this may be used as a primitive.
