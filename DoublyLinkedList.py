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

    def __find(self,value):

        if self.head.right is not None:
            kindOfvalue=''
            travelPointer=self.head.right
            flag=-1
            if travelPointer.data == value:
                flag =1
                kindOfvalue='Start'
            while travelPointer is not None and flag==-1:
                if travelPointer.data == value and travelPointer.right is not None:
                    flag=1
                    kindOfvalue='Mid'
                    break
                elif travelPointer.data == value and travelPointer.right is None:
                    flag=1
                    kindOfvalue='End'
                    break
                travelPointer=travelPointer.right

            if flag != -1:

                #print('\nFound '+self.__find(value)['value']+': Type '+self.__find(value)['type'])

                return {
                    'value':value,
                    'type':kindOfvalue
                }
            else:
                # print('\nValue Not found')
                return -1

        else:
            # print('\nEmpty Linked List')
            return -2
    def findNode(self,value):

        if self.__find(value)!=-2:
            return print('\nFound '+str(self.__find(value)['value'])+' and Type '+str(self.__find(value)['type'])+'\n') if self.__find(value)!=-1 else print("Value not found")
        else:
            print("Empty Linked List")

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

    def __insertMiddle(self,value,after):
        
        newnode = Node(value)
        print('\nList Prior to adding:'+str(value)+'\n')
        self.printNodes()

        righttravelPointer = self.head.right

        while righttravelPointer.data != after:
            righttravelPointer = righttravelPointer.right

        newnode.right = righttravelPointer.right
        newnode.left = righttravelPointer
        righttravelPointer.right = newnode
        newnode.right.left = newnode

        print('\nList After adding:'+str(value)+'\n')
        self.printNodes()


    def insertNode(self,value,location,after = None):
        if location == 'Start':
            self.__insertStart(value)

        elif location == 'End':
            self.__insertEnd(value)

        elif location == 'Mid':
            if after == None or self.__find(after) == -1 or self.__find(after) == -2:
                print('After Value does not exist')
                self.printNodes()
            else:
                self.__insertMiddle(value,after)
        
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
        currentNode = self.head.right
        print('\nList Prior to deleting:'+str(value)+'\n')
        self.printNodes()

        while currentNode.data != value:
            prevnode = currentNode
            currentNode = currentNode.right

        nextnode = currentNode.right
        prevnode.right = nextnode
        nextnode.left = prevnode

        currentNode.right = None
        currentNode.left = None

        del currentNode

        print('\nList After deleting:'+str(value)+'\n')
        self.printNodes()

    def deleteNode(self,value):

        if self.head.right is not None:
            self.__find(value) != -1

            findvalue = self.__find(value)

            if findvalue['type'] == 'Start':
                self.__deleteStart()

            elif findvalue['type'] == 'End':
                self.__deleteEnd()

            else:
                self.__deleteMid(value)



values=[2,3,5,6,7,8,9]

doubleLinkedList = DoubleLinkedList(values)

doubleLinkedList.printNodes()


