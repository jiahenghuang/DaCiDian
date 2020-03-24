import pypinyin

def word2pinyin(word):
	result = []
	for char in word:
		tmp = pypinyin.lazy_pinyin(char)[0].upper()+'_1'
		result.append(tmp)
	return ' '.join(result)

with open('tmp3.txt') as fr:
	data=fr.readlines()

with open('xxxx.txt','w') as fw:
	for line in data:
		line = line.strip()
		result = word2pinyin(line)
		if result:
			fw.write(line+'\t'+result+'\n')