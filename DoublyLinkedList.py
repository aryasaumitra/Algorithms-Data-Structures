#Program to Practice Doubly Linked List
"""
    Date: 04/09/2021
    Idea: To Practice Doubly Linked List
    Features to Add:
        1. Input a list of values and create a Linked List from the same.
        2. Find a value in a Linked List
        3. Delete a Value from Linked List
            1. Find what kind of value it is Start, Middle, End
            2. Apply Individual Logic
        4. Insert a value at end
        5. Insert a value at middle
        6. Insert a value at start

"""

class Node:

    def __init__(self,data) -> None:
        self.data=data
        self.right=None
        self.left=None

class DoubleLinkedList:

    def __init__(self,listofvalues=None):
        self.head=Node('Head')

        if listofvalues:
            self.addNodes(listofvalues)

    def addNodes(listofNodes):
        pass