import json

import codecs

def write_f(str):#写入sql文档

     file_object = codecs.open('data/sql/chenhe.sql', 'w', 'utf-8')
     
     file_object.write(str)
     
     file_object.close()
     
     print('success')


def check_key_value(fdict):
    
     if isinstance(fdict, list):
         
         global len_f
         
         global str
         
         str = ''
         
         len_f = len(fdict)#循环次数
         
         for element in fdict:#所有element同时进入
             
             check_key_value(element)
             
     elif isinstance(fdict, dict):
         
         #print(fdict)
         # i = eval(item)转为字典
         #i = item 
         #str = str + "insert into tencent(mid,attitudes_count,comments_count,reposts_count,geo,text,user,created_at) values " +"('%s','%s','%s','%s','%s','%s','%s','%s');\r\n" % (fdict["mid"], fdict['attitudes_count'],fdict['comments_count'], fdict['reposts_count'], fdict['geo'], fdict['text'])
         
         len_f -= 1
         
         print(len_f)
         
         str = str + "insert into comment(text) values "+"('%s');\r\n"%fdict["text"]
         #  print(str)
    
         if len_f == 0:
             #print(str)
             
             print(str)
             
             write_f(str)

data = []

with open('data/sql/chenhe.json') as f:
    
    for items in f:
        
         data.append(json.loads(items))
         
f.close()
#print(json.dumps(data, ensure_ascii=False))#将dict转为str，并且将ascii码关掉，输出中文

check_key_value(data)
#采用递归判断的方式将二维JSON列表转换为一维字典，减少
#l = [{"a":"b", "c":"d"}, {"a":"v", "c":"n"}]
#for item in l:
#    print(item, "sdfsdf")
#    print(item["a"])
#一般遍历提取带来的时间复杂度的提升，一般遍历方式会每次将整个列表进行遍历
