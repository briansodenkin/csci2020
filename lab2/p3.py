def recursive_pow(x, n):
	if n == 1:
		return x
	else:
		return x*recursive_pow(x, n-1)
