# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:49:04 2018

@author: bpou
"""

import random

grammar = """
sentence = adj noun verb adj noun2
adj = adj_single 和 adj_single 的 | null
adj_single = 漂亮  | 蓝色 | 好看
adv = 安静地 | 静静地
noun = 猫 | 女人 | 男人
verb = adv 看着 | adv 坐着 
noun2 = 桌子 | 皮球 
"""

def build_grammar(grammar_str, split='='):
    grammar_pattern = {}
    for line in grammar_str.split('\n'):
        if not line: continue
        statement, expr = line.split(split)
        grammar_pattern[statement.strip()] = [e.split() for e in expr.split('|')]
    return grammar_pattern

def generate(grammar_pattern, target):
    if target not in grammar_pattern: 
        return target
    
    expr = random.choice(grammar_pattern[target])
    
    tokens = [generate(grammar_pattern, e) for e in expr]#递归调用自己，直到表达式中不含有已声明内容
    
    return ''.join([t for t in tokens if t != 'null'])

grammar_pattern = build_grammar(grammar)
print(generate(grammar_pattern, 'sentence'))