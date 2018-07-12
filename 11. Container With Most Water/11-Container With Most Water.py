class Solution(object):
    def maxArea(self, height):
        '''
        maxi = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                maxi = maxi if maxi > (j - i) * (min(height[i], height[j])) else (j - i) * (min(height[i], height[j]))
        return maxi
        本来想两个for loop5行搞定的， 结果时间复杂度过不去， 老是time out
        '''
        
        l = 0
        r = len(height)-1
        if not height or len(height) == 1 :
            return 0
        res = (r-l)*(height[l] if height[l] < height[r] else height[r])
        
        while l < r:
            if height[l] < height[r] :
                res = res if res > height[l]*(r-l) else height[l]*(r-l)
                l += 1
            else :
                res = res if res > height[r]*(r-l) else height[r]*(r-l) 
                r -=1
        return res
