class Node():
    def __init__(self):
        self.info = Node
        self.next = None

    def __str__(self):
        return str(self.info)


class SLinkedList():
    def __init__(self, plist: Node):
        self.plist = plist

    def __str__(self):
        str_temp = ''
        temp = self.plist
        while temp != None:
            str_temp += f"{temp}-->"
            temp = temp.next
        str_temp += "None"
        return str_temp

    def push(self, x):
        p = Node
        p.info = x
        p.next = self.plist
        self.plist = p




    def list_size(self):
        count = 0
        p = self.plist
        while p != None:
            count += 1
            p = p.next
        return count



if __name__ == "__main__":
    s_linked_list = SLinkedList(Node(info=3))
    print(s_linked_list.push(Node(info=4)))
    print(s_linked_list)
    print(s_linked_list.push(Node(info=5)))
    print(s_linked_list)
    print(s_linked_list.push(Node(info=6)))
    print(s_linked_list)









