from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        window = {}
        get = 0
        left = 0
        right = 0
        result = (float("inf"), 0 , 0)
        while right < len(s):
            character = s[right]
            window[character] = window.get(character,0) + 1
            if character in dict_t and window[character] == dict_t[character]:
                get += 1
            while left <= right and get == required:
                character = s[left]
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                window[character] -= 1
                if character in dict_t and window[character] < dict_t[character]:
                    get -= 1
                left += 1
            right += 1
        return "" if result[0] == float("inf") else s[result[1]:result[2]+1]
                