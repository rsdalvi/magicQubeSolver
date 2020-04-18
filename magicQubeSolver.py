class Solution:
    def __init__(self, r1, r2, r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3

    def is_valid(self):
        sol = [self.r1, self.r2, self.r3]
        sol_digits = [i for row in sol for i in row]
        return all(i in sol_digits for i in range(1, 10))


class Row:
    solutions = []
    product_value = None

    def __init__(self, value):
        self.product_value = value

    def generate_solutions(self):
        for i in range(1, 10):
            for j in range(1, 10):
                for k in range(1, 10):
                    if i * j * k == self.product_value:
                        self.solutions.append((i, j, k))


class SolutionFinder:
    def find_soluiton(self):
        row1 = Row(54)
        row1.generate_solutions()
        row2 = Row(120)
        row2.generate_solutions()
        row3 = Row(56)
        row3.generate_solutions()

        column_products = (96, 180, 21)
        for r1 in row1.solutions:
            for r2 in row2.solutions:
                for r3 in row3.solutions:
                    if all(r1[i] * r2[i] * r3[i] == column_products[i] for i in range(0, 3)):
                        sol = Solution(r1, r2, r3)
                        if sol.is_valid():
                            return sol


if __name__ == '__main__':
    sol: Solution = SolutionFinder().find_soluiton()
    print(sol.r1, '\n', sol.r2, '\n', sol.r3)
