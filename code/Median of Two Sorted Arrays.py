class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        lindex = 0; rindex = len1; halflen = (len1+len2+1) // 2
        while (lindex <= rindex):
            loc1 = (lindex + rindex) // 2
            loc2 = halflen - loc1
            if (loc1 > 0 and nums1[loc1-1] > nums2[loc2]):
                rindex = loc1 - 1
            elif (loc1 < len1 and nums1[loc1] < nums2[loc2-1]):
                lindex = loc1 + 1
            else:
                if loc1 == 0:
                    left = nums2[loc2-1]
                elif loc2 == 0:
                    left = nums1[loc1-1]
                else:
                    left = max(nums1[loc1-1],nums2[loc2-1])
                if (len1+len2)%2==1:
                    return left
                else:
                    if loc1 == len1:
                        right = nums2[loc2]
                    elif loc2 == len2:
                        right = nums1[loc1]
                    else:
                        right = min(nums1[loc1],nums2[loc2])
                    return (left+right)/2




