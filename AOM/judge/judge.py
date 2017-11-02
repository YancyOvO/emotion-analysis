
def text():
  
     f1 = open('E:/biancheng/Python/judge/good.txt','r',encoding='utf-8')
  
     f2 = open('E:/biancheng/Python/judge/bad.txt','r',encoding='utf-8')
  
     line1 = f1.readline()
  
     line2 = f2.readline()
  
     str = ''
  
     while line1:
  
         str += line1
  
         line1 = f1.readline()
  
     while line2:
  
         str += line2
  
         line2 = f2.readline()
  
     f1.close()
  
     f2.close()
     return str#返回文中句子
  
#把单个词作为特征
  
def bag_of_words(words):

     
     return dict([(word,True) for word in words])#给词加上标签True
     
#dict是在两词之间插入词语，append是在词语后面加入词语
#print(bag_of_words(text()))
  
  
import nltk
  
from nltk.collocations import  BigramCollocationFinder#双词配置（排序，组合等操作）
  
from nltk.metrics import  BigramAssocMeasures
  
  
#把双个词作为特征--使用卡方统计的方法，选择排名前1000的双词
  
def  bigram(words,score_fn=BigramAssocMeasures.chi_sq,n=1000):
  
     bigram_finder=BigramCollocationFinder.from_words(words)#把文本变成双字搭配的形式
     print(type(bigram_finder))
     bigrams = bigram_finder.nbest(score_fn,n)#使用卡方统计的方法，选择排名前1000的双词，score_fn统计二元词使用的次数
     
     newBigrams = [u+v for (u,v) in bigrams]#将双字合成一个词
     
     return bag_of_words(newBigrams)
  
#bigram(text(),score_fn=BigramAssocMeasures.chi_sq,n=1000)
  
#把单个词和双个词一起作为特征
  
def  bigram_words(words,score_fn=BigramAssocMeasures.chi_sq,n=1000):#使用卡方统计法来找出前1000词
  
     bigram_finder=BigramCollocationFinder.from_words(words)
  
     bigrams = bigram_finder.nbest(score_fn,n)
  
     newBigrams = [u+v for (u,v) in bigrams]
    # print(bigrams)
  
     a = bag_of_words(words)
  
     b = bag_of_words(newBigrams)
  
     a.update(b)#把字典b合并到字典a中
  
     return a#所有单个词和双个词一起作为特征
  
#print(bigram_words(text(),score_fn=BigramAssocMeasures.chi_sq,n=1000))

#安装结巴，进入D:\software\Python\Python35\Scripts，执行pip3 install jieba即可；卸载使用pip3  uninstall jieba即可
  
import jieba
  
#返回分词列表如：[['我','爱','北京','天安门'],['你','好'],['hello']]，一条评论一个
  
def read_file(filename):
  
     stop = [line.strip() for line in  open('E:/biancheng/Python/judge/stop.txt','r',encoding='utf-8').readlines()]#停用词
  
     f = open(filename,'r',encoding='utf-8')
  
     line = f.readline()
  
     str = []
  
     while line:
  
         s = line.split('\t')
  
         fenci = jieba.cut(s[0],cut_all=False)#False默认值：精准模式，试图将句子最精确地切开，适合文本分析
  
         str.append(list(set(fenci)-set(stop)))
  
         line = f.readline()
  
     return str

#filename ='E:/biancheng/Python/judge/tiancaifengzi.txt'
#print(read_file(filename))
#安装nltk，进入D:\software\Python\Python35\Scripts，执行pip3 install  nltk即可
  
from nltk.probability import  FreqDist,ConditionalFreqDist#frequency distributian频率分布,条件频率分布
  
from nltk.metrics import  BigramAssocMeasures
  
  
#获取信息量最高(前number个)的特征(卡方统计)
  
def jieba_feature(number):   
     
     posWords = []
  
     negWords = []
     
     for items in read_file('E:/biancheng/Python/judge/good.txt'):#把集合的集合变成集合
        
         for item in items:
  
            posWords.append(item)
            
     for items in read_file('E:/biancheng/Python/judge/bad.txt'):
  
         for item in items:
  
            negWords.append(item)
  
     word_fd = FreqDist() #可统计所有词的词频
  
     cond_word_fd = ConditionalFreqDist() #可统计积极文本中的词频或消极文本中的词频
  
     for word in posWords:
  
         word_fd[word] += 1
  
         cond_word_fd['pos'][word] += 1

     for word in negWords:
  
         word_fd[word] += 1  #word_fd.N()等价于之后的total_word_count ；word_fd['不行']将输出不行在两篇文档中出现的次数  
         
         cond_word_fd['neg'][word] += 1
         
     
     pos_word_count = cond_word_fd['pos'].N() #积极词的数量   .B()为有多少种词
  
     neg_word_count = cond_word_fd['neg'].N() #消极词的数量
    
     total_word_count = pos_word_count + neg_word_count
     
     word_scores = {}#包括了每个词和这个词的信息量
  
     for word, freq in word_fd.items():
         
         pos_score = BigramAssocMeasures.chi_sq(cond_word_fd['pos'][word],  (freq, pos_word_count), total_word_count) #计算积极词的卡方统计量，这里也可以计算互信息等其它统计量
  
         neg_score = BigramAssocMeasures.chi_sq(cond_word_fd['neg'][word],  (freq, neg_word_count), total_word_count) #同理
  
         word_scores[word] = pos_score + neg_score #一个词的信息量等于积极卡方统计量加上消极卡方统计量
  
  
     best_vals = sorted(word_scores.items(), key=lambda item:item[1],  reverse=True)[:number] #把词按信息量倒序排序。number是特征的维度，是可以不断调整直至最优的
     
     best_words = set([w for w,s in best_vals])
  
     return dict([(word, True) for word in best_words])
  
  
#构建训练需要的数据格式：
  
#[[{'买': 'True', '京东': 'True', '物流': 'True', '包装': 'True', '\n': 'True', '很快': 'True', '不错': 'True', '酒': 'True', '正品': 'True', '感觉': 'True'},  'pos'],
  
# [{'买': 'True', '\n':  'True', '葡萄酒': 'True', '活动': 'True', '澳洲': 'True'}, 'pos'],
  
# [{'\n': 'True', '价格': 'True'}, 'pos']]
  
def build_features():
  
     #四种特征选取方式，越来越好
  
     #feature = bag_of_words(text())#单个词
  
     feature = bigram(text(),score_fn=BigramAssocMeasures.chi_sq,n=500)#双个词
  
     #feature =  bigram_words(text(),score_fn=BigramAssocMeasures.chi_sq,n=500)#单个词和双个词
  
     #feature = jieba_feature(300)#结巴分词
  
     
  
     posFeatures = []
  
     for items in read_file('E:/biancheng/Python/judge/good.txt'):
  
         a = {}
  
         for item in items:
             
             if item in feature.keys():#消除了/n,变成空格
                 
                 a[item]='True'#给item打上标签True，{'公司'：True}
                 
         posWords = [a,'pos'] #为积极文本赋予"pos"
         #print(posWords)
         posFeatures.append(posWords)
         
     #print(posFeatures)    
     negFeatures = []
  
     for items in read_file('E:/biancheng/Python/judge/bad.txt'):
  
         a = {}
  
         for item in items:
             
             if item in feature.keys():
  
                 a[item]='True'
  
         negWords = [a,'neg'] #为消极文本赋予"neg"
  
         negFeatures.append(negWords)
  
     return posFeatures,negFeatures
  
  
posFeatures,negFeatures =  build_features()#获得训练数据
  
from random import shuffle
  
shuffle(posFeatures) #把文本的排列随机化
  
shuffle(negFeatures) #把文本的排列随机化
  
  
train =  posFeatures[200:]+negFeatures[200:]#训练集(80%)
  
test = posFeatures[:200]+negFeatures[:200]#预测集(验证集)(20%)
 
shuffle(test) 
  
data,tag = zip(*test)#分离测试集合的数据和标签，便于验证和测试

  
def score(classifier):
     
     classifier = SklearnClassifier(classifier) #在nltk中使用scikit-learn的接口
  
     classifier.train(train) #训练分类器
  
  
     pred = classifier.classify_many(data) #对测试集的数据进行分类，给出预测的标签
  
     n = 0
  
     s = len(pred)
     
     for i in range(0,s):
         
         if pred[i]==tag[i]:
  
             n = n+1
             
  
     return n/s #对比分类预测结果和人工标注的正确结果，给出分类器准确度
  
  
#安装sklearn，进入D:\software\Python\Python35\Scripts，执行pip3 install  sklearn即可，而sklearn依赖于scipy，所以如果没有安装运行会报错说没有scipy模块。
  
#直接安装pip3 install  scipy报错，报no lapack/blas resources found这个错误，那么采用手动安装，访问http://www.lfd.uci.edu/~gohlke/pythonlibs这个网址，
  
#找到scipy，下载对应版本的whl，如python3.5对应的scipy-0.18.1-cp35-cp35m-win_amd64.whl，执行pip3 install scipy-0.18.1-cp35-cp35m-win_amd64.whl，安装完
  
#之后可以删除安装包whl。再次运行报没有numpy_mkl,发现已经安装了numpy，前者包含后者，所以可以先卸载numpyip3 uninstall numpy。
  
#在上面同样的网址下下载numpy-1.11.2+mkl-cp35-cp35m-win_amd64.whl,然后安装，再次运行即可
  
import sklearn
  
  
from nltk.classify.scikitlearn import  SklearnClassifier
  
from sklearn.svm import SVC, LinearSVC,  NuSVC
  
from sklearn.naive_bayes import  MultinomialNB, BernoulliNB
  
from sklearn.linear_model import  LogisticRegression
  
from sklearn.metrics import  accuracy_score

dict = {'sdfa':'afaf', 'adfa':'asfa'}
print(dict.keys())
  
print('BernoulliNB`s accuracy is %f'  %score(BernoulliNB()))
  
print('MultinomiaNB`s accuracy is %f'  %score(MultinomialNB()))
  
print('LogisticRegression`s accuracy is  %f' %score(LogisticRegression()))
  
print('SVC`s accuracy is %f'  %score(SVC()))
  
print('LinearSVC`s accuracy is %f'  %score(LinearSVC()))
  
print('NuSVC`s accuracy is %f'  %score(NuSVC()))

posWords = []

  
