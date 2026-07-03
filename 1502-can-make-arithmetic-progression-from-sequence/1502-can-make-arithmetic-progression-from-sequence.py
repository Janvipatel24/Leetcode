class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        print(arr)

        n = len(arr)
        difference = arr[1] - arr[0]

        for i in range(2,n):
            if arr[i] - arr[i-1] != difference:
                return False
        else:
            return True
        """
        :type arr: List[int]
        :rtype: bool
        """
        