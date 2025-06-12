
import time
import random
b = random.randint(3,5)
print(f"待ち時間: {b}秒")

time.sleep(b)

s= time.time()
print(f"開始時:{s}秒")

print("!!!!!")
input("刹那の見切り!! 合図が出たらenterを押せ!")
e = time.time()
print(f"終了:{e}秒")
k = e - s
print(f"かかった時間{k}秒")
if k < 0.01:
    print("歪")   
print("押された")