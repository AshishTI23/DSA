
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

	def palindrome_with_stack(self):
		stack = []
		curr = self.head
		while curr:
			stack.append(curr.val)
			curr = curr.next
		curr = self.head
		while curr:
			if stack.pop() != curr.val:
				return False
			curr = curr.next

		return True

	def print_list(self):
		node = self.head
		while node:
			print(node.val)
			node = node.next



# Driver program
linked_list = LinkedList()
linked_list.push_at_begining(1)
linked_list.push_at_begining(2)
linked_list.push_at_begining(3)
linked_list.push_at_begining(0)
linked_list.push_at_begining(1)

print(linked_list.palindrome_with_stack())



