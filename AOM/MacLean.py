import jieba

#返回分词列表如：[['我','爱','北京','天安门'],['你','好'],['hello']]，一条评论一个
import os
def read_file(filename):
     stop = [line.strip() for line in  open('judge/stop.txt','r',encoding='utf-8').readlines()]#停用词
     f = open(filename,'r',encoding='utf-8')
     line = f.readline()
     str = []
     while line:
         s = line.split('\t')
         fenci = jieba.cut(s[0],cut_all=False)#False默认值：精准模式，试图将句子最精确地切开，适合文本分析
         str.append(list(set(fenci)-set(stop)))
         line = f.readline()
     return str

from nltk.probability import  FreqDist,ConditionalFreqDist#frequency distributian频率分布,条件频率分布
from nltk.metrics import  BigramAssocMeasures
#获取信息量最高(前number个)的特征(卡方统计)

print(os.getcwd())
savePath=open('outcome/mac.txt', 'w', encoding = 'utf-8')

  
def jieba_feature(number):   
     posWords = []
     negWords = []
     for items in read_file('data/weibo_data/pos_weibo.txt'):#把集合的集合变成集合
         for item in items:
            posWords.append(item)
     for items in read_file('data/weibo_data/neg_weibo.txt'):
         for item in items:
            negWords.append(item)
     word_fd = FreqDist() #可统计所有词的词频
     pol_word_fd = ConditionalFreqDist() #可统计积极文本中的词频或消极文本中的词频
     for word in posWords:
         word_fd[word] += 1
         pol_word_fd['pos'][word] += 1
     for word in negWords:
         word_fd[word] += 1  #word_fd.N()等价于之后的total_word_count ；word_fd['不行']将输出不行在两篇文档中出现的次数  
         pol_word_fd['neg'][word] += 1
     pos_word_count = pol_word_fd['pos'].N() #积极词的数量   .B()为有多少种词
     neg_word_count = pol_word_fd['neg'].N() #消极词的数量
     total_word_count = pos_word_count + neg_word_count
     word_scores = {}#包括了每个词和这个词的信息量
     for word, freq in word_fd.items():
         pos_score = BigramAssocMeasures.chi_sq(pol_word_fd['pos'][word],  (freq, pos_word_count), total_word_count) #计算积极词的卡方统计量，这里也可以计算互信息等其它统计量
         neg_score = BigramAssocMeasures.chi_sq(pol_word_fd['neg'][word],  (freq, neg_word_count), total_word_count) #同理
         word_scores[word] = pos_score + neg_score #一个词的信息量等于积极卡方统计量加上消极卡方统计量
     best_vals = sorted(word_scores.items(), key=lambda item:item[1],  reverse=True)[:number] #把词按信息量倒序排序。number是特征的维度，是可以不断调整直至最优的
     best_words = set([w for w,s in best_vals])
     return dict([(word, True) for word in best_words])
  
  
#构建训练需要的数据格式：
  
#[[{'买': 'True', '京东': 'True', '物流': 'True', '包装': 'True', '\n': 'True', '很快': 'True', '不错': 'True', '酒': 'True', '正品': 'True', '感觉': 'True'},  'pos'],

  
def build_features():
     feature = jieba_feature(300)#结巴分词
     posFeatures = []
     for items in read_file('E:/biancheng/Python/AOM/data/weibo_data/pos_weibo.txt'):
         a = {}
         for item in items:
             if item in feature.keys():#消除了/n,变成空格
                 a[item]='True'#给item打上标签True，{'公司'：True}
         posWords = [a,'pos'] #为积极文本赋予"pos"
         #print(posWords)
         posFeatures.append(posWords)
     #print(posFeatures)    
     negFeatures = []
  
     for items in read_file('data/weibo_data/neg_weibo.txt'):
         a = {}
         for item in items:
             if item in feature.keys():
                 a[item]='True'
         negWords = [a,'neg'] #为消极文本赋予"neg"
         negFeatures.append(negWords)

     return posFeatures,negFeatures
  
  
posFeatures,negFeatures =  build_features()#获得训练数据

from random import shuffle

#shuffle(posFeatures) #把文本的排列随机化
shuffle(negFeatures) #把文本的排列随机化
pos_len = int(len(posFeatures)/5)
neg_len = int(len(negFeatures)/5)
train = posFeatures[pos_len:]+negFeatures[neg_len:]#训练集(80%)
test_pos = posFeatures[:pos_len]
test_neg = negFeatures[:neg_len]#预测集(验证集)(20%)
shuffle(test_pos)
shuffle(test_neg)
data_pos,tag_pos = zip(*test_pos)#分离测试集合的数据和标签，便于验证和测试
data_neg, tag_neg = zip(*test_neg)

  
def score(classifier):
     classifier = SklearnClassifier(classifier) #在nltk中使用scikit-learn的接口
     classifier.train(train) #训练分类器
     pred_pos = classifier.classify_many(data_pos) #对测试集的数据进行分类，给出预测的标签
     pred_neg = classifier.classify_many(data_neg)
     n = 0    
     n2 = 0 
     for i in range(0,pos_len):
         if pred_pos[i]==tag_pos[i]:
             n += 1
     for i in range(0, neg_len):
         if pred_neg[i]==tag_neg[i]:
             n2 += 1
     pos_precision = n/(n+neg_len-n2)
     pos_recall = n/pos_len
     neg_precision = n2/(n2+pos_len-n)
     neg_recall = n2/neg_len
     pos_F = 2*pos_precision*pos_recall/(pos_precision+pos_recall)
     neg_F = 2*neg_precision*neg_recall/(neg_precision+neg_recall)
     print(pos_F, neg_F)
     savePath.write('正面情感准确率为： %.2f\n'%pos_precision)
     savePath.write('负面情感准确率为： %.2f\n'%neg_precision)
     savePath.write('正面情感召回率为： %.2f\n'%pos_recall)
     savePath.write('负面情感召回率为： %.2f\n'%neg_recall)
     savePath.write('正面F-Measure值为： %.2f\n'%pos_F)
     savePath.write('负面F-Measure值为： %.2f\n'%neg_F)
     return pos_precision, neg_precision,  pos_recall, neg_recall #对比分类预测结果和人工标注的正确结果，给出分类器准确度
  
from nltk.classify.scikitlearn import  SklearnClassifier
#from sklearn.svm import LinearSVC,  NuSVC
from sklearn.naive_bayes import  MultinomialNB, BernoulliNB
#from sklearn.linear_model import  LogisticRegression

savePath.write('载入停用词...\n')
savePath.write('预处理句子：\n')
savePath.write('     进行结巴分词...\n')
savePath.write('     去除停用词...\n')
savePath.write('构建词袋：\n')
savePath.write('     卡方检验计算词语信息量...\n')
savePath.write('     标注词语词性...\n')
savePath.write('以2：8的比例构建测试集和训练集...\n')
savePath.write('分离测试集数据和标签...\n')
savePath.write('训练分类器...\n')
savePath.write('测试集分类...\n')
print('BernoulliNB`s accuracy is %.2f,%.2f,%.2f,%.2f'  %score(BernoulliNB()))
#print('MultinomiaNB`s accuracy is %.2f,%.2f,%.2f,%.2f'  %score(MultinomialNB()))
#print('LogisticRegression`s accuracy is  %.2f,%.2f,%.2f,%.2f' %score(LogisticRegression()))
#print('SVC`s accuracy is %.2f,%.2f,%.2f,%.2f'  %score(SVC()))
#print('LinearSVC`s accuracy is %.2f,%.2f,%.2f,%.2f'  %score(LinearSVC()))
#print('NuSVC`s accuracy is %.2f,%.2f,%.2f,%.2f'  %score(NuSVC()))


savePath.close()
