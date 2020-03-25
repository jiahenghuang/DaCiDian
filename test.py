#coding:utf-8
with open('tmp1') as fr:
    data = fr.readlines()

word2pinyin = {}
for line in data:
    line = line.strip().split('\t')
    if line[0] not in word2pinyin:
        word2pinyin[line[0]] = line[1]

with open('word2pinyin.txt','w') as fw:
    for key,value in word2pinyin.items():
        fw.write(key+'\t'+value+'\n')