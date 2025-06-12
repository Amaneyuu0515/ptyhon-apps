import time
import random

print("刹那の見切り!! 合図が出たらenterを押せ!")

s = random.uniform(5,15)
time.sleep(s)
print("!!")
e = input()
start = time.time()
end = time.time()
time_diff = end - start
time_diff = "{:.4}".format(time_diff)
if time_diff < 0.01:
    print("不正検知")
    pass
else:
    print(f"反応速度{time_diff}")