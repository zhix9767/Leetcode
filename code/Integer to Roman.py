class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        case1 = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        case2 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        case3 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        case4 = ["", "M", "MM", "MMM"]

        result = case4[num//1000]+case3[(num%1000)//100]+case2[(num%100)//10]+case1[num%10]
        return result

test = Solution()
num = 89
print(test.intToRoman(num))