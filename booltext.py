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
info=['8','8','8','8']
def indone(junk):
	kdone=0
	for qwerty in junk:
		if '<' in qwerty:
			kdone+=1
	if kdone < 1:
		return 0
	else:
		return 1
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
lkey=''
btxtdone=False
identt=False
while indone(info) == True:
	identt=True
	for k in info:
		if btxtdone == False:
			if '<BTXT>' in k:
				info.remove(k)
				btxtdone=True
			else:
				if btxtdone == False:
					print('No BTXT identifier found in file')
		if '<CLEAR>' == k:
			os.system('clear')
			info.remove('<CLEAR>')
		if '<PINK>' == k:
			print('\033[95m',end='')
			info.remove('<PINK>')
		if '<COLOR' in k:
			col=k.split(':')
			color=col[1]
			if color in colors:
				print(colors[color],end='')
			del info[info.index(k)]
		if '<DELAY>' == k:
			delay=True
			info.remove('<DELAY>')
		else:
			delay=False
		if '<$SHIFT>' == k:
			bangkey = 'and'
			andkey = 'or'
			orkey = 'not'
			info.remove('<$SHIFT>')
		elif '<$EXCLAMATION>' == k:
			bangkey = 'UH OH!'
			andkey = 'AND...'
			orkey = 'OR?!'
			info.remove('<$EXCLAMATION>')
		elif '<$KEYS' in k:
			key=k.split(':')
			bangkey=keys[1]
			andkey=keys[2]
			orkey=keys[3]
			del info[info.index(key)]
		else:
			bangkey='not'
			andkey='and'
			orkey='or'
		if '<SEPARATOR' in k:
			se=k.split(':')
			bkey=se[1]
			del info[info.index(se)]
		else:
			bkey='/'
		if '<C' in k:
			comment=k.split(':')
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
			del info[info.index(k)]
		if '<LINK' in k:
			lkey=info.index(k)
			def com(arg):
				os.system('echo \"'+arg+'\" > .tmp_btxt && python3 \"$(cat ~/.btxt_locale)\"')
			finfo=[]
			for oofy in info:
				finfo.append(oofy)
			comm=True
			info.remove(k)
		else:
			comm=False
		if '<COMMAND' in k:
			cm=k.split(':')
			os.system(cm[1])
			info.remove(k)
		if '<OUTPUT' in k:
			ouu=k.split(':')
			info.remove(k)
			ofile=ouu[1]
			fo = '\n'.join(info)
			os.system('echo \"'+fo+'\" >> '+ofile)
		else:
				output = False
		if '<SHOW>' == k:
			print('---------TEXT:--------')
			info.remove('<SHOW>')
			print(info)
			print('----------------------')
if identt == False:
	print("No BTXT identifier found in file.")
	exit()
for line in info:
	line=line.split(',')
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
	com(finfo[lkey])

