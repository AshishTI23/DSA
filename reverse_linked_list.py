# Given a linked list determine if it has cycle in it.

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.next = None


class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	def push_at_begining(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def reverse(self):
		prev = None
		curr = self.head
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev


	def print_list(self):
		node = self.head
		while node:
			print(node.val)
			node = node.next



# Driver program
linked_list = LinkedList()
linked_list.push_at_begining(5)
linked_list.push_at_begining(4)
linked_list.push_at_begining(3)
linked_list.push_at_begining(2)
linked_list.push_at_begining(1)

# Print before reversing
linked_list.print_list()

linked_list.reverse()

# Print after reversing
linked_list.print_list()



