#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:25:36 2018

@author: raine
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        
        # 反正同时拼接的只有两个链表,，分而治之
        def merge2lists(self, mergeKLists,list_i):
            p1 = mergeKLists[0]
            p2 = list_i
            while(p1.next and p2.next):
                if p1.next.val > p2.val:
                    tmp = p1.next
                    p1.next.val = p2.val
                    p1.next.next = tmp
                    
                    p1 = p1.next
                    p2 = p2.next
                # p1 和 p2 都走到了最后一个节点
                if not p1.next and not p2.next:
                    if p1.val > p2.val:
                        
                    p1.next = p2
                if not p2.next :
            
            return mergeKLists
        
        # 首先把 lists 的第一个 listnode 赋值给 mergeKLists
        mergeKLists = [lists[0]]
        k = len(lists[:]) #获取 排序链表数量
        for i in range(1,k):
            mergeKLists = merge2lists(mergeKLists,[lists[i]])
        print(mergeKLists)
                
                    
                

        