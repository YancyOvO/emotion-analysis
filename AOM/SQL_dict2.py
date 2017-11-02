import itertools  
import re

def build_dictionary():
     Features ={}
     for items in open('data/dic/Emo.txt','r',encoding='utf-8'):
         global num
         num = 0
         b = list(items.split())
         
         b = "".join(itertools.chain(b))
         num_list = re.findall('[\-]+[\d]+\.+[\d]+|[\d]+\.+[\d]+', b)#提取数字
         for item in num_list:
             num = float(item)
             num = round(num, 2)
         #for word in b:
             #if word =='[0-9]':
                 #w =  re.escape(word)  
         #print(b)
         b = re.sub('[\d]+\.+[\d]+', '', b)
         Features[b] = num
#     print(Features)

     return Features#返回文中句子

import codecs

def write_f(str):#写入sql文档

     file_object = codecs.open('data/sql/dictionary2.sql', 'w', 'utf-8')
     
     file_object.write(str)
     
     file_object.close()
     
     print('success')

def toSQL():
     str = ""
     dic = build_dictionary()

     dic.pop('')#删除空字符
     for dat, emo in dic.items():
         str = str + "insert into base_dict2(word,emotion) values "+"('%s','%s');\r\n"%(dat, emo)
     print(str)
     write_f(str)

toSQL()
