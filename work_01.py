import random

r = random.randint(1,100)
# print(r)
p = "failure,onemore!"
print("1~100の中から正解を当てろ")
if r < 50:
    print("50未満だ")
else:
    print("50以上だ")
for i in range(5):
    w = int(input())
    print(f"君の答えは{w}だ")
    if w == r:
        print("success!やるねぇ")
        break
    else:
        print("failure,onemore!")
        if w < r:
            print(f"答えは{w}より大きいぞ、もっと大きく!")
        else:
            print(f"答えは{w}より小さいみたいだぞ？")

if w == r:
    pass
else:
    print("continuation? yes?/no?")
    w = input()
    if w =="yes":
        print("1~100の中から正解を当てろ")
    if r < 50:
       print("50未満だ")
    else:
       print("50以上だ")
for i in range(5):
    w = int(input())
    print(f"君の答えは{w}だ")
    if w == r:
        print("success!やるねぇ")
        break
    else:
        print("failure,onemore!")
        if w < r:
            print(f"答えは{w}より大きいぞ、もっと大きく!")
        else:
            print(f"答えは{w}より小さいみたいだぞ？")
else:
    print("see you next game")
print(f"ちな、答えは{r}だったぞ。")