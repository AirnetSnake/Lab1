# -*- encoding: utf-8 -*-
#
#—делал только до 4,т.к. смысл и так пон€тен
def zgen():
	n = raw_input('Enter number 1-4: ')
	if n is not int:
		print('Bad input')
		return false
	nums={1:'    *\n    *\n    *\n    *\n    *\n    *\n   ***\n',
		2:' \n  ***\n     *\n     *\n    *\n   *\n  ****\n ',
		3:'\n  ****\n     *\n    *\n     *\n  *  *\n   **\n ',
		4:'     *\n    **\n   * *\n  *  *\n  ****\n     *\n     *\n     *')
	print nums[n]
	