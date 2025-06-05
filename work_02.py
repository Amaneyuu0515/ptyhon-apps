import time
import random

print("刹那の見切り!! 合図が出たらenterを押せ!")

s = random.uniform(5,15)
time.sleep(s)
print("!!")
start = time.time()
e = input()
end = time.time()
time_diff = end - start
time_diff = "{:.4}".format(time_diff)
if time_diff < 0.01:
   print("不正を検知しました。記録は無効化されます")
else:
   print(f"反応速度{time_diff}秒")