class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs: 
            return[]
        dicts = {}
        for i in strs:
            sort_i = str(sorted(list(i)))
            temp = dicts.get(sort_i,[])
            temp.append(i)
            dicts.update({sort_i:temp})
        result = []
        for key,value in dicts.items():
            result.append(value)
        return result