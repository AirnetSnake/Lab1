def leap(x):
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
	return result

