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
        # check if the DLL is empty
        # if it's empty 
        new_node = ListNode(value)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if DLL not empty
        else:
            # set new node's next to current head
            current = self.head
            new_node.next = current
            # set head's prev to new node
            current.prev = new_node
            # set head to the new node
            self.head = new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store value of the head
        removed_head = self.head
        # decrement the length of DLL
        self.length -= 1
        # delete the head
        if removed_head.next is not None:
            new_head = removed_head.next
            # if next is not None
                # SET head.next prev to self's prev (ignores self node)
            new_head.prev = None
                # SET head to head.next
            self.head = new_head
                # set self.tail to none ??
            # else (if head.next is None)
        else:
            self.head = None
            self.tail = None
                # set head to None
                # set tail to None
        # return the value
        return removed_head.value
            
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
        new_node = ListNode(value)
        self.length += 1

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            new_node.prev = current
            self.tail = new_node            
            
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

        removed_tail = self.tail
        # decrement the length of DLL
        self.length -= 1
        if removed_tail.prev is not None:
            new_tail = removed_tail.prev
            new_tail.next = self.head.next 
                
            self.tail = new_tail
                # set self.tail to none ??
            # else (if head.next is None)
        else:
            self.head = None
            self.tail = None
                # set head to None
                # set tail to None
        # return the value
        return removed_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # set the current head
        current = self.head
        moving_node = node
        # if moving node has a next no prev
        if moving_node.prev is None:
            # return the node, already the head
            return self.head
        # if moving node has a prev and no next (end of the list)
        elif moving_node.next is None:
            # save value of the moving node
            moving_node.prev.next = None
            # set new node's next to current head
            moving_node.next = current
            # set head's prev to new node
            current.prev = moving_node.value
            # set head to the new node
            self.head = moving_node
            self.tail = moving_node.prev
        # if moving node has a next and prev
        else:
            # next to moving nodes prev
            moving_node.prev.next = moving_node.next
            # moving nodes next prev set to moving node prev
            moving_node.next.prev = moving_node.prev
            # set self.head to node
            moving_node.next = current
            # set head's prev to new node
            current.prev = moving_node.value
            # set head to the new node
            self.head = moving_node

                 
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # set the current tail
        current = self.tail
        moving_node = node
        # if moving node has a prev no next
        if moving_node.next is None:
            # return the node, already the tail
            return self.tail
        # if moving node has a next and no prv (front of the list)
        elif moving_node.prev is None:
            # save value of the moving node
            moving_node.next.prev = None
            # set new node's prev to current tail
            moving_node.prev = current
            # set head's prev to new node
            current.next = moving_node
            # set head to the new node
            self.tail = moving_node
            self.head = moving_node.next
        # if moving node has a next and prev
        else:
            # next to moving nodes prev
            moving_node.prev.next = moving_node.next
            # moving nodes next prev set to moving node prev
            moving_node.next.prev = moving_node.prev
            # set self.head to node
            moving_node.prev = current
            # set head's prev to new node
            current.next = moving_node.value
            # set head to the new node
            self.tail = moving_node

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
        # initialize the head
        current = self.head
        next_node = self.head.next
        max_value = self.head.value
        # while there is a next value
        while next_node is not None:
            current_value = current.value
             # compare that nodes value to max_value
            if current_value > max_value:
                 max_value = current_value         
        return max_value