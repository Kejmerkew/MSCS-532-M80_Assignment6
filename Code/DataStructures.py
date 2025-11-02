# ----------------------------------------------------------
# 1. ARRAY IMPLEMENTATION
# ----------------------------------------------------------
class CustomArray:
    """Implements a simple dynamic array with basic operations."""

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def __repr__(self):
        return str(self.data)


# ----------------------------------------------------------
# 2. STACK IMPLEMENTATION (Using Array)
# ----------------------------------------------------------
class Stack:
    """Implements a stack (LIFO) using a Python list."""

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return str(self.stack)


# ----------------------------------------------------------
# 3. QUEUE IMPLEMENTATION (Using Array)
# ----------------------------------------------------------
class Queue:
    """Implements a queue (FIFO) using a Python list."""

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def __repr__(self):
        return str(self.queue)


# ----------------------------------------------------------
# 4. LINKED LIST IMPLEMENTATION
# ----------------------------------------------------------
class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Implements a singly linked list with basic operations."""

    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, key):
        """Delete the first occurrence of key in the list."""
        curr = self.head
        prev = None
        while curr:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next

    def traverse(self):
        """Return all node data as a list."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def __repr__(self):
        return " -> ".join(map(str, self.traverse()))


# ----------------------------------------------------------
# MAIN DEMONSTRATION
# ----------------------------------------------------------
if __name__ == "__main__":
    print("\n=== Demonstrating Elementary Data Structures ===\n")

    # Array demo
    arr = CustomArray()
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    arr.delete(1)
    print("Array:", arr)

    # Stack demo
    s = Stack()
    s.push(5)
    s.push(10)
    s.pop()
    print("Stack:", s)

    # Queue demo
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    print("Queue:", q)

    # Linked List demo
    ll = SinglyLinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.delete(20)
    print("Linked List:", ll)
