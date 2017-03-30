def add_words(word,words_dict):
	"""把单词添加到words_dict字典里，并计数"""
	if word in words_dict:
		words_dict[word]+=1
	else:
		words_dict[word]=1
 
import string
import re
from bs4 import BeautifulSoup

def	multiple_replace(str):
	str = str.replace("A", " A")
	str = str.replace("Q", " Q")
	str = str.replace("W", " W")
	str = str.replace("E", " E")
	str = str.replace("R", " R")
	str = str.replace("T", " T")
	str = str.replace("Y", " Y")
	str = str.replace("U", " U")
	str = str.replace("I", " I")
	str = str.replace("O", " O")
	str = str.replace("P", " P")
	str = str.replace("S", " S")
	str = str.replace("D", " D")
	str = str.replace("F", " F")
	str = str.replace("G", " G")
	str = str.replace("H", " H")
	str = str.replace("J", " J")
	str = str.replace("K", " K")
	str = str.replace("L", " L")
	str = str.replace("Z", " Z")
	str = str.replace("X", " X")
	str = str.replace("C", " C")
	str = str.replace("V", " V")
	str = str.replace("B", " B")
	str = str.replace("N", " N")
	str = str.replace("M", " M")
	return str
def process_line(line,words_dict):
	"""处理文件每行数据"""
	line = re.sub(r"[\~\!\@\#\$\%\^\&\*\(\)\_\+\}\{\|\"\:\?\>\<\,\.\/\;\'\\\]\[\=\-\`\']", ' ', line)  # 过滤符号
	line = line.strip()
	words_list = line.split()
	# 把一个单词全部大写转换为小写
	i = 0
	while i < len(words_list):
		if str(words_list[i]).isupper():
			words_list[i] = words_list[i].lower()
			# del words_list[i]
		else:
			i += 1
	# print(words_list)
	line_two = ' '.join(words_list)#列表转换字符串
	line_two = multiple_replace(line_two)
	words_list = line_two.split()
	for word in words_list:
		word=word.lower().strip(string.punctuation)  #删除进过分割的单词的尾部的一些符号
		add_words(word,words_dict)   #调用add_words函数，把单词插入到words_dict字典中
 
def print_result(words_dict):
	"""按格式输出words_dict中的数据"""
	pFilemove=open("move.txt","r")
	removewords=stripNonAlphaNum(pFilemove.read())#读取需要过滤单词
	val_key_list=[]
	for key,val in words_dict.items():
		# if len(key)>2 and val>1 and key not in removewords:       #过滤结果，只输出词频大于1以及单词长度大于2的单词
		if len(key)>2 and key.isalpha() and key not in removewords:       #isalpha()函数来判断英文字符，如果是英文字母，则输出true,否则，输出false示例代码
			val_key_list.append((key))
	val_key_list.sort()  #对val值进行逆排序
	print ("%-10s%-10s" %("word","count"))
	print ("_"*25)
	for key in val_key_list:
		# print ("%-12s   %3d" %(key,val))
		print ("%-s" %(key))#去掉统计

 # def removeStopwords(wordlist, stopwords):
 #    return [w for w in wordlist if w not in stopwords]

def stripNonAlphaNum(text):
	return re.compile(r'\W+', re.UNICODE).split(text)
 
##################################################
def main():
	"""主函数"""
	words_dict={}
	pFile=open("test.txt","r")

	for line in pFile:
		process_line(line,words_dict)
	print ("the length of the dictionary:",len(words_dict))
	print_result(words_dict)

main()