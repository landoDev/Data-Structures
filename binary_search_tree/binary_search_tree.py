"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass
        # Case 1: value is less than self.value
        if value < self.value:
            # if no left child, 
            if self.left is None:
                self.left = BSTNode(value)
            #   insert here
            # else
            else: 
                # repeat the process
                self.left.insert(value)
                # self.left.insert(value)  
        # Case 2: value is greater than OR EQUAl self.value
        elif value >= self.value:
        # EQUAL IS NOT WRITTEN IN STONE but tests here assume duplicates go to the right
            if self.right is None:
                # repeat inverse of left
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: if target is less than self.value
        if target < self.value:
            # if self.left is none it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
                # RETURNING RECURSIVE CALL BECAUSE:
                    # I want this value to be returned to the top of the method
                    # without it the boolean value True of False wouldn't be returned
        # case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # will only need the right side
        # iterate through the nodes using a loop constuct
        # if there isn't a right node return this value
        # my original solution
        # current = self
        # max_value = self.value
        # if current.right is None:
        #     return current.value
        # else:
        #     while current.right:
        #         current = current.right
        #         max_value = current.value
        # return max_value 

        # recursive approach
        if self.right is None:
            return self.value
        return self.right.get_max()               


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive solution
        # run fn on the current node
        fn(self.value)
        # check if there is a node on the left
        if self.left:
            self.left.for_each(fn)
        # check if there's a node on the right
        if self.right:
            self.right.for_each(fn)
        # otherwise do nothing else

    def __repr__(self):
        return f"{self.value}"

    # Part 2 -----------------------

    # USE ENQUEUE AND DEQUEUE METHODS (import them?)
    # stretch goal:
        # #preorder (postorder is opposite)

        # #visit logic
        # print(self.value)
        # # recurse left
        # self.left.fn()
        # # recurse right
        # self.right.fn()

        # #inorder
        # # recurse left
        # self.left.fn()
        # #visit logic
        # print(self.value)
        # # recurse right
        # self.right.fn()
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if current node is none
        # end of a recursion
        # (base case) return
        print("print ran")
        if node is None:
            return 
            
        
        # check if we can move left
        if self.left is not None:
            self.left.in_order_print(node.left)
        
        # visit the node by printing it's value
        print(node.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        from queue import Queue
        # use a queue to form a "line"
        # for the nodes to "get in"
        q = Queue()
        # start by placing the root in the queue
        q.enqueue(self)
        # need a while loop to iterate!!!
        # checking for: 
        # while length of queue is greater than 0 
        while q.size > 0:
            # dequeue item from item front of queue
            node = q.dequeue()
            # print that item
            print(node.value)
            # place left node in queue if not None
            if self.left is not None:
                next_node = self.left
                q.enqueue(next_node)
            # place right node in queue if not None
            if self.right is not None:
                next_node = self.right
                q.enqueue(next_node)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
   
    
    def dft_print(self, node):
        from stack import Stack
        # stack 
        # initialize an empty stack
        ref_stack = Stack()
        # push a root node onto the stack
        ref_stack.push(self)
        # need a while loop to manage the iteration
        # check for:
        # if stack is not empty, enter the while loop
        while ref_stack.size > 0:
            # pop top item off the stack
            this_node = ref_stack.pop()
            # print that item's value
            print(this_node)
            # if there is a right subtree
            # push right item onto the stack
            if self.right is not None:
                ref_stack.push(self.right.value)

            # if there is a left subtree
                # push left item onto the stack
            if self.left is not None:
                ref_stack.push(self.left.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
