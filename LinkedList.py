#Program to Practice Linked List
"""""
    Date: 13/07/2021
    Idea: To Practice Linked List
    Features to Add:
        1. Input a list of values and create a Linked List from the same.
        2. Find a value in a Linked List
        3. Delete a Value from Linked List
            1. Find what kind of value it is Start, Middle, End
            2. Apply Individual Logic
        4. Insert a value at end
        5. Insert a value at middle
        6. Insert a value at start

"""""

class Node:
    

    def __init__(self,data) -> None:
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self,listofValues=None) -> None:
        self.head=Node("Head")

        if listofValues:
            self.addNodes(listofValues)

    def addNodes(self,listOfValues):
        for eachvalue in listOfValues:
            node=Node(eachvalue)

            if self.head.next is None:
                self.head.next=node
            else:
                travelPointer=self.head.next
                while travelPointer.next is not None:
                    travelPointer=travelPointer.next
                travelPointer.next=node

    def printNodes(self):

        travelPointer=self.head.next

        if travelPointer is None:
            print('Empty Linked List')

        while travelPointer is not None:
            print(travelPointer.data,end='->')
            travelPointer=travelPointer.next

        print()

    def __find(self,value):

        if self.head.next is not None:
            kindOfvalue=''
            travelPointer=self.head.next
            flag=-1
            if travelPointer.data == value:
                flag =1
                kindOfvalue='Start'
            while travelPointer is not None and flag==-1:
                if travelPointer.data == value and travelPointer.next is not None:
                    flag=1
                    kindOfvalue='Mid'
                    break
                elif travelPointer.data == value and travelPointer.next is None:
                    flag=1
                    kindOfvalue='End'
                    break
                travelPointer=travelPointer.next

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
            
    def __deleteStart(self):
        currentNode=self.head.next
        self.head.next=currentNode.next

    def __deleteEnd(self):
        currentNode=self.head.next

        while currentNode.next is not None:
            prevNode=currentNode
            currentNode=currentNode.next

        prevNode.next=None


    def __deleteMiddle(self,value):
        currentNode=self.head.next

        while currentNode.data !=value:
            prevNode=currentNode
            currentNode=currentNode.next

        prevNode.next=currentNode.next

    def deleteValue(self,value):

        if self.head.next is not None:
            if self.__find(value) !=-1:
                findValue=self.__find(value)

                if findValue['type']=='Start':
                    self.__deleteStart()
                    print('List After Deletion')
                    self.printNodes()

                elif findValue['type']=='End':
                    self.__deleteEnd()
                    print('List After Deletion')
                    self.printNodes()

                else:
                    self.__deleteMiddle(value)
                    print('List After Deletion')
                    self.printNodes()
            else:
                print('\nValue not Found')
        else:
            print('\nList is Empty')

    def __insertStart(self,value):

        newNode=Node(value)
        currentStart=self.head.next
        newNode.next=currentStart
        self.head.next=newNode


    def __insertMiddle(self,value,after):
        
        newNode=Node(value)

        travelpointer=self.head.next

        while travelpointer.data != after:
            travelpointer=travelpointer.next

        newNode.next=travelpointer.next
        travelpointer.next=newNode

    def __insertEnd(self,value):
        
        newNode=Node(value)

        travelPointer=self.head.next

        while travelPointer.next is not None:
            travelPointer=travelPointer.next

        travelPointer.next=newNode

    def insertValue(self,value,location,after=None):
        
        if location=='Start':
            print('List Before Insertion')
            self.printNodes()
            self.__insertStart(value)
            print("List after Insertion")
            self.printNodes()

        elif location == 'End':
            print('List Before Insertion')
            self.printNodes()
            self.__insertEnd(value)
            print("List after Insertion")
            self.printNodes()

        elif location == 'Mid':
            if after == None or self.__find(after) == -1 or self.__find(after) == -2:
                print('After value does not exist')
                self.printNodes()
            else:
                print('List Before Insertion')
                self.printNodes()
                self.__insertMiddle(value,after)
                print("List after Insertion")
                self.printNodes()








values=[2,3,5,6,7,8,9]

linkedList=LinkedList(values)

linkedList.printNodes()

linkedList.findNode(4)

linkedList.findNode(7)

linkedList.deleteValue(6)

linkedList.insertValue(6,'Mid',8)
                