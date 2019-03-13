# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:30:25 2019

@author: ASUS
"""

import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

currdir = os.path.dirname(os.path.abspath( __file__ ))

def get_wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

def create_wordcloud(text):
    mask = np.array(Image.open(os.path.join(currdir,"cloud.png")))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",
                    mask=mask,
                    max_words=200,
                    stopwords=stopwords)
    wc.generate(text)
    wc.to_file(os.path.join(currdir,"wc.png"))
    
    
create_wordcloud(get_wiki("python programming language"))

cloud = WordCloud(background_color = 'white').generate(get_wiki("python programming language"))
plt.imshow(cloud)
plt.axis('off')
plt.show()

text = "刘若怡 大脑袋 大白痴 大白兔 大傻子 大个子 大眼睛 小儿子 小孙子"
cloud = WordCloud(background_color = 'white').generate(text)
plt.imshow(cloud)
plt.axis('off')
plt.show()