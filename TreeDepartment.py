'''cấu trúc lại cây nhị phân sao cho mỗi node chứa 1 department
class Department:
  id: int
  name: str
  person_count: int

Viết hàm lấy ra cây con của department theo id (với department hiện tại là node root)
input: department id
output: tree
     de_1                                                          de_3
   /          \                                                       /       \
de_2     de_3          my_func(de_3)->     de_4      de_5
             /       \
          node(de=de_4)    de_5
Viết hàm tìm danh sách department có person_count nhỏ hơn department truyền vào
input: department_id
output: List[Department]'''


class Department:
    def __init__(self, id: int, name: str, person_count: int):
        self.id = id
        self.name = name
        self.person_count = person_count

    def __str__(self):
        return f"{self.id}-{self.name}-{self.person_count}"


class Node:
    def __init__(self, data: Department):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


class TreeDepartment:
    def __init__(self):
        self.root = None

    def insert_department(self, current: Node, insert_node: Department) -> bool:
        if current:
            if current.data.id == insert_node.id:
                return False
            if current.data.id > insert_node.id:
                return self.insert_department(current.left, insert_node)
            else:
                return self.insert_department(current.right, insert_node)
        current = Node(insert_node)
        self.root = current
        return True

    def print_tree(self) -> str:
        if self.root == None:
            return False
        if self.root:
            print(self.root.data)
        if self.root.left:
            self.root.left.print_tree()
        if self.root.right:
            self.root.right.print_tree()

    def search_id(self, current_node: Node, id: int):
        if current_node:
            if current_node.data.id == id:
                return current_node.data.id
            if current_node.data.id > id:
                return self.search_id(current_node.left, id)
            else:
                return self.search_id(current_node.right, id)
        return None

    def search_person_count_by_id(self, id: int):
        if self.root:
            print(self.root.person_count)
            return self.root.person_count
        if self.root.left:
            self.root.left.print_tree()
        if self.root.right:
            self.root.right.print_tree()

    def search_smaller_person_count(self, id: int):
        if id == None:
            raise Exception("invalid input")
        if self.root:
            print(self.root.person_count)
            if self.root and self.root.person_count < self.search_person_count_by_id(id):
                return self.root.id
            if self.root.left and self.root.left.person_count < self.search_person_count_by_id(id):
                print(self.root.left.person_count)
                return self.search_smaller_person_count(self.root.left.id)
            if self.root.right and self.root.right.person_count > self.search_person_count_by_id(id):
                print(self.root.right.person_count)
                return self.search_smaller_person_count(self.root.right.id)


if __name__ == '__main__':
    tree = TreeDepartment()
    current = Node(Department(1, "A", 75000))
    insert_node = Department(3, "C", 45000)
    tree.insert_department(current, insert_node)
    # tree.print_tree()
    # insert_node = Department(2, "B", 45550)
    # tree.insert_department(current, insert_node)
    # tree.print_tree()
    # insert_node = Department(4, "D", 99500)
    # tree.insert_department(current, insert_node)
    # tree.print_tree()
    # tree.search_id(tree.root, 3)
    # tree.print_tree()
    # current.print_tree()
    # tree.search_id(current, 1)
    # tree.search_id(current, 2)
