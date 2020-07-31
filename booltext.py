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
	info = file.read().strip()
	file = open(info, 'r')
	info = file.read()
	os.system('rm .tmp_btxt')
info = info.split('\n')

for line in info:
	if line == '':
		info.remove('')
if '<RESET>' in info:
	os.system('reset')
	info.remove('<RESET>')
if '<PINK>' in info:
	print('\033[95m',end='')
	info.remove('<PINK>')
elif '<COLOR>' in info:
	colordex = info.index('<COLOR>')+1
	color=info[colordex]
	if color in colors:
		print(colors[color],end='')
	del info[colordex]
	info.remove('<COLOR>')
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
elif '<$KEYS>' in info:
	keylo = info.index('<$KEYS>')+1
	keys = info[keylo]
	keys = keys.split('/')
	bangkey=keys[0]
	andkey=keys[1]
	orkey=keys[2]
	del info[keylo]
	info.remove('<$KEYS>')
else:
	bangkey='not'
	andkey='and'
	orkey='or'
if '<SEPARATOR>' in info:
	bkey = info[info.index('<SEPARATOR>')+1]
	del info[info.index(bkey)]
	info.remove('<SEPARATOR>')
else:
	bkey='/'
for line in info:
	line = line.split(',')
if '<C>' in info:
	cdex = info.index('<C>')+1
	comment = info[cdex]
	comment = comment.split(':')
	if comment[0] == '>':
		print(comment[1])
	elif comment[0] == '!':
		print(comment[1])
		finfo = file.readlines()
		finfo[cdex] = ''
		finfo[cdex-1]=''
		file.writelines(finfo)
	elif comment[0] == '$':
		os.system(comment[1])
	del info[cdex]
	info.remove('<C>')
if '<COMMAND>' in info:
	cmkey = info.index('<COMMAND>')+1
	cm = info[cmkey]
	os.system(cm)
	del info[cmkey]
	info.remove('<COMMAND>')
if '<OUTPUT>' in info:
	output = True
	okey = info.index('<OUTPUT>') + 1
	ofile = info[okey]
	del info[okey]
	info.remove('<OUTPUT>')
	fo = '\n'.join(info)
	os.system('echo \"'+fo+'\" >> '+ofile)
else:
	output = False
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
