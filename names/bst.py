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
    def __init__(self, name=None):
        self.name = name
        self.left = None
        self.right = None

    # Insert the given name into the tree
    def insert(self, name):
        # compare input name with name of the Node
        # if name is < Node's name
        if len(name) < len(self.name):
            # go left
            # if there's no child to compare input name to
            if not self.left:
                # wrap the name in a BSTNode and park it
                self.left = BSTNode(name)
            # otherwise there is a child
            else:
                # call the left child's insert method
                self.left.insert(name)
        # otherwise name, >= Node's name
        else:
            # go right
            # if no right child wrap and park
            if not self.right:
                self.right = BSTNode(name)
            # otherwise thehe is a child
            else:
                # call right child's insert method
                self.right.insert(name)
    # Return True if the tree contains the name
    # False if it does not
    def contains(self, target):
        # 1. Base case
        if self.name == target:
            return True
        # 2. "How move closer to base case?"
        # compare target against name to determine direction
        if len(target) < len(self.name):
            # move left
            # is no left
            if not self.left:
                return False
            else:
                # call contains again on this child
                return self.left.contains(target) # using return becuase we are looking for some sort of answer
        else:
            # move right
            # is no right
            if not self.right:
                return False
            # is a right
            else:
                return self.right.contains(target)

    # Return the maximum name found in the tree
    def get_max(self):
        # RECURSIVE 
        # --------------------------
        if not self.right:
            return self.name

        return self.right.get_max()

        # ITERATION
        # --------------------------
        # current = self

        # while not current.right:
        #     current = current.right
        
        # return current.name

    # Call the function `fn` on the name of each node
    def for_each(self, fn):
        # call anon func on self.name
        fn(self.name)
        # if the node has a left child pass the anon func to it
        if self.left:
            self.left.for_each(fn)
        # if the node has a right child pass the anon func to it
        if self.right:
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT - depth first transversal (LIFO)
        # LIFO = STACK
        stack = []
        stack.append(self)

        # as long as the stack has nodes in it
        # there are more nodes to traverse
        while len(stack) > 0:
            current = stack.pop()

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            # call the anon func
            fn(current.name)

    def iterative_bredth_first_for_each(self, fn):
        from collections import deque
        # BFT: FIFO
        # queue data structure to do this
        queue = deque()
        queue.append(self)

        # continue to travel as long as there are more nodes
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            fn(current.name)

    # Part 2 -----------------------

    # Print all the names in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if node left than call self with node.left
        if node.left:
            self.in_order_print(node.left)
        # if not a node.right or is a node.right print self
        if not node.right or node.right:    
            print(node.name)
        # if node.right call self with node.right
        if node.right:
            self.in_order_print(node.right)

    # Print the name of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque

        queue = deque()
        queue.append(node)
        l = []

        while len(queue) > 0:
            current = queue.popleft()
            l.append(current.name)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)  

        l.sort()
        for n in l:
            print(n)
        
            

    # Print the name of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            c = stack.pop()
            print(c.name)

            if c.right:
                stack.append(c.right)
            if c.left:
                stack.append(c.left)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # 1. Visit the root.
            # print node.name
            print(node.name)
        # 2. Traverse the left subtree, i.e., call Preorder(left-subtree)
            if node.left:
                # call method with node.left
                self.pre_order_dft(node.left)
        # 3. Traverse the right subtree, i.e., call Preorder(right-subtree) 
            if node.right:
                # call method with node.right
                self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # LEFT -> RIGHT -> ROOT
        # Go left unitl you can't
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.name)

            



