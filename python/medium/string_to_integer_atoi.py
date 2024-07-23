# https://leetcode.com/problems/string-to-integer-atoi/
# ...i do not like this problem

class Solution:
    def myAtoi(self, s: str) -> int:
        # 1: whitespace
        s = s.strip()
        if len(s)==0:
            return 0
        
        # 2: signedness
        sign = -1 if s[0]=="-" else 1
        s = s[1:] if (s[0]=="-" or s[0]=="+") else s

        # 3: conversion
        while len(s)>0 and s[0]=="0":
            s = s[1:]
        for i in range(len(s)):
            try:
                if int(s[i]): continue
            except:
                s = s[:i]
                break
        if len(s)==0:
            return 0

        # 4: rounding
        bit, val = 2**31, int(s)*sign
        return max(-bit,val) if sign<0 else min(bit-1,val) 
