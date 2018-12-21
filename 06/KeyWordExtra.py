# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:12:55 2018

@author: bpou
"""
import pandas as pd
import jieba
from collections import Counter
from tqdm import tqdm_notebook
import math
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

content = pd.read_csv('..\..\wiki\\sqlResult_1558435.csv', encoding='gb18030')
print (len(content))
print (content.head())
print (content.iloc[3])

print (content.iloc[0]['content'])
def cut(string): return list(jieba.cut(string))
content_of_xiaomi = cut(content.iloc[0]['content'])

print (Counter(content_of_xiaomi).most_common()[:10])

content = content.fillna('')
all_news_content = content['content']
all_occurences = []
for c in tqdm_notebook(all_news_content, total=len(all_news_content)):
    all_occurences.append(set(cut(c)))
    
def inverse_document_frequency(word):
    eps = 1e-6
    return math.log10(len(all_occurences) / (sum(1 for w in all_occurences if word in w) + eps))
print (inverse_document_frequency('我们'))
def tf(word, cut_words_counter):
    return cut_words_counter[word] / sum(cut_words_counter.values())
print (tf('小米', Counter(content_of_xiaomi)))

def tfidf(word, cut_words_counter):
    w_tf = tf(word, cut_words_counter)
    
    idf = inverse_document_frequency(word)
    
    return w_tf * idf
print (tfidf('小米', Counter(content_of_xiaomi)))
print (tfidf('的', Counter(content_of_xiaomi)))


def get_words_importance(cut_words):
    importance = {
        w: tfidf(w, Counter(cut_words)) for w in set(cut_words)
    }
    
    return sorted(importance.items(), key=lambda x: x[1], reverse=True)

test_news = content.iloc[2573]['content']
print (test_news)

cut_test_news = cut(test_news)
lunar_important = get_words_importance(cut_test_news)

xiaomi_important = get_words_importance(content_of_xiaomi)
word_cloud = wordcloud.WordCloud(font_path='C:\Windows\Fonts\SimHei.ttf')
word_cloud_with_mask = wordcloud.WordCloud(font_path='C:\Windows\Fonts\SimHei.ttf')
def plot_word_cloud_by_importance(importance):
    plt.imshow(word_cloud_with_mask.generate_from_frequencies({w: fre for w, fre in importance}))
word_cloud_with_mask.generate_from_frequencies({w: fre for w, fre in lunar_important}).to_file('mask_test.png')
