import unittest

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        match = 0
        stack = []
        stack.append(-1)
        for j in range(len(s)):
            i = s[j]
            if( i == '('):
                stack.append(j)
            elif i ==')':
                stack.pop()
                if len(stack) != 0:
                    match = max(match, j - stack[len(stack)-1])
                else:
                    stack.append(j)
        return match

class TestUM(unittest.TestCase):
 
    def setUp(self):
        self.s = Solution()
 
    def testBaseCase(self): 
        self.assertEqual(self.s.longestValidParentheses("") , 0)
        self.assertEqual(self.s.longestValidParentheses("(") , 0)
        self.assertEqual(self.s.longestValidParentheses(")") , 0)
        self.assertEqual(self.s.longestValidParentheses("((((") , 0)
        self.assertEqual(self.s.longestValidParentheses("))))") , 0)
        self.assertEqual(self.s.longestValidParentheses("><") , 0)
        
    def testlongestValidParentheses(self): 
        self.assertEqual(self.s.longestValidParentheses("()") , 2)
        self.assertEqual(self.s.longestValidParentheses("()()") , 4)
        self.assertEqual(self.s.longestValidParentheses("(()()") , 4)
        
if __name__ == '__main__':
    unittest.main()
