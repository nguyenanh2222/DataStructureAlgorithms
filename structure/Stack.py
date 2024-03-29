class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        temp = self.head.next
        temp_str = ""
        while temp:
            temp_str += f"{temp.value}-->"
            temp = temp.next
        return temp_str

    def getSize(self):
        return self.size

    def isEmty(self):
        return self.size == 0

    def peek(self):
        if self.isEmty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    # delete, print


if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f'Stack: {stack}')

    for i in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
