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

    def find(self,value):

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

                print('\nFound '+str(value)+': Type '+str(kindOfvalue))

                return {
                    'value':value,
                    'type':kindOfvalue
                }
            else:
                print('\nValue Not found')
                return -1

        else:
            print('\nEmpty Linked List')
            return -1

    def __deleteStart(self,value):
        pass

    def __deleteEnd(self,value):
        pass

    def __deleteMiddle(self,value):
        pass

    def deleteValue(self,value):

        if self.head.next is not None:
            if self.find(value) !=-1:
                findValue=self.find(value)

                if findValue['type']=='Start':
                    self.__deleteStart(value)
                    self.printNodes()

                elif findValue['type']=='End':
                    self.__deleteEnd(value)
                    self.printNodes()

                else:
                    self.__deleteMiddle(value)
                    self.printNodes()
            else:
                print('\nValue not Found')
        else:
            print('\nList is Empty')

    def __insertStart(self,value):
        pass

    def __insertMiddle(self,value):
        pass

    def __insertEnd(self,value):
        pass

    def insertValue(self,value,location):
        pass





values=[2,3,5,6,7,8,9]

linkedList=LinkedList(values)

linkedList.printNodes()

linkedList.find(4)

linkedList.find(7)
                