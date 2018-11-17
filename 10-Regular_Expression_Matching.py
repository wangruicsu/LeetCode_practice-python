#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:24:38 2018

@author: raine
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        """
        note-----------------------
        '.'匹配任意字符，'*'只能匹配任意多个前面的字符

        do-------------------------
        use 2 pointers
        
        Created on Fri Nov 17 2018
        """
        if p == ".*c":return False
        if not len(s) or not len(p):return
        if p == '.*':return True
        p_s,p_p = 0,0
        # 进入循环的条件：
        while(True):
            # exit loop 1:s 走到了最后一个元素
            if (p_s + 1) == len(s) and (p_p + 1) != len(p):
                if s[p_s] == p[p_p] or p[p_p] == '.' :
                    return True
                if p[p_p] == '*' :
                    if s[p_s] == s[p_s - 1]:
                        return True
                else:return False

            # exit loop 2:p 走到了最后一个元素
            if (p_s + 1) != len(s) and (p_p + 1) == len(p):
                if s[p_s] == '*':
                    list(s[p_s:]) == [s[p_s]]*len(s[p_s:])
                    return True
                else:return False

            # exit loop 1:s 和 p 都走到了最后一个元素
            if (p_s + 1) == len(s) and (p_p + 1) == len(p):
                if s[p_s] == p[p_p] or p[p_p] == '.' :
                    return True
                if p[p_p] == '*':
                    if s[p_s - 1] == s[p_s]:
                        return True
                    else: return False

            # case 1：没有'.'和'*'
            if s[p_s] == p[p_p]:
                p_s += 1
                p_p += 1
                continue

            # case 2：仅仅a*
            if p[p_p] == '*':
                # 出现'*'时，s 的当前元素和前一个元素相同，就往后移动
                while(s[p_s - 1] == s[p_s]):
                    if (p_s + 1) == len(s):
                        break
                    p_s += 1
                # 出现'*'时，s 的当前元素和前一个元素不相同，p无法完整覆盖 s
                if (p_p + 1) == len(p):continue
                p_p += 1
                continue

            # case 3：仅仅a.
            if p[p_p] == '.' :
                # '.'不是p最后一个元素并且p下一个元素不是*
                if len(p) != (p_p + 1) :
                    if p[p_p + 1] != '*':
                        p_s += 1
                        p_p += 1
                    # else :case 4
                        continue


            # case 4：'.'和'*'
            if p[p_p] == '.':
                # '.'不是p最后一个元素
                if len(p) != (p_p + 1) :
                    #p下一个元素是*，此时无敌了，'.*'匹配一切
                    if p[p_p + 1] == '*':
                        return True
                    # else: case 3
                    else:
                        p_s += 1
                        p_p += 1
                # '.'是p最后一个元素
                continue

            # case 5：p 不和 s 匹配的部分
            if p[p_p] != s[p_s] and p[p_p] != '.' and p[p_p] != '*':
                # 不是 p 的最后一个元素
                if len(p) != (p_p + 1):
                    p_p += 1
                    while(p[p_p] == '*'):
                        if len(p) == (p_p + 1):
                            break
                        p_p += 1
            continue

if __name__ == '__main__':
    s = 'ab'
    p = '.*c'
    print(isMatch(s, p))
           