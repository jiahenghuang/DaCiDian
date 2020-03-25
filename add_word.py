#coding:utf-8
from pypinyin import pinyin, lazy_pinyin, Style

def word2pinyin(word):
    result = pinyin(word, style=Style.TONE3, heteronym=True)
    result_new = []
    for char in result:
        char = char[0]
        char = char[:-1].upper()+'_'+char[-1]   
        result_new.append(char)
    return ' '.join(result_new)

with open('word_to_pinyin.txt') as fr:
	data=fr.readlines()

with open('xxxx.txt','w') as fw:
	for line in data:
		line = line.strip().split('\t')[0]
		result = word2pinyin(line)
		if result:
			fw.write(line+'\t'+result+'\n')