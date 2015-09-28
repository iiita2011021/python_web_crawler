def extract_code(pat_num):
	cc = pat_num[0:2] #first two chars
	if pat_num[-2].isdigit():
		kc = pat_num[-1]
	else:
		kc = pat_num[-2] + pat_num[-1]

	return cc, kc #country code and kind code


pat_number = 'CA2386633C'
print extract_code(pat_number)

pat_number = 'WO2007134039A3'

print extract_code(pat_number)