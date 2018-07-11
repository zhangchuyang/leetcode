class Solution(object):
    def reverse(self, x):
        if len(str(x)) == 1:    return x
        while x % 10 == 0:
            x = x / 10
        if x < 0:
            x = -x
            x = int(str(x)[::-1])
            if -x < -2 ** 31:       return 0
            return -x
        else:
            x = int(str(x)[::-1])
            return 0 if x > 2 ** 31 -1 else x
