def merge(a1,a2):
	i = 0
	j = 0
	count = 0
	while (i < len(a1) and j < len(a2)):
		if (a1[i] <= a2[j]):
			i += 1
		else:
			j += 1
			count += len(a1) - i
	return count

def count(a):
	if (len(a) == 0 or len(a) == 1):
		return 0
	else:
		mid = len(a)/2
		return  count(a[0:mid]) + count(a[mid:]) + merge(a[0:mid],a[mid:])

import sys
fil = sys.argv[1]

nums = []
with open(fil,'r') as f:
	for a in f.readlines():
		nums.append(int(a.strip()))

result = count(nums)
print result