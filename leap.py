def leap():
	x=raw_input('Enter any year ')
	if x is not int:
		print('Bad input')
		return false
	if (x%4 is not 0) or (x%4==0 and x%100==0 and x%400 is not 0) 
		result=" not vis"
	else:
		result="vis"
	print(result)

