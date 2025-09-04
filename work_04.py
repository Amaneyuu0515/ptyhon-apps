import time
import random
import mysql.connector
from datetime import datetime

# ランダムな待ち時間
b = random.randint(3, 5)
time.sleep(b)

# 合図が出た時刻
s = time.time()
print("刹那の見切り!! 合図が出たらenterを押せ!")
print("!!!!!")

# プレイヤーの入力を待つ
input("▶︎ 押せ！")

# 押した時刻
e = time.time()

# 結果表示
print(f"開始時:{s}秒")
print(f"終了:{e}秒")

k = e - s
print(f"かかった時間 {k:.4f} 秒")

if k < 0.01:
    print("歪")
print("押された")

# プレイヤー名入力
name = input("名前を入力してください: ")

# DBに接続
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="amaneyuu0515",
    database="work04",
    autocommit=True,   # ← 追加
    connection_timeout=60
)
cursor = conn.cursor()

# データを挿入
sql = "INSERT INTO record (name, record_time, started_at) VALUES (%s, %s, %s)"
values = (name, datetime.fromtimestamp(e), datetime.fromtimestamp(s))
cursor.execute(sql, values)
print(cursor.rowcount, "件追加されました")

cursor.close()
conn.close()   # ← いったん閉じる

# ===== ランキング表示 =====
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="amaneyuu0515",
    database="work04",
    autocommit=True,
    connection_timeout=60
)
cursor = conn.cursor()

print("\n=== ランキング (TOP10) ===")
sql = """
SELECT
    name,
    record_time,
    started_at,
    TIMESTAMPDIFF(MICROSECOND, started_at, record_time) / 1000000.0 AS
    reaction_time
FROM record
ORDER BY reaction_time ASC
LIMIT 10
"""
cursor.execute(sql)

for i, row in enumerate(cursor.fetchall(), start=1):
    name, record_time, started_at, reaction_time = row
    print(f"{i}位: {name} さん - 反応時間 {reaction_time:.4f} 秒")

cursor.close()
conn.close()
