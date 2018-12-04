# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:25:47 2018

@author: bpou
"""
from collections import defaultdict
import time
import functools
prices = defaultdict(lambda : -float('inf'))
for i, v in enumerate([1, 5, 8, 9, 10, 17, 17, 20, 24, 30]):
    prices[i + 1] = v 
print (prices)
cache = {}
"""def revenue(r):
    if r in cache: return cache[r]
    op = max([prices[r]] + [(revenue(i) + revenue(r - i)) for i in range(1, r)] )
    cache[r] = op
    return op
 """
  
solution = {}
@functools.lru_cache(maxsize = 2*100) 
def revenue(r):
    #if r in solution: return solution[r]
    split, op = max([(0, prices[r])] + [(i, revenue(i) + revenue(r - i)) for i in range(1, r)], key=lambda x:x[1])
    solution[r] = (split, r - split)
    return op
start = time.time()
print (revenue(100))
print ('used time :{}'.format(time.time() - start))
print (solution)
def parse_solution(r, revenue_solution):
    assert r in revenue_solution
    left, right = revenue_solution[r]
    if 0 == left: return [right]
    else :
        return [left] + parse_solution(right, revenue_solution)
    
def pretty_solution(splits):
    return '->'.join(map(str, splits))

print (pretty_solution(parse_solution(90, solution)))
        
