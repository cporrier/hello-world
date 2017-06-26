# -* - coding : utf -8 -* -
# Merge sort algorithm
# Auteur : Carole Porrier
# Date : 27 octobre 2016
# Python 3

def merge(A,B):
	n = len(A) + len(B)
	i = 0
	j = 0
	C = list()
	for k in range(n):
		if i < len(A) and (j >= len(B) or A[i] < B[j]): 
			C.append(A[i])
			i = i + 1
		else :
			C.append(B[j])
			j = j + 1
	return C

def tri(T):
	n = len(T)
	if n <= 1 : return T
	elif n == 2 : return (min(T),max(T))
	else :
		m = int(n/2)
		A = tri(T[:m])
		B = tri(T[m:n])
		return merge(A,B)

T = [8, 6, 14, 67, 3, 9, 0, -5]
print(tri(T))
