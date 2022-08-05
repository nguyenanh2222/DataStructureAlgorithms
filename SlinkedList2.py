class Node:
    def __init__(self, info: int):
        self.info = info
        self.next = None

    def __str__(self):
        return self.info


class SLinkedList:
    def __init__(self):
        self.plist = None

    def __str__(self):
        temp = self.plist
        temp_str = ""
        while temp:
            temp_str += f"{temp.info}-->"
            temp = temp.next
        temp_str += "None"
        return temp_str

    def insert_head_node(self, x: Node):
        p: Node
        p = self.plist
        x.next = p
        self.plist = x

    def insert_tail_node(self, x: Node):
        p = self.plist
        while p:
            if p.next != None:
                p = p.next
            elif p.next == None:
                p.next = x
                x.next = None
                break

    def insert_pos_node(self, node: Node, pos):
        count = 0
        p = self.plist
        if p == None:
            return False
        while p:
            if count == pos-1:
                node.next = p.next
                p.next = node
                break
            count += 1
            p = p.next

    def delete_after(self, pre_node: Node):
        if



if __name__ == "__main__":
    ll = SLinkedList()
    ll.insert_head_node(Node(5))
    ll.insert_head_node(Node(6))
    ll.insert_head_node(Node(7))
    ll.insert_tail_node(Node(3))
    ll.insert_tail_node(Node(9))
    ll.insert_tail_node(Node(5))
    print(ll)
    ll.insert_pos_node(Node(1), 2)
    print(ll)
