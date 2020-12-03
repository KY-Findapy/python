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

def insert(head, Node):

    if head == None:
        return Node

    if Node.get_value() <= head.get_value():
        head.set_left_child(insert(head.get_left_child(), Node))
    else:
        head.set_right_child(insert(head.get_right_child(), Node))

    return head

A = Node(45)
B = Node(2)
C = Node(33)
D = Node(54)
E = Node(25)
F = Node(68)
G = Node(72)
H = Node(81)
I = Node(23)

head = insert(None, E)
insert(head, B)
insert(head, C)
insert(head, A)
insert(head, I)
insert(head, G)
insert(head, F)
insert(head, D)
insert(head, H)
#head.print_tree()

def lookup(head, data):

    if head == None:
        return print("Value not found")

    if head.get_value() == data:
        return head

    if data <= head.get_value():
        return lookup(head.get_left_child(), data)
    else:
        return lookup(head.get_right_child(), data)


def print_node(Node):
    if (Node == None):
        print("Not Found!")

    print(Node.get_value())

#print_node(lookup(head, 68))

def min_value(head):
    current = head

    while(current.left != None):
        current = current.left

    return current.data

insert(head, Node(1))
min_value(head)

def max_value(head):
    current = head

    #loop down to find rightmost leaf
    while(current.right != None):
        current = current.right

    return current.data

print(min_value(head))
print(max_value(head))

insert(head, Node(100))
print(min_value(head))
print(max_value(head))


class MyQueue:

    def __init__(self):

        self.items = []

    def is_empty(self):

        return len(self.items) == 0

    def enqueue(self, item):

        self.items.append(item)

    def dequeue(self):

        return self.items.pop(0)

    def size(self):

        return len(self.items)

    def peek(self):

        if self.is_empty():
            raise Exception("Nothing to peek")

        return self.items(0)


def breadth_first(Node):

    if(Node == None):
        raise Exception("No root found")

    path = []
    queue = MyQueue()
    queue.enqueue(Node)

    while queue.size() > 0:
        current = queue.dequeue()

        path.append(current.data)

        if current.get_left_child() != None:
            queue.enqueue(current.get_left_child())

        if current.get_right_child() != None:
            queue.enqueue(current.get_right_child())

    return path

#print(breadth_first(E))

def pre_order(Node):
    path = []

    if Node:
        path.append(Node.data)

        path = path + pre_order(Node.get_left_child())
        path = path + pre_order(Node.get_right_child())

    return path

print(pre_order(E))

def in_order(Node):
    path = []

    if Node:
        path = path + in_order(Node.get_left_child())

        path.append(Node.data)

        path = path + in_order(Node.get_right_child())

    return path

#print(in_order(E))

def post_order(Node):
    path = []

    if Node:
        path = path + post_order(Node.get_left_child())
        path = path + post_order(Node.get_right_child())

        path.append(node.data)

    return path

#print(post_order(E))