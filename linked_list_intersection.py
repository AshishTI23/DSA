# Intersection of two linked list


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

	def print_list(self):
		node = self.head
		while node:
			print(node.val)
			node = node.next

def intersection_of_two_linked_list(head1, head2):
	c1 = c2 = 0
	curr1 = head1
	curr2 = head2
	while curr1:
		c1 += 1
		curr1 = curr1.next
	while curr2:
		c2 += 1
		curr2 = curr2.next
	if c1 >= c2:
		d = c1 - c2
		curr1 = head1
		curr2 = head2
		for i in range(d):
			curr1 = curr1.next
	else:
		d = c2 - c1
		curr1 = head1
		curr2 = head2
		for i in range(d):
			curr2 = curr2.next
	while curr1 and curr2:
		if curr1 is curr2:
			return curr1
		else:
			curr1 = curr1.next
			curr2 = curr2.next
	return False



# driver program to test above function
head1 = Node(1);
head1.next = Node(2);
head1.next.next = Node(3);
head1.next.next.next = Node(4);
head1.next.next.next.next = Node(5);
head1.next.next.next.next.next = Node(6);
head1.next.next.next.next.next.next = Node(7);
# list2
head2 = Node(10);
head2.next = Node(9);
head2.next.next = Node(8);

# Creating intersection
head2.next.next.next = head1.next.next.next;



print(intersection_of_two_linked_list(head1, head2).val)

