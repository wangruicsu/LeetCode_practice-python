#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        """
        思路：
        约束①：子串要与 words 中的单词完全匹配，中间不能有其他字符
        约束②：不需要考虑 words 中单词串联的顺序
        约束③：子串不止一个
        约束④：一些长度相同的单词 words
        
        DO：
        每次从 s 的第 i 个元素开始取一个与 words元素个数一样列表 pattern，比较pattern和 words 是否相同（比较list 相同前要先排序）。
        Fail：超出时间限制（怀疑是排序那里）
        
        改进：i 的遍历范围由range(len(s)) 换为range(len(s) - k*len(words) +1)
        通过（1384 ms）
        
        @date：2018-12-05 
        @author：Raine
        """
        if not s or not words: return [] #空字符串返回
        k = len(words[0])
        if len(s) < k*len(words): return [] #字符串长度小于 words 中的字母数量返回
        
        index = []
        words.sort()
        
        for i in range(len(s) - k*len(words) +1):
            pattern = [] # s 中可能与 words 匹配的子串
            for j in range(len(words)):
                pattern.append(s[i+j*k:i+j*k+k])
            pattern.sort()
            if pattern == words: 
                index.append(i)
        return index
        