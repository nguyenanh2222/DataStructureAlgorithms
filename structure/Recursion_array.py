class RecursionArray:
    """doc stack: ngan xep, queue: hang doi"""

    def print_1(self, n):
        if n == 0:
            return
        print("So n: ", n)
        self.print_1(n - 1)

    def print_2(self, n):
        if n == 0:
            return
        self.print_2(n - 1)
        print("So n: ", n)

    def print_3(self, n):
        for i in range(n):
            if i % 2 != 0:
                return
            else:
                self.print_3(n-1)




if __name__ == "__main__":
    recursion_array = RecursionArray()
    print(recursion_array.print_3(10))
