import tkinter as tk


class ChatGame:
    def __init__(self, root):
        self.root = root
        self.root.title("選択式チャットゲーム")
        self.text_area = tk.Text(root, width=80, height=25, wrap="word")
        self.text_area.pack(padx=10, pady=10)
        self.text_area.config(state="disabled")

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.script_queue = []

        self.main()

    # ===== テキスト表示 =====
    def add_text(self, text):
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, f"{text}\n")
        self.text_area.see(tk.END)
        self.text_area.config(state="disabled")

    # ===== ボタン管理 =====
    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def add_next_button(self, func=None):
        self.clear_buttons()
        btn = tk.Button(
            self.button_frame, text="▶︎次へ", command=lambda:
            self.next_line(func)
        )
        btn.pack()

    def add_choice_buttons(self, options, func_list):
        self.clear_buttons()
        for idx, option in enumerate(options):
            btn = tk.Button(
                self.button_frame,
                text=option,
                command=lambda i=idx: self.choice_selected(i, func_list),
            )
            btn.pack(side="left", padx=5)

    # ===== script_queueを処理 =====
    def next_line(self, after_func=None):
        if after_func:
            after_func()
            return

        if not self.script_queue:
            self.add_text("=== END ===")
            self.clear_buttons()
            return

        line = self.script_queue.pop(0)

        if isinstance(line, str):
            self.add_text(line)
            self.add_next_button()
        elif isinstance(line, list) and len(line) == 2:
            # [選択肢リスト, 対応関数リスト]
            options, funcs = line
            self.add_choice_buttons(options, funcs)
        else:
            print("script_queueの形式エラー:", line)

    # ===== 選択肢処理 =====
    def choice_selected(self, idx, func_list):
        if idx < len(func_list):
            func_list[idx]()
        else:
            print("選択肢のインデックスが範囲外です:", idx)

    # ===== ゲーム章（オリジナルセリフ） =====
    def main(self):
        self.script_queue = [
            "👤 とある王国、あなたはその王国の一般人だった。",
            "👤 ある日、王様から城へと呼び出された。",
            "👤 王様「よくぞ来てくれた、勇者の資格を持つものよ。」",
            "👤 王様「お主はこの世界を救う旅に出る覚悟はあるか？」",
            [["はい", "いいえ"], [self.main_choice_yes, self.main_choice_no]],
        ]
        self.next_line()

    def main_choice_yes(self):
        self.script_queue = [
            "👤 あなた「、、、よくわかりませんが、わかりました。」",
            "👤 王様「素晴らしい…その勇気、しかと見届けた。」",
            "👤 王様「では、まずは北の森へ向かうがよい。」",
            "👤 王様から剣と盾を受け取り、あなたは旅立つことになった。",
        ]
        self.add_next_button(self.chapter2)

    def main_choice_no(self):
        self.script_queue = [
            "👤 あなた「、、、嫌です、俺は争いが嫌いな一般人なので。」",
            "👤 王様「……そうか。勇なき者に未来はない。」",
            "👤 王様「ここで終わりだ。衛兵よ、此奴を捕らえよ！」",
            "👤 あなたは王へ反逆したとされ処刑されてしまった。",
        ]
        self.add_next_button(self.bad_ending)

    # ===== 章2 =====
    def chapter2(self):
        self.script_queue = [
            "👤 あなたは北の森の入り口にたどり着いた。",
            "👤 森は暗く静かで、どこか不気味な雰囲気が漂っている。",
            "👤 森を歩いていると、笛の演奏が聞こえてくる...",
            "👤 あなた「、、、誰かいるのか？」",
            "👤 そこにいたのはエルフの少女だった",
            "👤 エルフの少女「あなたは誰？この森になんのよう？」",
            "👤 あなた「、、、一応勇者らしいんだけど、、めんどくさい人（王様）に言われてここまできただけだよ。」",
            "👤 エルフの少女「そうなんだ。私はこの森の盟主、リリアンヌよ」",
            "👤 リリアンヌ「この森は魔物が多くて危険だから、私が案内しましょうか？」",
            [
                ["彼女の話を素直に聞く", "無視して進む"],
                [self.chapter2_follow, self.chapter2_ignore],
            ],
        ]
        self.next_line()

    def chapter2_follow(self):
        self.script_queue = [
            "👤 あなた「、、、ありがとう。助かるよ。」",
            "👤 リリアンヌ「わかった、私についてきて。」",
            "👤 あなたは少女と共に森へ踏み出した。",
            "👤 深い霧の中、魔物の気配が近づいてくる――。",
        ]
        self.add_next_button(self.chapter3_with_girl)

    def chapter2_ignore(self):
        self.script_queue = [
            "👤 あなた「、、、別に案内なんていらないよ。」",
            "👤 リリアンヌ「そう、でも、気をつけて」",
            "👤 あなたは少女を無視して森に入った。",
            "👤 足元に気を取られていると、突然背後から何かが襲いかかってきた――！",
            "👤 あなた「！！」",
            "👤 魔物『ガアアア……！』",
        ]
        self.add_next_button(self.bad_ending)

    # ===== 章3以降（リリアンヌと魔王） =====
    def chapter3_with_girl(self):
        self.script_queue = [
            "👤 あなたとリリアンヌは森の奥へと進んでいった。",
            "👤 リリアンヌ「この森には魔物がたくさんいるの。」",
            "👤 リリアンヌ「でも、私の魔法で守ってあげるから安心して。」",
            [["逃げる", "攻撃する"], [self.chapter3_escape, self.chapter3_attack]],
        ]
        self.next_line()

    def chapter3_escape(self):
        self.script_queue = [
            "👤 あなた「、、、戦いたくないし、逃げよう」",
            "👤 あなたとリリアンヌは魔物を避けて森を進んでいく。",
            "👤 あなたたちは無事に森を抜けることができた。",
        ]
        self.add_next_button(self.chapter4)

    def chapter3_attack(self):
        self.script_queue = [
            "👤 あなた「、、、自分でやるから、下がってて。」",
            "👤 少女は魔法でなんとか魔物を退けたが、あなたの受けた傷は致命傷となってしまった。",
        ]
        self.add_next_button(self.bad_ending)

    def chapter4(self):
        self.script_queue = [
            "👤 あなたとリリアンヌは森を抜け、広い平原に出た。",
            [["休む", "すぐに進む"], [self.chapter4_rest, self.chapter4_go]],
        ]
        self.next_line()

    def chapter4_rest(self):
        self.script_queue = [
            "👤 あなたはリリアンヌの提案を受け入れ、少し休むことにした。",
            "👤 あなたはリリアンヌと共に草むらで休息を取った。",
            "👤 準備ができたら、魔王の城へ向かうことにした。",
        ]
        self.add_next_button(self.chapter5)

    def chapter4_go(self):
        self.script_queue = [
            "👤 あなたはすぐに進むことを決意した。",
            "👤 疲れが溜まっていた所に魔物が現れた。",
            "👤 あなたは疲れ切っていて、まともに戦うことができなかった。",
        ]
        self.add_next_button(self.bad_ending)

    def chapter5(self):
        self.script_queue = [
            "👤 あなたとリリアンヌは苦難の末魔王の城へと向かった。",
            [["魔物と戦う", "話し合う"], [self.chapter5_fight, self.chapter5_talk]],
        ]
        self.next_line()

    def chapter5_fight(self):
        self.script_queue = [
            "👤 あなたとリリアンヌは魔物たちと激しい戦闘を繰り広げた。",
            "👤 ついに、魔王が姿を現した。",
            "👤 魔王「人間ども、よくも、、」",
            "👤 あなた「魔王、、やるしかないのか、、」",
        ]
        self.add_next_button(self.normal_ending)

    def chapter5_talk(self):
        self.script_queue = [
            "👤 あなた「、、、やっぱり、戦うの好きじゃないや、俺、、」",
            "👤 魔王「、、、そうか、ならば、我と共にくるが良い、」",
        ]
        self.add_next_button(self.good_ending)

    # ===== エンディング =====
    def good_ending(self):
        self.script_queue = [
            "🌟【エンディング：理想のセカイ】",
            "👤 あなたとリリアンヌは魔王と共に新しい世界を築く。",
        ]
        self.add_next_button()

    def normal_ending(self):
        self.script_queue = [
            "🌙【エンディング：平和な日常...?】",
            "👤 王様「よくぞ魔王を倒してくれた！お主はこの世界の英雄じゃ！」",
        ]
        self.add_next_button()

    def bad_ending(self):
        self.script_queue = [
            "💀【エンディング：世界の崩壊】",
            "👤 魔王「人間どもを皆殺しにしろ！我らの国を守るために！」",
            "👤 勇者を失った世界は魔物に全てを滅ぼされた。",
        ]
        self.add_next_button()


if __name__ == "__main__":
    root = tk.Tk()
    game = ChatGame(root)
    root.mainloop()
