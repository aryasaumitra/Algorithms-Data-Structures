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
        7. Find a Value

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

    def __insertStart(self,value):
        
        newnode = Node(value)

        print('\nList Prior to adding:'+str(value)+'\n')

        self.printNodes()

        newnode.right = self.head.right
        newnode.left = self.head
        self.head.right = newnode
        oldNode = newnode.right
        oldNode.left = newnode

        print('\nList After adding:'+str(value)+'\n')

        self.printNodes()

    def __insertEnd(self,value):
        
        newnode = Node(value)
        print('\nList Prior to adding:'+str(value)+'\n')
        self.printNodes()

        righttravelPointer = self.head
        while righttravelPointer.right is not None:
            righttravelPointer = righttravelPointer.right

        righttravelPointer.right = newnode
        newnode.left = righttravelPointer

        print('\nList After adding:'+str(value)+'\n')
        self.printNodes()

    def __insertMiddle(self,value):
        pass


    def insertNode(self,value,location,after = None):
        if location == 'Start':
            self.__insertStart(value)

        elif location == 'End':
            self.__insertEnd(value)

        elif location == 'Mid':
            self.__insertMiddle(value)
        
        else:
            print('Enter Correct Location')

    def __deleteStart(self,value):
        print('\nList Prior to deleting:'+str(value)+'\n')
        self.printNodes()

        currentStart = self.head.right
        self.head.right = currentStart.right
        currentStart.right.left = self.head

        currentStart.left = None
        currentStart.right = None

        del currentStart

        print('\nList After deleting:'+str(value)+'\n')
        self.printNodes()

    def __deleteEnd(self,value):
        
        rightTravelPointer = self.head.right
        print('\nList Prior to deleting:'+str(value)+'\n')
        self.printNodes()

        while rightTravelPointer.right is not None:
            prevNode = rightTravelPointer
            rightTravelPointer = rightTravelPointer.right

        prevNode.right = None

        rightTravelPointer.left = None

        del rightTravelPointer

        print('\nList After deleting:'+str(value)+'\n')
        self.printNodes()
        
    def __deleteMid(self,value):
        pass

    def deleteNode(self,value):

        pass



values=[2,3,5,6,7,8,9]

doubleLinkedList = DoubleLinkedList(values)

doubleLinkedList.printNodes()


