
#prompt:
""" You are an expert Python programmer. Write a class for a basic singly linked list with the following methods:
1. insert(value): Inserts a new node with the given value at the end of the list.
2. delete(value): Deletes the first node with the given value from the list.
Make sure to include proper handling for edge cases, such as deleting from an empty list or deleting a value that does not exist in the list. Provide a simple demonstration of how to use the linked list class.
Here is a Python implementation of a basic singly linked list with the specified methods:"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        if not self.head:
            print("List is empty. Cannot delete.")
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print(f"Value {value} not found in the list.")

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print("Linked List:", " -> ".join(map(str, values)))

# Demonstration of the SinglyLinkedList class

linked_list = SinglyLinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.display()  # Output: Linked List: 10 -> 20 -> 30
linked_list.delete(20)
linked_list.display()  # Output: Linked List: 10 -> 30
linked_list.delete(40)  # Output: Value 40 not found in the list.
linked_list.delete(10)
linked_list.display()  # Output: Linked List: 30
linked_list.delete(30)
linked_list.display()  # Output: Linked List: