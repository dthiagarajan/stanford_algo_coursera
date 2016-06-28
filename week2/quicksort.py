def partition_first(a,l,r):
	p = a[l]
	i = l+1
	for j in range(l+1,r):
		if a[j] < p:
			a[i],a[j] = a[j],a[i]
			i += 1
	return i-1
def quicksort_first(a,l,r):
	if (r - l) <= 1:
		return 0
	else:
		k = partition_first(a,l,r)
		a[l],a[k] = a[k],a[l]
		c1 = (quicksort_first(a,l,k))
		c2 = (quicksort_first(a,k+1,r))
		return (r-l-1) +  c1 + c2 

def partition_last(a,l,r):
	a[l],a[r-1] = a[r-1],a[l]
	return partition_first(a,l,r)
def quicksort_last(a,l,r):
	if (r - l) <= 1:
		return 0
	else:
		k = partition_last(a,l,r)
		a[l],a[k] = a[k],a[l]
		c1 = (quicksort_last(a,l,k))
		c2 = (quicksort_last(a,k+1,r))
		return (r-l-1) +  c1 + c2 

def partition_med(a,l,r):
	mid = 0
	if (r-l % 2 == 0):
		mid = (r-l)/2
	else:
		mid = (r-l)/2 + 1
	m = [a[l], a[mid], a[r-1]]
	m.sort()
	if (a[l] == m[1]):
		return partition_first(a,l,r)
	elif (a[mid] == m[1]):
		a[mid],a[l] = a[l],a[mid]
		return partition_first(a,l,r)
	else:
		a[r-1],a[l] = a[l],a[r-1]
		return partition_first(a,l,r)

def quicksort_med(a,l,r):
	if (r - l) <= 1:
		return 0
	else:
		k = partition_med(a,l,r)
		a[l],a[k] = a[k],a[l]
		c1 = (quicksort_med(a,l,k))
		c2 = (quicksort_med(a,k+1,r))
		return (r-l-1) +  c1 + c2 	

with open("QuickSort.txt","r") as f:
	a = [int(l.strip()) for l in f.readlines()]
print quicksort_first(a,0,len(a))
with open("QuickSort.txt","r") as f:
	a = [int(l.strip()) for l in f.readlines()]
print quicksort_last(a,0,len(a))
with open("QuickSort.txt","r") as f:
	a = [int(l.strip()) for l in f.readlines()]
print quicksort_med(a,0,len(a))


