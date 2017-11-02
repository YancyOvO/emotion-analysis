import jieba
import itertools
import SQL_Conn
#txt = open("D:/Backup/Desktop/2/wenju_weibo.txt", "r", encoding = "utf-8")


def load_issueWord():
     degree = [] 
     test = open('data/issue/judge_word.txt','r',encoding='utf-8')
     for items in test:
         b = list(items.split())
         #print(type(b))
         b = "".join(itertools.chain(b))
         degree.append(b)
     test.close()
     return degree

#judge_word = load_issueWord('E:/biancheng/Python/AOM/data/issue/judge_word.txt')   # 权值为2

def judge_issue(txt):
    cs = SQL_Conn.cs() 
    judge_word = load_issueWord()
    con = []
    for words in txt:
         word_emo = 0
         emo = []
         a = 0
         b = 1
         que = False
         fenci = jieba.cut(words,cut_all=False)
         t = list(fenci)    
         for word in t:
             row_count = cs.execute("select word,emotion from base_dict_issue where word = %s", (word))  
             if row_count:
                 row = cs.fetchone()
                 if row[1] == 'pos':
                     word_emo+=1
                 else:
                     word_emo-=1   
         if "?"or "？" in t:
             que = True
         for word in t[0:]:
             #print(word)
             if word in judge_word:
                 if que == True:
                     a = -1
                     b = -1
         b = word_emo * b
         if b >=1:
             b = 1
         elif b<=-1:
             b = -1
         emo = [words, a, b]
         #print(emo)
         con.append(emo)
    txt.close()
    cs.close()
    return con

def judge_issue_line(line):
     judge_word = load_issueWord()
     emo = []
     a = 0
     b = 0
     que = False       
     if "?" in line:
         que = True
     for word in line[0:]:
         if word in judge_word:
             if que == True:
                 a = -1
                 b = -1
     emo = [line, a, b]
     #print(emo)
     return emo
    
#judge_issue()
