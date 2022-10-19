def recursive_pow(x, n):
	if n == 0:
		return 1
	if n > 0:
		return x*recursive_pow(x, n-1)
