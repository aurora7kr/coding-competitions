# input
S = list(input())

# count
na = S.count('a')
nb = S.count('b')
nc = S.count('c')

mx = max(na, nb, nc)
if mx == na:
	print('a')
elif mx == nb:
	print('b')
elif mx == nc:
	print('c')
