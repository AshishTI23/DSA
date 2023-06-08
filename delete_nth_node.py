# Delete nth node from linked list.

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

	def delete_node(self, position):
		i = 1
		curr = self.head
		if position == 1:
			self.head = curr.next
		else:
			while curr:
				i += 1
				next_node = curr.next
				prev = curr
				if i == position:
					prev.next = next_node.next
				else:
					curr = curr.next
					
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

# Print before deletion
linked_list.print_list()

linked_list.delete_node(2)

# Print after deletion
linked_list.print_list()



