#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        """
        思路-----------------------
        case 1：当模式中的第二个字符不是*时： 
        case 1.1. 如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，继续后移匹配。 
        case 1.2. 如果字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。
        
        case 2: 当模式中的第二个字符是*时： 
        case 2.1. 字符串第一个字和模式第一个字符匹配，
             case 2.1.1. 字符串的第二个字符和第一个字符相同，字符串后移一位；
             case 2.1.2. 字符串的第二个字符和第一个字符不相同，模式后移1字符；
        case 2.2. 字符串第一个字和模式第一个字符不匹配，模式后移2字符； 
        -----------------------end
        
        Created on Fri Nov 18 2018
        """
        # case 1：最简单的情况，p 和 s 相等
        if s == p:
            return True
        # case 2：第二位出现了*
        if len(p)>1 and p[1] == '*':
            # p[0]匹配 s[0]，当 s[0]==s[1]时，s=s[1:]否则p=p[2:]
            if s and (s[0]==p[0] or p[0] == '.'):# p[0] 匹配 s[0]，则
                return self.isMatch(s,p[2:]) or self.isMatch(s[1:],p)
            else:# 但是 p[0]不匹配 s[0]，直接跳过 p 的前两位
                return self.isMatch(s,p[2:])
        #  case3：p 的前两位没有出现 *,直接比较第一位
        elif s and p and (s[0] == p[0] or p[0]=='.'):
            return self.isMatch(s[1:],p[1:])
        # 递归退出条件：s 和 p 不相等
        return False