def TI_to_Espacenet(string):
	code1 = string[0:4]
	code2 = string[4:8]
	rest = string[8:]

	code2 = code2.lstrip('0')

	return code1 + ' ' + code2 + '/' + rest



string = "H02K004103"
print string
print TI_to_Espacenet(string)