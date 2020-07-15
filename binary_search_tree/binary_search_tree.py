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
        current = self
        max_value = self.value
        if current.right is None:
            return current.value
        else:
            while current.right:
                current = current.right
                max_value = current.value
        return max_value                


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


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
