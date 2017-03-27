def add_words(word,words_dict):
    """把单词添加到words_dict字典里，并计数"""
    if word in words_dict:
        words_dict[word]+=1
    else:
        words_dict[word]=1
 
import string
import re
from bs4 import BeautifulSoup 
def process_line(line,words_dict):
    """处理文件每行数据"""
    line=line.strip()
    words_list=line.split()
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