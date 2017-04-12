#coding:utf-8
import os


def dir_list(dir_name, subdir, *args):
	'''Return a list of file names in directory 'dir_name'
	If 'subdir' is True, recursively access subdirectories under 'dir_name'.
	Additional arguments, if any, are file extensions to add to the list.
	Example usage: fileList = dir_list(r'H:\TEMP', False, 'txt', 'py', 'dat', 'log', 'jpg')
	'''
	fileList = []
	for file in os.listdir(dir_name):
		dirfile = os.path.join(dir_name, file)
		if os.path.isfile(dirfile):
			if len(args) == 0:
				fileList.append(dirfile)
			else:
				if os.path.splitext(dirfile)[1][1:] in args:
					fileList.append(dirfile)

		# recursively access file names in subdirectories
		elif os.path.isdir(dirfile) and subdir:
			# print "Accessing directory:", dirfile
			fileList += dir_list(dirfile, subdir, *args)
	return fileList


def combine_files(fileList, fn):
	f = open(fn, 'a',encoding='utf-8')
	for file in fileList:
		print('Writing file %s' % file)
		#写入过滤符号
		f.write(open(file,encoding='utf-8').read())
		# f.write('a,')
	f.close()


if __name__ == '__main__':
	blank = open('output_file.txt','w')  #新建空白文件TXT
	blank.close()
	search_dir = "D:/python/word-count/laravel"
	fn = "output_file.txt"
	# combine_files(dir_list(search_dir, False, 'txt'), fn)
	for root, dirs, files in os.walk(search_dir):
		root = root.replace( "\\","/") #转换root path
		root = root+"/"

		combine_files(dir_list(root, False, 'txt','php','py','json'), fn)
		# print(root)