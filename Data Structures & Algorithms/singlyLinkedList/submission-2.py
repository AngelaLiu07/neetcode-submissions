class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:

        node = self.head
        for i in range(index):
            if node is None:
                return -1
            node = node.next
        return node.val if node else -1
        

    def insertHead(self, val: int) -> None:
        newNode = Node(val)

        if (self.tail is None):
            self.tail = newNode
        newNode.next = self.head
        self.head = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if (self.head is None and self.tail is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        

    def remove(self, index: int) -> bool:
        if index < 0 or self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        prev = self.head
        for i in range(index-1):
            if prev is None:
                return False
            prev = prev.next
        if prev is None or prev.next is None:
            return False
        if prev.next == self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

        

        

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        while node:
            values.append(node.val)
            node = node.next
        return values
        
