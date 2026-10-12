class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        nextNode = self.head
        for i in range(index):
            if nextNode == None:
                return -1
            else:
                nextNode = nextNode.next
        return nextNode.val if nextNode else -1

    def insertHead(self, val: int) -> None:
        if self.head == None and self.tail == None:
            self.head = Node(val)
            self.tail = self.head
        elif self.head == None:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
        

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            return
        else:
            newNode = Node(val)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            self.tail = newNode

        

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head == None:
                self.tail = self.head
            return True
        curr = self.head
        if self.tail == None:
            self.head = None
            return True
        else:
            for i in range(index-1):
                if curr == None:
                    return False
                curr = curr.next
            if (curr == None or curr.next == None):
                return False
            if (curr.next == self.tail):
                curr.next = None
                self.tail = curr
                return True
            if (curr.next == self.head):
                self.head = curr.next.next
                return True

            else:
                curr.next = curr.next.next
                return True
        

    def getValues(self) -> List[int]:
        newList = []
        curr = self.head
        while curr:
            newList.append(curr.val)
            curr = curr.next
        return newList

        
