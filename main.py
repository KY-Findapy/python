from queue import Queue


#O(1) operations
#constant time operation
def check_oddeven(number):
  count = 0
  num_iterations = 0

  if number % 2 == 0:
      num_iterations += 1
      print("%d is an even number" % number)

  else:
      num_iterations += 1
      print("%d is an odd number" % number)

  print("Total number of iterations: %d" % num_iterations)

def find_square(number):
    num_iterations = 0
    square = number ** 2

    num_iterations += 1

    print("Square of %d is %d \nTotal number of iterations is %d" % (number, square, num_iterations))

#O(n) operations
def check_prime1(number):

    num_iterations = 0
    for i in range(2, number):
        num_iterations += 1

        if number %i == 0:
            print("%d is not a prime number \n Total number of iterations is %d" % (number, num_iterations))

    print("%d is a prime number \n Total number of iterations is %d" % (number, num_iterations))

def check_prime2(number):

    num_iterations = 0

    mid_point = int(number / 2)

    for i in range (2, mid_point):
        num_iterations += 1

        if number %i == 0:
            print("%d is not a prime number \n Total number of iterations is %d" % (number, num_iterations))

    print("%d is a prime number \n Total number of iterations is %d" % (number, num_iterations))

#O(n) operations no.2
def find_maxval(num_list):

  maxval = num_list[0]
  num_iterations = 0

  for i in range(len(num_list)):
      num_iterations += 1

      if maxval < num_list[i]:
          maxval = num_list[i]

  print("Maximum value of the list = %d \nTotal number of iterations is %d" % (maxval, num_iterations))

def find_factorial(number:int):
    fact = 1
    num_iterations = 1

    if (number < 0 or type(number) != int):
        print("Invalid number!")
        return

    for i in range(fact, number+1):
        fact = fact * i
        num_iterations += 1

    print("The factorial of %d is %d \n Total number of iterations is %d" % (number, fact, num_iterations))

def two_for_loops(number):

    total = 0
    num_iterations = 0

    for i in range(number):
        num_iterations += 1
        total = total + i

    for i in range(100):
        num_iterations += 1
        total = total + i

    print("Total iterations are %d" % num_iterations)

#O(n * n ) operations
#Find permutations
def print_pairs(number_list):

    num_iterations = 0
    n = len(number_list)

    for i in range(n):
        for j in range(n):
            print(number_list[i], number_list[j])
            num_iterations += 1

    print("total iterations are %d" % num_iterations)

#Find prime number
def find_prime(lower, upper):
    num_iterations = 0

    for num in range(lower, upper):
      for i in range(2, int(num/2)):
        num_iterations += 1

        if num % i == 0:
            break

      else:
        print(num)

    print("total iterations are %d" % num_iterations)

def print_combination(n,m):

    num_iterations = 0

    for i in range(n):
        for j in range(m):
            print(i,j)
            num_iterations += 1

    print("total iterations are %d" % num_iterations)

###
### New Exercise: Queue
###

olympics = Queue(5)

#create custom queue
class myqueue:

#creates new queue
  def __init__(self):
    self.items = []

#verify if queue is empty
  def is_empty(self):
    return len(self.items) == 0

#add element to the back of queue
  def enqueue(self, items):
    return self.items.append(items)

#remove element from the front of queue
  def dequeue(self, items):
    return self.pop(0)

#return size of queue
  def size(self):
      return len(self.items)

#look at 1st element of queue
  def peek(self):
      if self.is_empty():
          raise Exception("Nothing to peek")

      return self.items[0]

#Linkedlist

class Node:
#node is a singly-linked list.

  def __init__(self, dataval=None, nextval=None):
    self.dataval = dataval
    self.nextval = nextval

  def __reduce__(self):
    return repr(self.dataval)

class Linkedlist:
  def __init__(self):

      self.head = None

#creats string representative of the data in a list
  def __repr__(self):

    nodes = []
    curr = self.head

    while curr:
        nodes.append(repr(curr))
        curr = curr.nextval
    return "[" + "->".join(nodes) + "]"

#Insert new element at the beginning of the list.
  def prepend(self, dataval):
      self.head = Node(dataval =dataval, nextval = self.head)

#insert a new element at the end of the list
  def append(self, dataval):
      if not self.head:
          self.head = Node(dataval = dataval)
          return

      curr = self.head

      while curr.nextval:
          curr = curr.nextval

      curr.nextval = Node(dataval=dataval)

#insert a new element after the node with middle_dataval
  def add_after(self, middle_dataval, dataval):

    if middle_dataval is None:
      print("Data to insert after not specified")
      return

    curr = self.head

    while curr and curr.dataval != middle_dataval:
      curr = curr.nextval

    new_node = Node(dataval = dataval)

    new_node.nextval = curr.nextval
    curr.nextval = new_node

#search for the first element with 'dataval' matching 'data'. Return element or none if not found
  def find(self, data):

      curr = self.head
      while curr and curr.dataval != data:
          curr = curr.nextval

      return curr

#Remove first occurence of 'data' in the list
  def remove(self, data):
    curr = self.head
    prev = None

    while curr and curr.nextval != data:
        prev = curr
        curr = curr.nextval

    if prev is None:
        self.head = curr.nextval
    elif curr:
        prev.nextval = curr.nextval
        curr.nextval = None

#Reverse the list in place
  def reverse(self):
      curr = self.head

      prev_node = None
      next_node = None

      while curr:
          nextval = curr.nextval
          curr.nextval = prev_node

          prev_node = curr

          curr = nextval
      self.head = prev_node

#Reverse list in place using recursion
  def reverse_recursive(self):

      def recursive(curr,prev):
          if not curr:
              return prev

          nextval = curr.nextval
          curr.nextval = prev

          prev = curr
          curr = nextval

          return recursive(curr,prev)

      self.head = recursive(curr=self.head, prev=None)

#Count the number of nodes in the linked list
  def count_nodes(self):

      if (self.head == None):
          return 0
      else:
          curr = self.head
          count = 0
          while (curr != None):
              curr = curr.nextval
              count += 1

          return count

#Test validity of data structures
numbers = Linkedlist()
print(numbers)

numbers.append(2)
numbers.append(3)
print(numbers)

numbers.prepend(1)
print(numbers)

numbers.count_nodes()

## Sorting Algorithms
#Selection Sort Algorithm
#Time complex = o(n^2)

def print_list(num_list):
    print(num_list)

def selection_sort(original_list):

    length = len(original_list)

    for i in range(length):

        min_value_index = 1

        for j in range(i + 1, length):

            if original_list[min_value_index] > original_list[j]:
                min_value_index = j

        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i]

        print("Sorted till index: ", i)
        print_list(original_list)

    print("Sorted list: ")
    print_list(original_list)

#selection sort test
num_list = [32,12,42,75,78,5,32]
#selection_sort(num_list)

#Bubble Sort Algorithm
#Adapative
#Worst case time complexity = O(n2)
def bubble_sort(original_list):

    length = len(original_list)

    for i in range(length -1, 0, -1):

        for index in range(i):

            if original_list[index] > original_list[index + 1]:

                original_list[index + 1], original_list[index] = \
                  original_list[index], original_list[index + 1]

        print("Unsorted till index: ", i - 1)
        print_list(original_list)

student_marks = [21, 99, 67, 18, 5, 94, 76, 88, 83, 75]
#bubble_sort(student_marks)

#Insertion Sort Algorithm
#Worst case time complexity = O(n^2)
def insertion_sort(original_list):

    length = len(original_list)

    for i in range(0, length - 1):

        for j in range(i + 1, 0, -1):
            if original_list[j] < original_list[j - 1]:

                original_list[j], original_list[j - 1] = \
                  original_list[j - 1], original_list[j]

        print("Sorted till index: ", i)
        print_list(original_list)

a = [32, 23, 44, 37, 11, 66, 56, 65]
#insertion_sort(student_marks)

#Shell Sort Algorithm
#apply insertion sort on sublist
#Adapative | Divide and Conquer

def shell_sort(original_list):

    length = len(original_list)

    gap = length // 2

    while gap > 0:

        for i in range(gap, length):
            temp = original_list[i]

            j = i

            while j >= gap and original_list[j - gap] > temp:
                original_list[j] = original_list[j-gap]
                j -= gap

            original_list[j] = temp

            print("Gap: ", gap)
            print_list(original_list)

        gap = gap // 2

#shell_sort(student_marks)

#Merge Sort Algorithm
def merge_sort(original_list):
    if len(original_list) <= 1:
        return

    mid = len(original_list) // 2

    lefthalf = (original_list)[:mid]
    righthalf = (original_list)[mid:]

    merge_sort(lefthalf)
    print_list(lefthalf)

    merge_sort(righthalf)
    print_list(righthalf)

    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            original_list[k] = lefthalf[i]

            i = i + 1

        else:
            original_list[k] = righthalf[j]
            j = j + 1

    while i < len(lefthalf):
        original_list[k] = lefthalf[i]

        i = i + 1
        k = k + 1

    while j < len(righthalf):
        original_list[k] = righthalf(j)

        j = j + 1
        k = k + 1

#Quick Sort Algorithm
#Function 1
#pick pivot element and place it in its correct position
def partition(original_list, start_index, end_index):

    curr_index = start_index
    pivot = original_list[end_index]

    for i in range(start_index, end_index):

        if original_list[i] <= pivot:

            original_list[curr_index], original_list[i] = \
              original_list[i], original_list[curr_index]
            curr_index = curr_index + 1

    original_list[curr_index], original_list[end_index] = \
      original_list[end_index], original_list[curr_index]

    return curr_index

#Function no.2 --> main function
#pivot is placed in its correct spot
#elements to the left pibot <= pivot
def quick_sort(original_list, start_index, end_index):
    if start_index >= end_index:
        return

    pi = partition(original_list, start_index, end_index)

    print("Element in the right place: ", original_list[pi])
    print_list(original_list)

    quick_sort(original_list, start_index, pi - 1)

    quick_sort(original_list, pi + 1, end_index)

#Test algorithm
quick_sort(a, 0, len(a) - 1)