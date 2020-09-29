import time

def fib(n):
	if n in [1,2]:
		return 1
	return fib(n-1)+fib(n-2)	

start = time.time()
result = fib(40)
end = time.time()
print(f"斐波那契数列的第40项是:{result},耗时:{end-start}秒")	