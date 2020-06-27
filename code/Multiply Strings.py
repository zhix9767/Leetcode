class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1)+len(num2))
        pos = 0
        for i in reversed(num1):
            tempPos = pos
            for j in reversed(num2):
                product[tempPos] += int(i) * int(j)
                product[tempPos+1] += (product[tempPos] // 10)
                product[tempPos] %= 10
                tempPos += 1
            pos += 1
        product.reverse()
        index = 0
        while index < len(num1) + len(num2) - 1 and product[index] == 0:
            index += 1
        return ''.join(map(str, product[index:]))
