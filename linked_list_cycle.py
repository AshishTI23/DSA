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

	def has_loop(self):
		fast = slow = self.head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if fast == slow:
				return True

		return False

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

# creating loop
linked_list.head.next.next.next.next.next = linked_list.head


if linked_list.has_loop():
	print("Loop Detected !")
else:
	print("Loop not found !")
