#coding:utf-8
with open('word_to_pinyin.txt') as fr:
    data = fr.readlines()

word2pinyin = {}
for line in data:
    line = line.strip().split('\t')
    word2pinyin[line[0]] = line[1]

with open('word2pinyin.txt','w') as fw:
    for key,value in word2pinyin.items():
        fw.write(key+'\t'+value+'\n')