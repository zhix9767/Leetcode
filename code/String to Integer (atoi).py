class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        start = False
        Flag = 1
        for i in range(len(str)):        
            if str[i] == ' ' and not start :
                continue         
            elif str[i] == '+' and not start:
                start = True
            elif str[i] == '-' and not start:
                start = True
                Flag = -1
            elif str[i]>'9' or str[i]<'0':
                break
            else:
                start = True
                result = result * 10 + int(str[i])-int('0')
        result = result * Flag
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result
            