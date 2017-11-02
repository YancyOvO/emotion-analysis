import re
import jieba
import SQL_Conn

from xml.dom import minidom  
#import sys
#sys.path.append('E:/biancheng/Python/AOM')
import plt
import issue as ue
def import_data(filename, a):
     
     dom = minidom.parse(filename)
     
     if a == 0:
     
         data = dom.getElementsByTagName('article')
         
     else:
         
         data = dom.getElementsByTagName('emotion')
        
     return data


def jieba_cut(data):
     global user
     global f
     global prt
     dat_last = False
     user = 0
     #dat = import_data('E:/biancheng/Python/AOM/data/test.xml', 0)
     #stop = [line.strip() for line in  open('E:/biancheng/Python/AOM/data/Stop.txt','r',encoding='utf-8').readlines()]#停用词
     dat = []
     dat_len = 0
     dat_i = 0
     for line in data:
         dat.append(line)
         dat_len += 1

    # print(stop)
     string = []

     for line in dat:
         if prt == True:
             dat_i+=1
             print(dat_i, dat_len)
             if dat_len == dat_i :
                 dat_last = True
                 f.write("您输入的句子是："+line+"\n")
         
        # if line.firstChild == None:
         if not line :
             
             continue

         else:
             
            # l_dat = line.firstChild.data
             l_dat = line
             
             if '@' in l_dat:
                 st = False
                 b = False
                 l_dat = re.sub('\/', '', l_dat)
                 if l_dat[0] == '@':
                     st = True
                 for word in l_dat:
                     #print(l_dat)                     
                     if word == '@' :
                         if dat_last == True:
                             f.write("去除@用户：")
                         b = True
                         user +=1
                     if st == True:
                         if word ==' ' or word ==':':
                             if dat_last == True:
                                 f.write("\n")
                             b = False
                     else:
                         if word =='\n':
                             if dat_last == True:
                                 f.write("\n")
                             b = False                    
                         
                     if b == True:
                         if dat_last == True:
                             f.write(word)
                         w =  re.escape(word)  
                         
                         l_dat = re.sub(w, '', l_dat)

             
             l_dat = re.sub('[a-zA-Z0-9\n\/\:\.\"\“\”]', '', l_dat)
             if dat_last == True:
                 f.write("去除无用符号及英文和数字\n")             
             #l_dat = re.sub('(\n)', '', l_dat)
             s = l_dat.split('\t')#切分成多条句子,规整格式
             fenci = jieba.cut(s[0],cut_all=False)#False默认值：精准模式，试图将句子最精确地切开，适合文本分析
             fenci = list(fenci)
             if dat_last == True:
                 f.write("切分句子为："+str(fenci)+"\n") 
             #print(type(fenci))
             string.append(fenci)
     

     return string

import itertools

def load_degree(test):#读取程度词
     degree = [] 
     for items in open(test,'r',encoding='utf-8'):
         b = list(items.split())
         #print(type(b))
         b = "".join(itertools.chain(b))
         degree.append(b)
     return degree


# 程度副词词典
mostdict = load_degree('data/degree/most.txt')   # 权值为2
verydict = load_degree('data/degree/very.txt')   # 权值为1.75
overdict = load_degree('data/degree/over.txt')  # 权值为1.6
moredict = load_degree('data/degree/more.txt')   # 权值为1.5
ishdict = load_degree('data/degree/ish.txt')   # 权值为1.2
insufficientdict = load_degree('data/degree/insufficiently.txt')  # 权值为0.5
oppositedict = load_degree('data/degree/opposite.txt')  # 权值为-0.5
global wt
wt = False
global prt
prt = False

def match(word, sentiment_value):
     global wt
     global f
     if word in mostdict:
         sentiment_value *= 2.0
         if wt == True:
             f.write("发现一级程度词“"+word+"”，等待情感词出现...\n")
         print('一级程度词：', word)
     elif word in verydict:
         sentiment_value *= 1.75
         if wt == True:
             f.write("发现二级程度词“"+word+"”，等待情感词出现...\n")
         print('二级程度词：', word)
     elif word in overdict:
         sentiment_value *= 1.6
         if wt == True:
             f.write("发现三级程度词“"+word+"”，等待情感词出现...\n")
         print('三级程度词：', word)
     elif word in moredict:
         sentiment_value *= 1.5
         if wt == True:
             f.write("发现四级程度词“"+word+"”，等待情感词出现...\n")
         print('四级程度词：', word)
     elif word in ishdict:
         sentiment_value *= 1.2
         if wt == True:
             f.write("发现五级程度词“"+word+"”，等待情感词出现...\n")
         print('五级程度词：', word)
     elif word in insufficientdict:
         sentiment_value *= 0.5
         if wt == True:
             f.write("发现六级程度词“"+word+"”，等待情感词出现...\n")
         print('六级程度词：', word)
     elif word in oppositedict:
         sentiment_value *= -0.5
         if wt == True:
             f.write("发现转义词“"+word+"”，等待情感词出现...\n")
         print('转义词：', word)
     #print (word, sentiment_value )
     return sentiment_value

def finding(filename):
     global wt
     global f
     f = open("outcome/record.txt", 'w', encoding = 'utf-8')
     outcome = []
     imp_word = []
     dat_ok = jieba_cut(filename)
     cs = SQL_Conn.cs()
     a = 0
     result = 0
     total = 0
     dat_len = len(dat_ok)
     dat_i = 0
     d=open("data/issue/test.txt", "w", encoding = 'UTF-8')
     d.truncate()#清空文件内容
     for items in dat_ok:
         dat_i+=1
         if len(items) == 0:
             result = 0
             outcome.append(result)
             continue
         if dat_i == dat_len:
             wt = True
         a+=1
         i = 0#扫描到词的个数
         s =0#扫描到程度词的位置
         poscount = 0#得分
         negcount = 0
         
         label = ue.judge_issue_line(items)#反问句识别
         if label[1] == -1 :
             total = label[2]
             d=open("data/issue/test.txt", "a", encoding = 'UTF-8')
             c = "".join(itertools.chain(label[0]))
             d.write(c+str(label[2])+'\n')
             d.close()
             if wt == True:
                 if label[2] >0:
                     f.write("这是一句带有积极情感的反问句\n")
                 if label[2] <0:
                     f.write("这是一句带有消极情感的反问句\n")
             #print(label,a)
             
         else:     
             for item in label[0]:
                 if item == ',' or item == '，' or item == '。' or item == '！'or item == ']':
                     #感叹句识别
                     if item == '！'or item == '!': 
                         if result > 0:
                             result += 2
                             if wt == True:
                                 f.write("发现感叹号,当前积极值为："+str(poscount)+"\n")
                         elif result < 0:
                             result -= 2
                             if wt == True:
                                 f.write("发现感叹号,当前消极值为："+str(negcount)+"\n")
                                 
                     total = total + result
                     result = 0
                     poscount = 0
                     negcount = 0
                     i += 1
                     print("当前情感值为%.2f"%total)
                     if wt == True:
                         f.write("上一句子计算完毕,目前情感值为："+str(total)+"\n")
                 else:
                     row_count = cs.execute("select word,emotion from base_dict where word = %s", (item))
                     imp_word.append(item)
                     if row_count:
                         row = cs.fetchone()#获取到数据库对应词和词性
                         #print(row_count, row[2])
                         if row[1] == 'pos':
                             poscount += 1
                             
                             #多种辅助判断方法
                             for w in items[s:i]:#查找附近是否有程度词及反义词
                                 poscount = match(w, poscount)
                             if wt == True and row[0] != '我':
                                 f.write("发现积极词“"+row[0]+"”,当前积极值为："+str(poscount)+"\n")        
                             if row[0] == '我'and wt == True:
                                 poscount -= 1
                             if row[0] == '微笑' or row[0]=='拜拜':
                                 for w in items[i-1:i]:
                                     if w == '[':
                                         poscount-=2
                                         if wt == True:
                                             f.write("该词为反义表情["+row[0]+"]，积极值减2，当前积极值为："+str(poscount)+"\n")
                             s=i
    
                             print('出现积极词"%s"积极值%s：'%(row[0], poscount))
                         elif row[1] == 'neg':
                             negcount += 1
                             
                             #程度副词检测
                             for w in items[s:i]:
                                 negcount = match(w, negcount)
                             s=i
                             
                             if wt == True:
                                 f.write("发现消极词“"+row[0]+"”,当前消极值为："+str(negcount)+"\n")
                             print('出现消极词"%s"消极值%s：'%(row[0], negcount))
                         #print(row[0], row[1])
                         #print(negcount)
                     i += 1
                     
                     #print(row[0], row[1])
                     result = poscount - negcount
             total = total + result
         print(label[0], total)
         outcome.append(total)
         if wt == True and total > 0:
             f.write("检测完毕，表达情感为积极，情感值为："+str(total)+"\n")
         if wt == True and total < 0:
             f.write("检测完毕，表达情感为消极，情感值为："+str(total)+"\n")
         if wt == True and total == 0:
             f.write("检测完毕，情感值为0\n")
         total = 0
         result = 0


     SQL_Conn.close()
     f.close()
     return imp_word, outcome

def finding2(filename):
     outcome = []
     imp_word = []
     dat_ok = jieba_cut(filename)
     cs = SQL_Conn.cs()
     for items in dat_ok:
         a = 0.0
         for item in items:
             row_count = cs.execute("select word,emotion from base_dict2 where word = %s", (item))
             imp_word.append(item)
             if row_count:
                 row = cs.fetchone()
                 #print(row_count, row[2])
                 a += row[1]
                 if row[1]<0:
                     print(row[1])
                 #print(row[0], row[1])
         #print(items, a)
         outcome.append(a-1)
     SQL_Conn.close()
     
     print(outcome)
     return imp_word, outcome

def Pos(txt):
#     dic_pos, dic_neg = build_dictionary()
     filename = open(txt,'r',encoding='utf-8')
     imp_word, outcome = finding(filename)
     filename.close()

     c = Counter(imp_word).most_common(100)
     #savePath.write('统计频率最高词语...\n')
     print(c)
     
     return outcome
     
def Neg(txt):
#     dic_pos, dic_neg = build_dictionary()
     filename = open(txt,'r',encoding='utf-8')
     imp_word, outcome = finding(filename)
     filename.close()

     c = Counter(imp_word).most_common(100)
     #savePath.write('统计频率最高词语...\n')
     print(c)
     
     return outcome


def audio(sentence):
     global prt
     prt = True
     imp_word, outcome = finding(sentence)
     plt.DrawPlt(outcome)
     prt = False
     global wt
     wt = False
     return outcome

def outcome_treat():
    
     train = Pos('data/weibo_data/pos_weibo.txt')
     user_ok = user
     train2 = Neg('data/weibo_data/neg_weibo.txt')
     user_ok+=user
     
     outcome = train+train2
     plt.DrawPlt(outcome)
     #print(train)
     #data, tag = zip(*train)
     s = len(train)
     s2 = len(train2)
     
     for i in range(0, s):
         
         if train[i]>0:
             
             train[i] = '1'
             
         elif train[i]==0:
             
             train[i] = '0'
             
         else:
             
             train[i] = '-1'

     for j in range(0, s2):
         
         if train2[j]>0:
             
             train2[j] = '1'
             
         elif train2[j]==0:
             
             train2[j] = '0'
             
         else:
             
             train2[j] = '-1'

     return train, train2, user_ok
     
 
from nltk.probability import  FreqDist

from collections import Counter
#from gensim import corpora
#import gensim
 
def new_dictionary():

     words = jieba_cut()
    
     dic = []
     
     for items in words:
         
         dic.append(items)
        
     word_fd = FreqDist()
     
     for word in dic:
         
         word_fd[word]+=1
#     dic_2 = corpora.Dictionary(words)
#     corpus = [dic_2.doc2bow(doc)for doc in words]
#     Lda = gensim.models.ldamodel.LdaModel
#     ldamodel = Lda(corpus, num_topics = 3, id2word = dic_2, passes = 50)
#     print(ldamodel.print_topics(num_topics = 3, num_words = 3))
     c = Counter(dic).most_common(100)
     
     print(c)
     
     return c



def conclusion():
    
     #test_data = import_data('E:/biancheng/Python/AOM/data/test.xml', 1)
     test_data = open('data/weibo_data/pos_weibo.txt','r',encoding='utf-8')
     test_data2 = open('data/weibo_data/neg_weibo.txt','r',encoding='utf-8')
     test_tag = []
     test_tag2 = []
     
     for line in test_data:
         #test_tag.append(line.firstChild.data)
         test_tag.append(line)
    
     pos_len= len(test_tag)
     
     for line2 in test_data2:
         test_tag2.append(line2)   
     
     neg_len= len(test_tag2)
    
     train_tag, train_tag2, user_ok = outcome_treat()
     
     #print(test_tag, train_tag)
     
     n = 0
     
     n2 = 0
     
     for i in range(0, pos_len):
         
         #if test_tag[i] == train_tag[i]:
         if train_tag[i]=='1':
             
             n += 1

     for j in range(0, neg_len):
         
         if train_tag2[j]=='-1':
             
             n2 += 1   
     
     pos_precision = n/(n+neg_len-n2)
     neg_precision = n2/(n2+pos_len-n)
     pos_recall = n/pos_len
     neg_recall = n2/neg_len
     F_pos = 2*pos_precision*pos_recall/(pos_precision+pos_recall )
     F_neg = 2*neg_precision*neg_recall/(neg_precision+neg_recall )
     
     print('正面情感准确率', pos_precision)
     print('负面情感准确率', neg_precision)
     print('正面情感召回率', pos_recall)
     print('负面情感召回率', neg_recall)
     print('正面F-Measure值', F_pos)
     print('负面F-Measure值', F_neg)
     savePath=open('E:/biancheng/Python/AOM/outcome/dict.txt', 'w', encoding = 'utf-8')
     savePath.write('预处理句子：\n')
     savePath.write('     跳过空句...\n')
     savePath.write('     去掉@用户... 共处理'+str(user_ok)+'处\n')
     savePath.write('     去掉英文及数字...\n')
     savePath.write('     进行分词...\n')
     savePath.write('载入程度词...\n')
     savePath.write('程度词赋权值...\n')
     savePath.write('连接词典数据库...\n')
     savePath.write('句子情感分析：\n')
     savePath.write('      反问句及情感判定...\n')
     savePath.write('      对照词典为词语标注词性值...\n')
     savePath.write('      对照程度词增加关键词语词性值...\n')
     savePath.write('      词语词性值累加获取句子词性值...\n')
     savePath.write('断开词典数据库...\n')
     savePath.write('标注句子情感倾向...\n')
     savePath.write('载入人工标记值...\n')
     savePath.write('正面情感准确率为： %.2f\n'%pos_precision)
     savePath.write('负面情感准确率为： %.2f\n'%neg_precision)
     savePath.write('正面情感召回率为： %.2f\n'%pos_recall)
     savePath.write('负面情感召回率为： %.2f\n'%neg_recall)
     savePath.write('正面F-Measure值为： %.2f\n'%F_pos)
     savePath.write('负面F-Measure值为： %.2f\n'%F_neg)
     savePath.close()
    



conclusion()





