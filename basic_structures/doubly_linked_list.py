class DLList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    class Fifo:
        def __init__(self):
            self.head = None
            self.tail = None

        def insert_deque(self, data):
            node = DLList.Node(data)
            if not self.head:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node

        def delete_deque(self):
            self.tail = self.tail.prev
            if not self.tail:
                self.head = None
            else:
                self.tail.next = None

        def print_list(self):
            temp = self.head
            print("None", end="<->")
            while temp:
                print(temp.data, end="<->")
                temp = temp.next
            print("None")

        def insert_i(self, i, data):
            temp = self.head
            for j in range(i):
                temp = temp.next

            node = DLList.Node(data)
            node.prev = temp.prev
            node.next = temp
            if temp.prev:
                temp.prev.next = node
            else:
                self.head = node
