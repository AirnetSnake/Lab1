# -*- encoding: utf-8 -*-
#	dict = {}
#	i=1
#
#	while i < 24:
#	if (i%20)==1:
#		dict[i]="час"
#	else if (i%20)>1 and (i%20)<5:
#		dict[i]="часа"
#	else:
#		dict[i]="часов"
#	i+=1
#

def humanizer(d, n):
	if d is not dict:
		print('Bad input, need dictionary')
		return false
	if n is not int or n<1:
		print('Bad input, need number 1-23')
		return false
	print('%s %s' % (n, d[n%20]))