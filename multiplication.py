# -* - coding : utf -8 -* -
# Karatsuba multiplication
# Auteur : Carole Porrier
# Date : 29 octobre 2016
# Python 3

def mult(x, y, n):
    """
    Fonction permettant de multiplier de très très grands nombres
    """
    if x < 10 and y < 10 : return x*y
    else :
        n = n/2
        (a, b) = divmod(x, (10**n))
        (c, d) = divmod(y, (10**n))
        p = mult(a, c, n)
        q = mult(a, d, n)
        r = mult(b, c, n)
        s = mult(b, d, n)
        res = pow(10, 2*n)*p + pow(10, n)*(q+r) + s
        return res

# exemple de multiplication avec cette fonction
print(mult(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627, 64))
