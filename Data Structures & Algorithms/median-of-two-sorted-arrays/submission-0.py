class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1)+len(nums2)
        half = totalLength//2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left = -1
        right = len(nums1)-1
        while left <= right:
            mid1 = (left+right)//2
            mid2 = half - mid1 -2
            nums1Left = nums1[mid1] if mid1 >= 0 else float("-infinity")
            nums1Right = nums1[mid1+1] if (mid1+1) < len(nums1) else float("infinity")
            nums2Left = nums2[mid2] if mid2 >= 0 else float("-infinity")
            nums2Right = nums2[mid2+1] if (mid2+1) < len(nums2) else float("infinity")
            if nums1Left <= nums2Right and nums1Right >= nums2Left:
                if totalLength % 2:
                    return min(nums1Right, nums2Right)

                return (max(nums1Left, nums2Left)+min(nums1Right, nums2Right))/2
            elif nums1Left > nums2Right:
                right = mid1 -1
            else:
                left = mid1+1
