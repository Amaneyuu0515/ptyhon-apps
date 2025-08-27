import random


while True:
    # ランダムな数字を生成

    a = random.randint(1, 100)  # 1から100のランダムな整数を生成
    print(a)

    result = False  # ゲームの結果を格納する変数
    c = 0
    for i in range(5):
        c = c + 1
        input_line = int(input("1から100の数字を入力してください: "))
        if input_line == a:
            print("正解")
            result = True
            break
        else:
            print("不正解")
            if input_line < a:
                if a - input_line > 10:
                    print("10以上大きい")
                else:
                    print("もっと大きい数字ですが、かなり近いです")
            else:
                if input_line - a > 10:
                    print("10以上小さいです")
                else:
                    print("もっと小さい数字ですが、かなり近いです")

    if result:
        print(f"ゲームに勝ちました！ あなたは{c}回目で正解しました。")
    else:
        print(f"ゲームに負けました。正解は{a}でした。")

    ans = input("もう一度やる？(yes/no): ")
    if ans != "yes":
        print("seeyounextgame!")
        break
