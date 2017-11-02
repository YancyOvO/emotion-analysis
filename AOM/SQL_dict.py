import itertools  
import re

def build_dictionary():#获取词语极性，创建集成词典。因dict特性，key值不能重复，则新词典中不会有重复词语
     posFeatures = {}
     negFeatures = {}
     for items in open('data/dic/Pemo.txt','r',encoding='utf-8'):      
         b = list(items.split())
         b = "".join(itertools.chain(b))
#         b = reduce(lambda x,y:x+y, b)#将b中所有数据按照加法的方式全部加起来
         posFeatures[b]='pos'#给items打上标签True转换成dict，{'公司'：True}
     for items in open('data/dic/Peva.txt','r',encoding='utf-8'):
         b = list(items.split())
         b = "".join(itertools.chain(b))
         posFeatures[b]='pos'
     for items in open('data/dic/Pos.txt','r',encoding='utf-8'):
         b = list(items.split())
         b = "".join(itertools.chain(b))
         posFeatures[b]='pos'
     for items in open('data/dic/pos_net.txt','r',encoding='utf-8'):       
         b = list(items.split())
         b = "".join(itertools.chain(b))
         posFeatures[b]='pos'
     for items in open('data/dic/Nemo.txt','r',encoding='utf-8'):
         b = list(items.split())
         b = "".join(itertools.chain(b))
         negFeatures[b]='neg'
     for items in open('data/dic/Neva.txt','r',encoding='utf-8'):
         b = list(items.split())
         b = "".join(itertools.chain(b))
         negFeatures[b]='neg'
     for items in open('data/dic/Neg.txt','r',encoding='utf-8'):
         b = list(items.split())
         b = "".join(itertools.chain(b))
         negFeatures[b]='neg'
     for items in open('data/dic/Neg_net.txt','r',encoding='utf-8'):
         b = list(items.split())
         b = "".join(itertools.chain(b))
         negFeatures[b]='neg'
     for items in open('data/dic/Emo.txt','r',encoding='utf-8'):
         global num
         num = 0
         b = list(items.split())
         b = "".join(itertools.chain(b))
         num_list = re.findall('[\-][\d]+\.+[\d]|[\d]+\.+[\d]', b)#提取数字
         for item in num_list:
             num = float(item)
         if num<=1.2 and num>=-0.8:#设置取词阈值
             continue
         b = re.sub('[\d]+\.+[\d]+', '', b)
         if '-' not in b:
             posFeatures[b]='pos'
         else:
             b = re.sub('\-', '', b)
             negFeatures[b] = 'neg'
     return posFeatures, negFeatures#返回文中句子

import codecs

def write_f(str):#写入sql文档
     file_object = codecs.open('data/sql/dictionary.sql', 'w', 'utf-8')
     file_object.write(str)
     file_object.close()
     print('success')

def toSQL():
     str = ""
     pos, neg = build_dictionary()
     dic=dict(pos)
     dic.update(neg)
     dic.pop('')#删除空字符
     for dat, emo in dic.items():
         str = str + "insert into base_dict(word,emotion) values "+"('%s','%s');\r\n"%(dat, emo)
     write_f(str)

toSQL()
