"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class StackNode:
    def __init__(self , value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

    def __repr__(self):
        return f"{self.value}"

class Stack:
    def __init__(self):
        # self.size = 0
        # self.storage = []
        self.head = None
        self.tail = None        


    def __len__(self):
        # return len(self.storage)
        node_count = 0
        node_marker = self.head
        while node_marker != None:
            node_count += 1
            node_marker = node_marker.next_node
        return node_count





    def push(self, value):
        # return self.storage.append(value)
        new_stack = StackNode(value)
        if not self.head:
            self.head = new_stack
            self.tail = new_stack
        else:
            self.tail.set_next(new_stack)
            self.tail = new_stack



    def pop(self):
        # if len(self.storage) > 0:
        #     removed = self.storage.pop()
        #     print(self.storage)
        #     return removed
        if self.head == None and self.tail == None:
            return None
        else:
            removed = self.head
            self.head = self.head.next_node
            removed.next_node = None
            return removed


