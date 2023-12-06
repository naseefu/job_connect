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
        while current.next:
            print(current.data,end="->")
            current = current.next
        print("none")
ls = Linkedlist()
ls.append(1)
ls.append(2)
ls.append(3)
ls.display()