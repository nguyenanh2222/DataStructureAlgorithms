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

from collections.abc import Iterator


class Department:
    def __init__(self, id: int, name: str, person_count: int):
        self.id = id
        self.name = name
        self.person_count = person_count

    def __str__(self):
        return f"{self.id}-{self.name}-{self.person_count}"


class Node:
    def __init__(self, data: Department, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


class TreeDepartment:
    def __init__(self):
        self.root = None

    def insert_department(self, insert_node: Department) -> None:
        self.root = self._insert_department(self.root, insert_node)

    def _insert_department(self, current: Node, _insert_node: Department, parent: Node = None) -> Node:
        if current is None:
            current = Node(_insert_node, parent)
        else:
            if current.data.id > _insert_node.id:
                current.left = self._insert_department(current.left, _insert_node, current)
            elif current.data.id < _insert_node.id:
                current.right = self._insert_department(current.right, _insert_node, current)
            else:
                raise Exception(f"Node with insert node {_insert_node} already exists")
                # TH: current.data.id == _insert_node.id:
        # current = Node(_insert_node)
        return current

    def search_id(self, id) -> Node:
        return self._search_id(self.root, id)

    def _search_id(self, current_node: Node, id: int) -> Node:
        if current_node is None:
            raise Exception(f"Node with id {id} does not exist")
        else:
            if current_node.data.id > id:
                current_node = self._search_id(current_node.left, id)
            elif current_node.data.id < id:
                current_node = self._search_id(current_node.right, id)
        return current_node

    def _print_tree(self, node: Node):
        if node:
            self._print_tree(node.left)
            print(node.data)
            self._print_tree(node.right)

    def print_tree(self):
        return self._print_tree(self.root)

    def _smaller_tree(self, node: Node):
        if node:
            self._smaller_tree(node.left)
            print(node.data)
            self._smaller_tree(node.right)

    def smaller_tree(self, id: int):
        node = tree.search_id(id)
        return self._smaller_tree(node)

    def _person_count(self, node: Node, _list_person_count = []):
        if node:
            self._person_count(node.right, _list_person_count)
            self._person_count(node.left, _list_person_count)
            _list_person_count.append({"ID": node.data.id, "Person Count": node.data.person_count})
            return _list_person_count

    def smaller_person_count(self, id):
        list_smaller_person_count = []
        node = tree.search_id(self.root.data.id)
        pivot = tree.search_id(id).data.person_count
        list_person_count = self._person_count(node)
        for item in list_person_count:
            if item["Person Count"] > pivot:
                list_smaller_person_count.append(item)
        return list_smaller_person_count

if __name__ == '__main__':
    tree = TreeDepartment()
    tree.insert_department(Department(3, "A", 75000))
    tree.insert_department(Department(2, "D", 50500))
    tree.insert_department(Department(4, "E", 60000))
    tree.insert_department(Department(1, "F", 69000))
    tree.insert_department(Department(5, "G", 87000))
    # tree.print_tree()
    # tree.search_id(2)
    # t = tree.smaller_tree(4)
    # print(t)
    print(tree.smaller_person_count(4))


