#Сделал только до 3, т.к. или я неправильно понял смысл задачи
def zgen():
	n = raw_input('Enter number 1-4: ')
	if n is not int:
		print('Bad input')
		return false
	nums={1:'    *\n    *\n    *\n    *\n    *\n    *\n   ***\n',
		2:' \n  ***\n     *\n     *\n    *\n   *\n  ****\n ',
		3:'\n  ****\n     *\n    *\n     *\n  *  *\n   **\n ')
		4:'     *\n    **\n   * *\n  *  *\n  ****\n     *\n     *\n     *')
	print nums[n]
	