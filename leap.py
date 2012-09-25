def leap():
	x=raw_input('Enter any year ')
	if x is not int:
		print('Bad input')
		return false
	if x%4==0:
		if x%100==0:
			if x%400==0:
				result="vis"
			else:
				result="not vis"
		else:
			result="vis"
	else
		result="not vis"
	print(result)

