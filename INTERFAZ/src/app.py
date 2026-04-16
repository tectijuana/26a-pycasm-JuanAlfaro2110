import ctypes
import time

lib = ctypes.CDLL("./build/libops.so")

lib.add.argtypes = [ctypes.c_long, ctypes.c_long]
lib.add.restype = ctypes.c_long

print("ASM ADD:", lib.add(10, 20))

# Benchmark
def bench():
    start = time.time()
    for _ in range(10_000_000):
        lib.add(1,2)
    end = time.time()
    print("ASM:", end - start)

bench()