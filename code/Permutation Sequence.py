class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        fac = self.factorial(n)
        result = ""
        k -= 1
        numbers = list(range(1,n+1))
        for i in range(n):
            index = k // fac[n-i-1]
            result += str(numbers[index])
            numbers.pop(index)
            k -= index * fac[n-i-1]
        return result

    def factorial(self, n):
        result = [1]
        temp = 1
        for i in range(1,n):
            temp *= i
            result.append(temp)
        return result