from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0 or len(words[0]) == 0:
            return []
        result = []
        words_size = len(words[0])
        words_count = len(words)
        map = Counter(words)
        for i in range(len(s)-words_count * words_size + 1):
            word_dict = dict(map)
            count = 0
            for j in range(words_count):
                substring = s[i + j*words_size : i + (j+1) * words_size]
                if substring in word_dict and word_dict[substring] > 0:
                    count += 1
                    word_dict[substring] -= 1
                else: break
            if count == words_count:
                result.append(i)
        return result
