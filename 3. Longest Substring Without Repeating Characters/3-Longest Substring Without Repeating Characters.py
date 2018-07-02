class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = []
        length = 0
        maxi = 0
        for i in s:
            if i not in l:
                l.append(i)
                length += 1
                if maxi <= length:
                    maxi = length
            else:
                l = l[(l.index(i) + 1)::]
                l.append(i)
                length = len(l)
        return maxi 
