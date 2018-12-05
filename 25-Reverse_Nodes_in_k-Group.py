#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """
        思路：
        约束①：空链表
        约束②：链表长度不是 K 的整数倍时，余下的部分不进行逆转
        DO：
        创建新的逆转后的链表 newList
        在每个 长度为（k-1）的 for 循环中
            创建逆转的子链表 tmpList
                子链表长度不够 k 时，newList直接接上余下的部分
        newList 接上 tmpList
        
        @date：2018-12-03 
        @author：Raine
        
        """
        p1 = head # 依次指向第1，K+1，2K+1，，，个节点
        if not p1:return head  # 返回空链表

        p2 = head # 指向目前正在翻转的节点
        newList = ListNode(0) # 创建逆转后的链表
        p3 = newList
        # 链表长度小于 K 就不进行翻转
        while(p2 is not None):
            tmpList = ListNode(0) #新的子 逆序链表
            tmpList.val = p2.val
            #print(tmpList.val)
            p4 = tmpList # 指向子链表的第一个节点
            p5 = tmpList # 指向子链表的最后一个节点，用于 p3 的移动
            p1 = p2 # 标记 子链表 tmpList 开始翻转的位置
            for i in range(k-1): # 生成子链表
                p2 = p2.next
                if p2 is None:
                    p3.next = p1 #子链表长度不足 k，newList 直接从 p1 接上不进行翻转的部分。
                    return newList.next 
                newNode = ListNode(p2.val) # 创建新节点，并加入 tmpList
                newNode.next = tmpList
                tmpList = newNode # 更新 tmpList
                p4 = tmpList
            
            p3.next = p4 #每次完整得到一个逆序的 k 长度的链表时，才接入 newList
            p3 = p5 # p3 指向 newList 最后一个节点，也就是当前 tmpList的最后一个节点
            p2 = p2.next # p2 指向下一次开始翻转的节点
        return newList.next
            
            
            
            
            
            
            
            
            
            