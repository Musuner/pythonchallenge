str = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
i=0
for c in str:
	if ord(c) == 32:
		print(' ')
	if ord(c) == 121:
		print('a',end='')
	if ord(c) == 122:
		print('b',end='')
	#print (ord(str[i]),end='')
	print(chr(ord(str[i])+2),end='  ')
	i+=1
print('.')
print(ord('z'))
print(ord(' '))
print(ord('y'))



