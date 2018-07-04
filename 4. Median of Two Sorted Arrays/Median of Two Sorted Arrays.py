class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        print(nums3)
        if len(nums3) % 2 == 0:
            return (nums3[len(nums3) / 2 - 1] + nums3[len(nums3) / 2]) / 2.0
        else:
            return float(nums3[int(math.ceil(len(nums3) / 2))])
