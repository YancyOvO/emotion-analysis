import jieba
import re
import SQL_Conn
import issue2

rhe_good = open("data/issue/good.txt", "r", encoding = "utf-8")
rhe_bad = open("data/issue/bad.txt", "r", encoding = "utf-8")
dis_rhe = open("data/issue/dis_rhe.txt", "r", encoding = "utf-8")

def judge_issue(txt):
    cs = SQL_Conn.cs() 
    con = []
    for words in txt:
         sentence = 0
         prefer = 1
         label = []
         fenci = jieba.cut(words,cut_all=False)
         t = list(fenci)
         imp_2 = False
         n = 0
         word_emo = 0
         for word in t:
#             sen = sentence
#             pre = prefer
             row_count = cs.execute("select word,emotion from base_dict_issue where word = %s", (word))
             if row_count and not re.findall('不', word) and not re.findall('没', word):
                row = cs.fetchone()
                if row[1] == 'pos':
                    word_emo+=1
                else:
                    word_emo-=1
                #print(row[0], word_emo)
             if re.findall('你', word)and sentence==0:
                 prefer *= -1
             if word == '难道'or word =='哪能'or word == '怎能' or word =='哪'or word =='何必':#直接关键词
                 if sentence != -1:
                     sentence = -1#反问句
                     prefer *= -1#句意相反
             if word =='怎能不' or word =='能不' or word == '非得':
                 if sentence != -1:
                     sentence = -1#反问句
             if word == '怎么' :#一级间接关键词
                 if sentence != -1:
                     sentence = -3#确定为问句但不确定是否为反问句
                     prefer *= -1
             if sentence == -3:
                 if re.findall('能', word) or word == '可以' or word == '还'or word =='会' :#辅助关键词
                     sentence = -1
             if re.findall('就', word)or re.findall('还', word)or word == '哪里' or word == '谁':#二级间接关键词
                 #prefer = -1
                 imp_2 = True
             if word =='不是' or word == '不'or word =='不像'or word =='没有' or word == '没'or word =='没什么':#反义关键词
                 if sentence %2 ==0:
                     if imp_2 == True:
                         sentence -=2#q趋向于反问句
                     else:
                         n = 2
                     prefer *= -1
                 elif sentence == -1 :
                     prefer *=-1
             if re.findall('都', word)or re.findall('正是', word)or re.findall('也', word)or re.findall('还', word):
                 if n >0:
                     sentence = -1
                     prefer *= -1
                     n = 0
             if re.findall('就', word):
                 if n >0:
                     sentence = -1
                     prefer = -1
                     n = -1
                 continue
             if word == '么'or word == '吗'or word == '?'or word =='？':#问句关键词
                 if sentence %2==0 and sentence <0:
                     sentence = -1
                     prefer *= -1
                 elif sentence %2==1 and sentence <0:
                     sentence = -1
             if word == '?' or word =='？'or word ==','or word =='，'or word =='。' or word ==' ' or word ==']'or word =='!'or word =='！' or word =='…':
                 if sentence==-1:
                     #print(word, sentence, prefer)
                     break
                 else:
                     sentence = 0
                     prefer = 1
                     imp_2 = False
                     word_emo = 0
             if n != 0:
                 n -= 1
                 
             #if sentence != sen or prefer != pre:
             #print(word, sentence, prefer)
         if word_emo>=0:
             word_emo = 1
         else:
             word_emo = -1
         if n != -1:
             prefer = prefer * word_emo
         label = [words, sentence, prefer]
         print(label)
         con.append(label)
    SQL_Conn.close()
    #txt.close()
    return con

def judge_issue_line(line):
     cs = SQL_Conn.cs()
     sentence = 0
     prefer = 1
     label = []
     imp_2 = False
     n = 0
     word_emo = 0
     for word in line:
         row_count = cs.execute("select word,emotion from base_dict_issue where word = %s", (word))
         if row_count and not re.findall('不', word) and not re.findall('没', word):
            row = cs.fetchone()
            if row[1] == 'pos':
                word_emo+=1
            else:
                word_emo-=1
            #print(row[0], word_emo)
         if re.findall('你', word)and sentence==0:
             prefer *= -1
         if word == '难道'or word =='哪能'or word == '怎能' or word =='哪'or word =='何必':#直接关键词
             if sentence != -1:
                 sentence = -1#反问句
                 prefer *= -1#句意相反
         if word =='怎能不' or word == '能不':
             if sentence != -1:
                 sentence = -1#反问句
         if word == '怎么' :#一级间接关键词
             if sentence != -1:
                 sentence = -3#确定为问句但不确定是否为反问句
                 prefer *= -1
         if sentence == -3:
             if re.findall('能', word) or word == '可以' or word == '还'or word =='会' :#辅助关键词
                 sentence = -1
         if re.findall('就', word)or re.findall('还', word)or word == '哪里' or word == '谁':#二级间接关键词
             #prefer = -1
             imp_2 = True
         if word =='不是' or word == '不'or word =='不像'or word =='没该' or word == '没'or word =='没什么':#反义关键词
             if sentence %2 ==0:
                 if imp_2 == True:
                     sentence -=2#q趋向于反问句
                 else:
                     n = 2
                 prefer *= -1
             elif sentence == -1 :
                 prefer *=-1
         if re.findall('都', word)or re.findall('正是', word)or re.findall('也', word):
             if n >0:
                 sentence = -1
                 prefer *= -1
                 n = 0
         if re.findall('就', word):
             if n >0:
                 sentence = -1
                 prefer = -1
                 n = -1
             continue
         if word == '么'or word == '吗'or word == '?'or word =='？':#问句关键词
             if sentence %2==0 and sentence <0:
                 sentence = -1
                 prefer *= -1
             elif sentence %2==1 and sentence <0:
                 sentence = -1
         if word == '?' or word =='？'or word ==','or word =='，'or word =='。' or word ==' ' or word ==']'or word =='!'or word =='！' or word =='…':
             if sentence==-1:
                 #print(word, sentence, prefer)
                 break
             else:
                 sentence = 0
                 prefer = 1
                 imp_2 = False
                 word_emo = 0
         if n != 0:
             n -= 1
             
         #if sentence != sen or prefer != pre:
         #print(word, sentence, prefer)
     if word_emo>=0:
         word_emo = 1
     else:
         word_emo = -1
     if n != -1:
         prefer = prefer * word_emo
     label = [line, sentence, prefer]
     #print(label)
     return label 

#dd = ['…', '…', '评论', '里', '的', '人', '都', '有', '病', '吧', '，', '张子', '萱', '就是', '长得', '漂亮', '陈赫', '为什么', '不能', '跟', '她', '在', '一起', '啊', '🙄', '️', '媒体', '说', '小', '三', '她', '就', '小', '三', '了', '？', '🙄', '️'] #
#
#fenci = jieba.cut("非得洗白了才能发微博？",cut_all=False)
#t = list(fenci)
#judge_issue_line(t)

def conclusion():
    n1 = 0
    m1 = 0
    n2 = 0
    m2 = 0
    n = 0
    c_good = judge_issue(rhe_good)
    c_bad = judge_issue(rhe_bad)
    c_dis_rhe = judge_issue(dis_rhe)
    for d in c_dis_rhe:
        if d[1] == 0:
            n+=1
    for g in c_good:
        if g[1] == -1:
            n1+=1
            if g[2] == 1:
                m1+=1
    for b in c_bad:
        if b[1] == -1:
            n2+=1
            if b[2] == -1:
                m2+=1   
    print(n1, m1, n2, m2)
    rhe_Y = (n1+n2)/(len(c_good)+len(c_bad))
    rhe_N = n/len(c_dis_rhe)
    pos_precision = m1/(m1+n2-m2)
    neg_precision = m2/(m2+n1-m1)
    pos_recall = m1/n1
    neg_recall = m2/n2
    F_pos = 2*pos_precision*pos_recall/(pos_precision+pos_recall )
    F_neg = 2*neg_precision*neg_recall/(neg_precision+neg_recall )
    print('反问句识别率', rhe_Y)
    print('非反问句识别率', rhe_N)
    print('正面情感准确率', pos_precision)
    print('负面情感准确率', neg_precision)
    print('正面情感召回率', pos_recall)
    print('负面情感召回率', neg_recall)
    print('正面F-Measure值', F_pos)
    print('负面F-Measure值', F_neg)

    
def conclusion2():
    n1 = 0
    m1 = 0
    n2 = 0
    m2 = 0
    n = 0    
    c_good2 = issue2.judge_issue(rhe_good)
    c_bad2 = issue2.judge_issue(rhe_bad)
    c_dis_rhe2 = issue2.judge_issue(dis_rhe)    
    for d in c_dis_rhe2:
        if d[1] == 0:
            n+=1
    for g in c_good2:
        if g[1] == -1:
            n1+=1
            if g[2] == 1:
                m1+=1
    for b in c_bad2:
        if b[1] == -1:
            n2+=1
            if b[2] == -1:
                m2+=1   
    print(n1, m1, n2, m2)
    rhe_Y = (n1+n2)/(len(c_good2)+len(c_bad2))
    rhe_N = n/len(c_dis_rhe2)

    pos_precision = m1/(m1+n2-m2)
    neg_precision = m2/(m2+n1-m1)
    pos_recall = m1/n1
    neg_recall = m2/n2

    F_pos = 2*pos_precision*pos_recall/(pos_precision+pos_recall )
    F_neg = 2*neg_precision*neg_recall/(neg_precision+neg_recall )
    print('反问句识别率', rhe_Y)
    print('非反问句识别率', rhe_N)
    print('正面情感准确率', pos_precision)
    print('负面情感准确率', neg_precision)
    print('正面情感召回率', pos_recall)
    print('负面情感召回率', neg_recall)
    print('正面F-Measure值', F_pos)
    print('负面F-Measure值', F_neg)
    
conclusion()
#conclusion2()


