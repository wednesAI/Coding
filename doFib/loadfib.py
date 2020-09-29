import ctypes
import time	

so = ctypes.cdll.LoadLibrary('./_fib.so')
fib = so.Fib

start = time.time()
result = fib(40)
end = time.time()
print(f"斐波那契列数列第40项：{result},耗时：{end - start}")
