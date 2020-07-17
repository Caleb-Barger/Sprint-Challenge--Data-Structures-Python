class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, current_node, prev):
        # recrsion is my frined here
        # 1 -> 2 -> 3
        # if a node after the last one exists
        if current_node:
            # store a refrence to the next node
            next_node = current_node.get_next()
            # have the current node point to the previous node
            current_node.set_next(prev)
            # call w/ next node being the current node
            # current node being the next node
            self.reverse_list(next_node, current_node)
        else:
            self.head = prev
            # print(self.head.value)


# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.reverse_list(list.head, None)




  

