class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        def num1():
            total = 0
            for i in range(1, n + 1):
                if i % m != 0:
                    total += i
            return total
        def num2():
            total = 0
            for i in range(1, n + 1):
                if i % m == 0:
                    total += i
            return total
        def diff():
            return num1() - num2()
        print(num1())
        print(num2())
        return diff()
