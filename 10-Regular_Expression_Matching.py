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
        note-----------------------
        当第二位出现了*时
        如果第一位不匹配就跳过至p 的*的下一位（ p 中不和 s 匹配的字符如果后面紧接着*，则认为该字符没有出现过）
        如果第一位匹配，就看 s 的前两位是否重复，重复则 s 继续往后走，p 不移动；不重复则跳至 p 的*下一位，s 不移动

        do-------------------------
        递归
        
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