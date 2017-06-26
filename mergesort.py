# -* - coding : utf -8 -* -
# Merge sort algorithm
# Auteur : Carole Porrier
# Date : 27 octobre 2016
# Python 3

def merge(A,B):
	"""
	Fonction qui prend en entrée deux listes A et B déjà triées et qui les fusionne en une seule liste triée
	"""
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
	"""
	Fonction récursive permettant de trier une liste T, en utilisant la fonction merge
	"""
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
