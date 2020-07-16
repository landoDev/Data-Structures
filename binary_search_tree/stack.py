from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()        

    def __len__(self):
        # return len(self.storage)
        return self.size

    def push(self, value):
        # return self.storage.append(value)
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # if len(self.storage) > 0:
        #     removed = self.storage.pop()
        #     print(self.storage)
        #     return removed
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        else:
            return None