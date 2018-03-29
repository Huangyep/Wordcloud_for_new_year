#coding = UTF-8
import jieba
import numpy
import codecs
import pandas
import matplotlib.pyplot as plt
from os import path 
from scipy.misc import imread
from wordcloud import WordCloud,ImageColorGenerator

#打开词库文件
file = codecs.open(u"2018.txt","r",encoding='UTF-8')
content = file.read()
file.close()

#用jieba库进行中文分词
segment = []
segs = jieba.cut(content)
for seg in segs:
	if len(seg)>1 and seg!='\r\n':
		segment.append(seg)

#进行分词词频统计
words_df = pandas.DataFrame({'segment':segment})
words_df.head()
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat = words_stat.reset_index()
print(words_stat)

#词云图显示出来
#cloud_mask = imread(r'C:\Users\hp\Desktop\gou.png')
d = path.dirname(__file__)
cloud_mask = imread(path.join(d, "gou.png"))
wordcloud = WordCloud(background_color='white',mask=cloud_mask,
	font_path="C:\simhei.ttf")
words = words_stat.set_index('segment').to_dict()
wordcloud.fit_words(words['计数'])
plt.imshow(wordcloud)
plt.axis('off') 
plt.show()