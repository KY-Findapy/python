#Binary Search
def binary_search(sorted_list, key):
    min_index = 0
    max_index = len(sorted_list) - 1

    while(min_index <= max_index):
        mid = (min_index + max_index) // 2

        if sorted_list(mid) == key:
            return mid
        elif sorted_list(mid) < key:
            min_index = mid + 1
        else:
            max_index = mid - 1

    return -1

num_list = [23, 25, 41, 45, 56, 66, 74, 81, 94, 99]
#binary_search(num_list, 81)
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None

        self.data = data

    def get_left_child(self):
        return self.left

    def set_left_child(self, left):
        self.left = left

    def get_right_child(self):
        return self.right

    def set_right_child(self, right):
        self.right = right

    def get_value(self):
        return self.data

    def set_value(self, value):
        self.data = value

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

def insert(head, node):

    if head == None:
        return node

    if node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), node))
    else:
        head.set_right_child(insert(head.get_right_child(), node))

    return head

A = Node(23)
B = Node(13)
C = Node(44)
D = Node(34)
E = Node(55)
F = Node(67)

head = insert(None, E)

head.print_tree()

insert(head, B)

head.print_tree()

insert(head, F)
head.print_tree()

def lookup(head, data):

    if head == None:
        return print("Value not found")

    if head.get_value() == data():
        return head

    if data <= head.get_value():
        return lookup(head.get_left_child(), data)
    else:
        return lookup(head.get_right_child(), data)

def print_node(node):
    if (node == None):
        print("Not Found!")

    print(node.get_value())

#value not found
#print_node(lookup(head, 12))

def min_value(head):
    current = head

    while(current.left != None):
        current = current.left

    return current.data

min_value(head)

def max_value(head):
    current = head

    #loop down to find rightmost leaf
    while(current.right != None):
        current = current.right

    return current.data

max_value(head)

insert(head, Node(100))

max_value(head)
