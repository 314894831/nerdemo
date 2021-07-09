# 将原有文本转换为模型的输入文本
import os
import glob
import pandas as pd
import jieba
import sys


text_path=sys.argv[1]+"\*"
csv_path='src/main/java/com/ner/demo/txts/ourtrain1.csv'#手工标注

def load_entity_label():
    label=set()
    entity=[]
    origin_result={}
    df=pd.read_csv(csv_path,sep=',', header=0,encoding="gbk")
    for row in df.iterrows():
        label.add(row[1]['实体类型'])
        entity.append(row[1]['实体名称'])
        origin_result[row[1]['实体名称']]=row[1]['实体类型']
    return label, entity, origin_result


#jieba分词，实体标注
def transform():
    origin_label, entity,origin_result=load_entity_label()

    #load dics
    for i in entity:
        jieba.add_word(i)
    
    # 分词
    s=[]
    paths=glob.glob(text_path)
    for p in paths:
        with open(p,'r', encoding='utf-8') as f:
            s.extend(jieba.lcut(f.read()))
    
    for ss in range(0, len(s)):
        if '\n' in s[ss]:s[ss].replace('\n','')


    # label transform
    with open('src/main/java/com/ner/demo/txts/chs_eng.txt','r', encoding='utf-8') as f2:
        var=f2.read()
    var=var.split('\n')
    var_dic={}
    for v in var:
        vv=v.split('\t')
        if len(vv)!=0:
            var_dic[vv[0]]=[vv[1], vv[2]]
    new_result=[]
    for word in s:
        if len(word)==0:
            varrr=[]
            varrr.append('')
            varrr.append('O')
            new_result.append(varrr)
            continue
        
        if len(word)==1 and word[0]=='\n':
            varrr=[]
            varrr.append('')
            varrr.append('O')
            new_result.append(varrr)
            continue
        

        if word in origin_result.keys():
            begin_label=var_dic[origin_result[word]][0]
            end_label=var_dic[origin_result[word]][1]

            for index in range(0, len(word)):
                varrr=[]
                varrr.append(word[index])
                if index==0:
                    varrr.append(begin_label)
                else:
                    varrr.append(end_label)
                new_result.append(varrr)
  
        else:
            for index in range(0, len(word)):
                varrr=[]
                varrr.append(word[index])
                varrr.append('O')
                new_result.append(varrr)

    #write result
    with open('src/main/java/com/ner/demo/txts/jieba_result.txt','w', encoding='utf-8') as f3:
        for nr in new_result:
            # 跳过空格与回车
            # if  nr[0][0]=='\n':continue
            f3.write('{}\t{}\n'.format(nr[0], nr[1]))


    

transform()