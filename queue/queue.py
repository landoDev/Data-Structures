"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class QueueNode:
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

class Queue:
    def __init__(self):
        # self.size = 0
        # self.storage = []
        self.head = None
        self.tail = None     
    def __len__(self):
        # return len(self.storage)
        elements = 0
        node_element = self.tail
        while node_element != None:
            print(node_element)
            elements += 1
            node_element = node_element.next_node
        return elements        

    def enqueue(self, value):
        # return self.storage.insert(0, value)
        queue_node = QueueNode(value)
        next_head = self.head
        queue_node.next_node = next_head
        print(queue_node)
        self.head = value

    def dequeue(self):
        # if len(self.storage) > 0:
        #     return self.storage.pop()
        if not self.tail:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value        
