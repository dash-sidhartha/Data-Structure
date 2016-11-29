#!/usr/bin/env python  -- This makes it possible to run the file as a script invoking the interpreter implicitly

""" Introduction to Linked List """


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

if __name__ == '__main__':
	ll = LinkedList()
	ll.head = Node(3)
	ll.head.next = Node(2)
	ll.head.next.next = Node(1)
	ll.traverseList()