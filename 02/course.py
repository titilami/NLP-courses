# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:37:13 2018

@author: bpou
"""
import os
import re
import requests

import time
from collections import Counter

import random
from functools import reduce
from operator import mul, add
test = requests.get('https://movie.douban.com/').text
#print(test)
#print(ord('我'))
#print(chr(25105))

filename = 'zh_wiki_00'
pwd = os.getcwd()
print(pwd)
all_content = open(filename ,encoding='utf-8', errors='ignore').read()
#print ((all_content))


def tokenize(string): 
    return ''.join(re.findall('[\w|\d]+', string))


#print(all_content[:200])
ALL_CHARACTER = tokenize(all_content)

all_character_counts = Counter(ALL_CHARACTER)


#print(all_character_counts.most_common()[:100])
def get_probability_from_counts(count):
    all_occurences = sum(count.values())
    def get_prob(item): 
        return count[item] / all_occurences
    return get_prob

get_char_prob = get_probability_from_counts(all_character_counts)

def get_char_probability(char): 
    all_occurences = sum(all_character_counts.values())
    return all_character_counts[char] / all_occurences

def get_running_time(func, arg, times):
    start_time = time.time()
    for _ in range(times):
        func(arg)
    print('\t\t {} used time is {}'.format(func.__name__, time.time() - start_time))

random_chars = random.sample(ALL_CHARACTER, 1000)
#print(random_chars)

get_running_time(get_char_probability, '神', 10000)


print (reduce(add, range(1, 101)))

def prob_of_string(string):
    return reduce(mul, [get_char_prob(c) for c in string])


print (prob_of_string('这只是数学'))

gram_length = 1
one_gram_counts = Counter(ALL_CHARACTER[i:i+gram_length] for i in range(len(ALL_CHARACTER) - gram_length))
gram_length = 2
two_gram_counts = Counter(ALL_CHARACTER[i:i+gram_length] for i in range(len(ALL_CHARACTER) - gram_length))
print (one_gram_counts.most_common()[:20])
print ("2-gram_counts")
print (two_gram_counts.most_common()[:20])
get_pair_prob = get_probability_from_counts(two_gram_counts)


def get_2_gram_prob(word, prev):
    if get_pair_prob(word+prev) > 0: 
        return get_pair_prob(word+prev) / get_char_prob(prev)
    else:
        return get_char_prob(word)
    
def get_2_gram_string_prob(string):
    probablities = []
    for i, c in enumerate(string):
        prev = '<s>' if i == 0 else string[i-1]
        probablities.append(get_2_gram_prob(c, prev))
    return reduce(mul, probablities)
pair = """前天晚上吃晚饭的时候
前天晚上吃早饭的时候""".split('\n')

pair2 = """正是一个好看的小猫
真是一个好看的小猫""".split('\n')

pair3 = """我无言以对，简直
我简直无言以对""".split('\n')
pairs = [pair, pair2, pair3]

def get_probability_prefromance(language_model_func, pairs):
    for (p1, p2) in pairs:
        print('*'*18)
        print('\t\t {} with probability {}'.format(p1, language_model_func(tokenize(p1))))
        print('\t\t {} with probability {}'.format(p2, language_model_func(tokenize(p2))))
get_probability_prefromance(prob_of_string, pairs)
print ("get_2_gram_string_prob")
get_probability_prefromance(get_2_gram_string_prob, pairs)