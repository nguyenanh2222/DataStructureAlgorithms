class ReStack:
    def main_display(self, n: int):
        self.display(n - 1)

    def display(self, n: int):
        if n == 0:
            return False
        # print(n)
        self.display(n - 1)
        print(n)

    def main_cal_s(self, n: int):
        for n in range(n):
            n+=1
            print(self.cal_s(n))

    def cal_s(self, n: int):
        if n == 0:
            return False
        return self.cal_s(n-1) + n

    def main_even(self, n: int):
        if n == 0:
            return False
        print(self.find_even(n))
    def find_even(self, n: int):
        for i in range(n):
            if n % 2 == 0:
                return n
            
# // 1. In ra những số từ 1 - n
# 	// 2. In ra những số từ n - 1
# 	// 3. In ra những số chẵn từ 1 - n
# 	// 4. In ra những số lẻ từ (n - 1) - 1
# 	// 5. Tính tổng những số từ 1 - n
# 	// 6. Tính tổng những số lẻ từ 1 - n
# 	// 7. Tính tổng những số nguyên tố từ 1 - n.





if __name__ == "__main__":
    restack = ReStack()
    n = int(input("Input number: "))
    # restack.main_display(n)
    # restack.main_cal_s(n)
    restack.main_even(n)
