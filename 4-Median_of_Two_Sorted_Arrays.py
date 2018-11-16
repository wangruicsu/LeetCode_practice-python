#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        """
        note: 
        1. sorted arrays
        2. the median of the two sorted arrays → resort two arrays and find out median
        do：
        拼接两个有序数组为一个新的有序数组并输出中位数
        
        Created on Fri Nov 16 2018
        """
        
        """"""
        if len(nums1) == len(nums2) == 0:return
        if len(nums1) == 0: 
            return nums2[int(len(nums2)/2)] if len(nums2)%2 != 0 else (nums2[int(len(nums2)/2) -1]+nums2[int(len(nums2)/2)])/2.0
        if len(nums2) == 0: 
            return nums1[int(len(nums1)/2)] if len(nums1)%2 != 0 else (nums1[int(len(nums1)/2) -1]+nums1[int(len(nums1)/2)])/2.0

        index_median = int((len(nums1)+len(nums2))/2.0)# 不管为奇偶，找到index_median就足够找到中位数了
        nums3 = []
        i,j = 0,0

        short_array = nums1
        long_array = nums2

        if len(nums1) > len(nums2): 
            short_array = nums2
            long_array = nums1

        short = len(short_array)
        long = len(long_array)

        while(True):
            # 维持有序性：比较长短数组的对应元素大小，就添加谁的元素到 nums3中
            if short_array[i] > long_array[j]: 
                nums3.append(long_array[j])
                j += 1
                long -= 1
            else:
                nums3.append(short_array[i])
                i += 1
                short -= 1
                
            # 短数组使用完后，无需再比较长短数组的对应元素大小，将长数组直接拼接在 nums3后面。
            if long == 0 and short == 0:
                return nums3[index_median] if len(nums3)%2 != 0 else (nums3[index_median]+nums3[index_median-1])/2.0

            if short == 0:
                nums3 += long_array[j:]
                return nums3[index_median] if len(nums3)%2 != 0 else (nums3[index_median]+nums3[index_median-1])/2.0

            if long == 0:
                nums3 += short_array[i:]
                return nums3[index_median] if len(nums3)%2 != 0 else (nums3[index_median]+nums3[index_median-1])/2.0