class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        add = 0
        result = ""
        for i in range(max(len(a),len(b))):
            temp = (int(a[i]) if i < len(a) else 0) + (int(b[i]) if i < len(b) else 0) + add
            add = temp // 2
            result += str(temp % 2)
        if add:
            result += "1"
        return result[::-1]
        