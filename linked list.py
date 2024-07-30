class Node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if (self.head):
            current=self.head
            while (current.next):
                current=current.next
                current.next=new_node
        else:
            self.head=new_node

    def printLL(self):
        current=self.head
        while (current):
            print(current.data)
            current=current.next

LL=LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()


