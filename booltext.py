import os
from time import sleep

colors={
'PINK':'\033[95m',
'RED':'\033[31m',
'GREEN':'\033[32m',
'BLUE':'\033[34m',
'YELLOW':'\033[93m',
'ORANGE':'\033[33m',
'PURPLE':'\033[35m'
}

mode = 'auto'
if mode == 'man':
	print('Choose a .btxt file:')
	bfile = input('>')
	bsplit = bfile.split('.')
	if bsplit[1] != 'btxt':
		print('Make sure that the file you are using is a .btxt file.')
		exit()
	file = open(bfile, 'r+')
	info = file.read()
elif mode == 'auto':
	file = open('.tmp_btxt', 'r+')
	bfile = file.read().strip()
	file = open(bfile, 'r')
	info = file.read()
	os.system('rm .tmp_btxt')
info = info.split('\n')

for line in info:
	if line == '':
		info.remove('')
for k in info:
	if '<CLEAR>' in info:
		os.system('clear')
		info.remove('<CLEAR>')
	if '<PINK>' in info:
		print('\033[95m',end='')
		info.remove('<PINK>')
	elif '<COLOR' in k:
		col=k.split('%')
		color=col[1]
		if color in colors:
			print(colors[color],end='')
		del info[info.index(col)]
	if '<DELAY>' in info:
		delay=True
		info.remove('<DELAY>')
	else:
		delay=False
	if '<$SHIFT>' in info:
		bangkey = 'and'
		andkey = 'or'
		orkey = 'not'
		info.remove('<$SHIFT>')
	elif '<$EXCLAMATION>' in info:
		bangkey = 'UH OH!'
		andkey = 'AND...'
		orkey = 'OR?!'
		info.remove('<$EXCLAMATION>')
	elif '<$KEYS' in k:
		key=k.split('%')
		bangkey=keys[1]
		andkey=keys[2]
		orkey=keys[3]
		del info[info.index(key)]
	else:
		bangkey='not'
		andkey='and'
		orkey='or'
	if '<SEPARATOR' in k:
		se=k.split('%')
		bkey=se[1]
		del info[info.index(se)]
	else:
		bkey='/'
	if '<C' in k:
		comment=k.split('%')
		if comment[1] == '>':
			print(comment[2])
		elif comment[1] == '*':
			print(comment[2])
			file=open(bfile, 'r')
			finfo = file.read().strip()
			finfo=finfo.split('\n')
			finfo[finfo.index(k)]=''
			file=open(bfile,'w')
			file.writelines('\n'.join(finfo))
			if len(comment) > 3:
				if comment[3] == '$':
					os.system(comment[1])
		elif comment[1] == '$':
			os.system(comment[1])
		info.remove(k)
	if '<LINK' in k:
		lkey=k.split('%')
		def com(arg):
			os.system('echo \"'+arg+'\" > .tmp_btxt && python3 \"$(cat ~/.btxt_locale)\"')
		comm=True
		info.remove(k)
	else:
		comm=False
	if '<COMMAND' in k:
		cm=k.split('%')
		os.system(cm[1])
		info.remove(k)
	if '<OUTPUT>' in k:
		ouu=k.split('%')
		info.remove(k)
		ofile=ouu[1]
		fo = '\n'.join(info)
		os.system('echo \"'+fo+'\" >> '+ofile)
	else:
		output = False
	for line in info:
		line=line.split(',')
	if '<SHOW>' in info:
		print('---------TEXT:--------')
		info.remove('<SHOW>')
		print(info)
		print('----------------------')
i=0
while i < (len(info)):
	e=0
	while e < (len(info[i])):
		sym = info[i][e]
		if e == (len(info[i])-1):
			lineend=True
		else:
			lineend=False
		if sym == '!':
			if lineend == True:
				print(bangkey)
			else:
				print(bangkey, end=bkey)
		elif sym == '&':
			if lineend == True:
				print(andkey)
			else:
				print(andkey,end=bkey)
		elif sym == '|':
			if lineend == True:
				print(orkey)
			else:
				print(orkey,end=bkey)
		e+=1
	if delay == True:
		sleep(2.5)

	i+=1
if comm == True:
	com(lkey[1])

