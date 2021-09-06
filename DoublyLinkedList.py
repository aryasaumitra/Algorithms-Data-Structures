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
            self.__addNodes(listofvalues)

    def __addNodes(self,listofNodes):

        travelPointer = self.head
        
        for eachvalue in listofNodes:
            node=Node(eachvalue)

            travelPointer.right = node
            node.left = travelPointer
            travelPointer = travelPointer.right

    def printNodes(self):

        righttravelPointer = self.head

        print('\nList from Left to Right\n')
        while righttravelPointer is not None:

            if righttravelPointer.right is None:
                lefttravelpointer = righttravelPointer
            print(righttravelPointer.data,end = "->")
            righttravelPointer = righttravelPointer.right

        print("\nList from Right to Left\n")

        while lefttravelpointer is not None:

            print(lefttravelpointer.data,end = "<-")
            lefttravelpointer = lefttravelpointer.left



values=[2,3,5,6,7,8,9]

doubleLinkedList = DoubleLinkedList(values)

doubleLinkedList.printNodes()


