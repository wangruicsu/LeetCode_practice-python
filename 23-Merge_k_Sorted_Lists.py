#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 23:08:40 2018

@author: raine
"""

class Solution:
    # 反正同时拼接的只有两个链表,，分而治之
    def merge2lists(self, p1,p2):
        if not p1: return p2
        if not p2: return p1
        new = ListNode(0)#指向合并后的有序链表表头
        p3 = new

        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        if p1: p3.next = p1
        if p2: p3.next = p2
        return new.next
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:return lists
        if len(lists) == 1:return lists[0]

        # 首先把 lists 的第一个 listnode 赋值给 mergeKLists
        k = len(lists[:]) #获取 排序链表数量
        for i in range(1,k):
            if not lists[i]:
                continue
            # 每次都把第 i 个链表接到 lists[0]后面
            lists[0] = self.merge2lists(lists[0],lists[i])  
        return lists[0]