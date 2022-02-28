#CalPiV2.py
from random import random
from time import perf_counter
DARTS = 10000*10000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x,y = random(),random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
end = perf_counter()
Pi = 4 * (hits/DARTS)
print("圆周率的值为:{}".format(Pi))
print("循环运行时间为:{:.5f}s".format(end - start))
