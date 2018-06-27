class Solution(object):
    def isPalindrome(self, x):
        y = str(x)[::-1]
        if y == str(x):  return True
        return False
        
