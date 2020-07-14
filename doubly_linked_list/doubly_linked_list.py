"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    # call delete on the node instance itself to use in remove methods of list (?)
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        # increment the DLL length
        new_node = ListNode(value)
        self.length += 1
        # check if the DLL is empty
        # if it's empty 
        if self.head and self.tail is None:
            #  set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        # if DLL not empty
        else:
            # set new node's next to current head
            current = self.head
            new_node.next = current
            # set head's prev to new node
            self.head.prev = new_node.value
            # set head to the new node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store value of the head
        # decrement the length of DLL
        # delete the head
            # if next is not None
                # deal with next nodes prev value
                # needs to point to the prev of the node being removed
                # SET head.next prev to self's prev (ignores self node)
                # SET head to head.next
                # set self.tail to none ??
            # else (if head.next is None)
                # set head to None
                # set tail to None
        # return the value
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        # increment the DLL length

        # check if the DLL is empty
        # if it's empty 
            #  set head and tail to the new node instance
        # if DLL not empty
            # set new node's prev to current tail
            # set current tail's next to new node
            # set tail to the new node
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store value of the tail
        # decrement the length of DLL
        # delete the tail
            # if tail.prev is not None
                # deal with prev nodes next value
                # needs to point to the prev of the node being removed
                # SET tail.prev next to None (ignores self node)
                # SET tail to tail.prev
                # set self.prev to none ??
            # else (if tail.prev is None)
                # set head to None
                # set tail to None
        # return the value
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass