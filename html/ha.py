class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        i = 1
        while current and i<4:
            print(current.data,end="->")
            current = current.next

            i+=1
        print(current.data)
ls = Linkedlist()
ls.append(1)
ls.append(3)
ls.append(3)
ls.append(4)
ls.display()