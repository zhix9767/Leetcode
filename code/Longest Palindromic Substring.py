class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s)==0):
            return ""
        matrix = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            matrix[i][i] = 1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                matrix[i][i+1] = True
        for j in range(2,len(s)):
            for i in range (0, len(s)-j):
                if s[i] == s[i+j] and matrix[i+1][i+j-1]:
                    matrix[i][i+j] = True
                else:
                    matrix[i][i+j] = False
        for j in range(len(s),-1,-1):
            for i in range(0,len(s)-j):
                if matrix[i][i+j]:
                    return s[i:i+j+1]


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0:
            return ""
        count = 2 * length + 1 # the number of position
        LPS = [0] * count
        #init
        LPS[0] = 0
        LPS[1] = 1
        centerPosition = 1
        centerRightPosition = 2

        for currentRightPosition in range(2, count):
            currentLeftPosition = 2 * centerPosition - currentRightPosition
            LPS[currentRightPosition] = 0
 
            # condition 1
            if LPS[currentLeftPosition] < centerRightPosition - currentRightPosition:
                LPS[currentRightPosition] = LPS[currentLeftPosition]

            # condition 2
            elif LPS[currentLeftPosition] == centerRightPosition - currentRightPosition and \
                centerRightPosition == 2 * length:
                    LPS[currentRightPosition] = LPS[currentLeftPosition]

            # condition 3 and condition 4
            else:
                while LPS[currentRightPosition] + currentRightPosition < count - 1  and \
                    currentRightPosition - LPS[currentRightPosition] > 0 and \
                        (((LPS[currentRightPosition] + currentRightPosition + 1)%2 == 0) or \
                            (s[(LPS[currentRightPosition] + currentRightPosition +1)//2] \
                                == s[(currentRightPosition - LPS[currentRightPosition] -1)//2])):
                                LPS[currentRightPosition] += 1

            if currentRightPosition + LPS[currentRightPosition] > centerRightPosition:
                centerRightPosition = currentRightPosition + LPS[currentRightPosition]
                centerPosition = currentRightPosition

        maxPosition = -1
        maxLength = -1  
        for i in range(count):
            if LPS[i] > maxLength:
                maxLength = LPS[i]
                maxPosition = i
        start = (maxPosition - maxLength) // 2
        end =  start + maxLength
        return s[start : end]