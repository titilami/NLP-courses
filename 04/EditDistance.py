# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 21:05:35 2018

@author: bpou
"""
from memo import memo

@memo
def GetEditDistance(string1, string2):
    if len(string1) == 0: return len(string2)
    if len(string2) == 0: return len(string1)
    return min(
            [GetEditDistance(string1[:-1], string2) + 1,
            GetEditDistance(string1, string2[:-1]) + 1,
            GetEditDistance(string1[:-1], string2[:-1]) + (0 if string1[-1] == string2[-1] else 2)]
            )
    
print(GetEditDistance('uuuubin iwf test', 'xxxbd efwf efw taste'))