class Solution(object):
    def longestPalindrome(self, s):
        slength = len(s)
        begin = 0
        length = 0
        table = []
        for i in range(slength):
            tem = []
            for j in range(slength):
                tem.append(0)
            table.append(tem)
            
        for i in range(slength):
            table[i][i] = 1
            
        for i in range(slength - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = 1
                begin = i
                length = 1
                
        for tem in range(1, slength):
            for i in range(slength - tem):
                j = i + tem
                if (s[i] == s[j]) and table[i + 1][j - 1] == 1:
                    table[i][j] = 1
                    length = tem
                    begin = i
        return s[begin : begin + length + 1]
