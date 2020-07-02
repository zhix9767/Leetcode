class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pointer = len(nums1)-1
        m -= 1
        n -= 1
        while m >= 0 and n >=0:
            if nums1[m] > nums2[n]:
                m[pointer] = nums1[m]
                m -= 1
            else:
                m[pointer] = nums2[n]
                n -= 1
            pointer -= 1
        while n >= 0:
            m[pointer] = nums2[n]
            n -= 1
            pointer -= 1
        return
        