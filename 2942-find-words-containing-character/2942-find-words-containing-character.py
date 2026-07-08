class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        ans = []
        for i in range(len(words)):
            a  = find(words[i], x)
            if a != -1:
                ans.append(i)
        return ans
    def find(inputString, findChar):
    
        for i in range(len(inputString)):
            if findChar == inputString[i]:
                return i
        return -1
    
        