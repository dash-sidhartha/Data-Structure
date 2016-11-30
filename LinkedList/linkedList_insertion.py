#!/usr/bin/env python  -- This makes it possible to run the file as a script invoking the interpreter implicitly

""" Insertion into Linked List from front, end and at a specific position"""


__author__ = "Sidhartha A. Dash"
__version__ = "1.0"
__email__ = "dash.sidhartha18@gmail.com"
__contact__ = "91- 943 77 822 01"

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def traverseList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def insertAtFirst(self, key):
		if self.head is None:
			self.head = Node(key)
		else:
			node = Node(key)
			temp = self.head
			self.head = node
			node.next = temp

	def insertAtEnd(self, key):
		if self.head is None:
			self.head = Node(key)
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = Node(key)

	def insertAtSpecificPos(self, key, pos):
		if pos == 1:
			temp = self.head
			self.head = Node(key)
			self.head.next = temp
		else:
			temp = self.head
			while temp and pos-1:
				prev = temp
				temp = temp.next
				pos = pos - 1

			if temp is None:
				pass
			else:
				new_node = Node(key)
				new_node.next = temp
				prev.next = new_node


if __name__ == '__main__':
	ll = LinkedList()

	# Insert at First
	ll.insertAtFirst(3)
	ll.insertAtFirst(2)
	ll.insertAtFirst(1)
	ll.traverseList()

	# # Insert at Last
	ll.insertAtEnd(1)
	ll.insertAtEnd(2)
	ll.insertAtEnd(3)
	ll.traverseList()

	# Insert at Specific Postion
	ll.insertAtSpecificPos(1, 1)
	ll.insertAtEnd(2)
	ll.insertAtEnd(3)
	ll.insertAtSpecificPos(4, 2)
	ll.insertAtSpecificPos(5, 3)
	ll.traverseList()