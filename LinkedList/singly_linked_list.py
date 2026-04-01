class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


# Usage
ll = SinglyLinkedList()

ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()        # 10 20 30
print(ll.get_length())  # 3

ll.delete(20)
ll.display()        # 10 30
