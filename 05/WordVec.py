# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:28:57 2018

@author: bpou
"""

import jieba
import os
import time
import gensim
from gensim.models import Word2Vec 
from gensim.models.word2vec import LineSentence
target_files = ['..\..\wiki\zh_wiki_00']

all_words = open(target_files[0], encoding='utf-8').read()
def WriteTokenToFile(open_file, output_file):
    for line in open(open_file, encoding='utf-8'):
        words = list(jieba.cut(line))
        output_file.write(' '.join(words))
        
with open('..\..\wiki\\train_corpus.txt', 'w', encoding='utf-8') as output_f:
    for f in target_files:
        WriteTokenToFile(f, output_f)
start = time.time()
mini_model = Word2Vec(LineSentence('..\..\wiki\\train_corpus.txt'), min_count = 1)
#mini_model = gensim.models.Word2Vec.load('web_words.model')
end = time.time()
print ('used time :{}'.format(time.time() - start))
print (mini_model.most_similar('数学'))

outp1 = '..\..\wiki\web_words.model'
mini_model.save(outp1)

model = gensim.models.Word2Vec.load('..\..\wiki\web_words.model')
print (model.most_similar('数学'))

#todo 可视化