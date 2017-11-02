import numpy as np
import matplotlib.pyplot as plt

def DrawPlt(dic):
    labels = 'pos', 'no_emo', 'neg'
    result = [0, 0, 0]
    pos = 0
    neg = 0
    no_emo = 0
    n=0
    for i in dic:
        if i > 0:
            result[0]+=1
        elif i == 0:
            result[1]+=1
        else:
            result[2]+=1
        n+=1
    if n == 0:
        no_emo = 100
    else:
        pos = result[0]/n*100
        no_emo = result[1]/n*100
        neg = result[2]/n*100
            
    fracs = [pos, no_emo, neg]
    explode = [0.0, 0.0, 0.0] # 0.1 凸出这部分，
    #colors = ['#dc4d01', '#fd8d49', '#ffb07c']
    colors = ['w', '#b6ffbb', '#d6b4fc']
    #colors = ['#6dedfd', '#8af1fe', '#bdf6fe']
    #colors = ['#014d4e', '#0a888a', '#05696b'], '#f0944d'
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    #autopct ，show percet
    plt.pie(x=fracs, labels=labels, colors=colors, explode=explode,autopct='%3.1f %%',
            shadow=False, labeldistance=1.1, startangle = 90,pctdistance = 0.6
     
            )
    '''
    labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    shadow，饼是否有阴影
    startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    pctdistance，百分比的text离圆心的距离
    patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    '''
    plt.title("Pie chart of emotion distribution")  
    plt.savefig('outcome/plt_outcome.png', format='png', bbox_inches='tight', transparent=True, dpi=53) # bbox_inches='tight' 图
    plt.close()
    
plt.show()
