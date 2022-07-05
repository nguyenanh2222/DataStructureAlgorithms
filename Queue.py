class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class Queue:
    # Mô phỏng hàng đợi(queue) dùng danh sách liên kết đơn (SLL)
    # queue la mot abstract data type (ADT), tuan theo phuong phap FIFO
    def __init__(self):
        # khoi tao danh sach
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        temp_str = ""
        while temp:
            temp_str += f"{temp.data}-->"
            temp = temp.next
        temp_str += "None"
        return temp_str

    def enQueue(self, new_node: int):
        # chen node co gia tri x vao cuoi head
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return new_node.data
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    def deQueue(self):
        # lay mot phan tu ra khoi queue
        if self.head == None:
            return self.head.data
        else:
            self.head.data = self.head.next.data
            self.head = self.head.next
    def front(self):
        # lay gia tri tai phan tu dau tien
        return self.head.data
    def rear(self):
        # lay gia tri cuoi trong queue
        while self.head:
            if self.head.next == None:
                return self.head.data
            else:
                self.head = self.head.next

    def isEmpty(self):
        # kiem tra hang doi rong
        if self.head is None:
            return True
        else:
            return False

    def sizeQueue(self):
        size = 0
        while self.head:
            size += 1
            self.head = self.head.next
        return size

    def deleteQueue(self):
        if self.head == None:
            return
        while self.head:
            self.head = self.head.next
            if self.head == None:
                return
            else:
                self.head.next = None

    def printQueue(self):
        node = self.head
        print(queue)


if __name__ == '__main__':
    queue = Queue()
    queue.isEmpty()
    _is_empty = queue.isEmpty()
    print(_is_empty)
    size = queue.sizeQueue()
    print(size)
    # queue.printQueue()
    add = queue.enQueue(1)
    print(add)
    size = queue.sizeQueue()
    print(size)
    queue.enQueue(2)
    queue.enQueue(3)
    # queue.rear()
    # queue.deQueue()
    # queue.deleteQueue()
    # queue.printQueue()
    # queue.front()
    # queue.deQueue()
    # print(queue)
    # queue.deleteQueue()
    # print(queue)
