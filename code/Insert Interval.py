class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        result = []
        last = newInterval
        for i in range(len(intervals)):
            if intervals[i][1] < last[0]:
                result.append(intervals[i])
            elif intervals[i][0] > last[1]:
                result.append(last)
                result += intervals[i:len(intervals)]
                return result
            else:
                last[0] = min(last[0],intervals[i][0])
                last[1] = max(last[1],intervals[i][1])
        result.append(last)
        return result
            
