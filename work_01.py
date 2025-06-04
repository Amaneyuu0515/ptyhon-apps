import random
r = random.randint(1,100)
# print(r)
w = int(input("1~100までの数字を当てよ"))
print(f"入力された数字は{w}です。")
if r < w:
    print("50より小さいです")
else:
    ("51より大きいです")
for i in range(5):
    w = int(input())
    if w == r:
        print("success!!")
        break
    else:
        print("failure")