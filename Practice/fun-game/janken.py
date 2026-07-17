import random, time

# 代入
E = 0
won = 0
lose = 0
draw = 0

while True:
    print(
        "japanese janken - python script",
        "以下の出し手から選択してください",
        "`グー` or `gu`",
        "`チョキ` or `tyoki`",
        "`パー` or `pa`",
        sep="\n"
    )

    # input
    try:
        Y = str(input("Enter `None` or `exit` to exit >"))

    # 終了対応のif文
    except ValueError:
        print("終了します。")
        break

    if Y == "exit":
        print("終了します。")
        break

    # 変換
    match Y:
        case "gu":
            Y = "グー"
        case "tyoki":
            Y = "チョキ"
        case "pa":
            Y = "パー"
        case _:
            print("正確な文字を入力してください")
            continue

    # randomでのenemyの出し手を作成
    E = random.choice(["グー", "チョキ", "パー"])
    
    # 判定

    # 引き分け判定
    if E == Y:
        print("== draw ==")
        draw += 1
        H = "draw"
    else:
        match Y:
            # 勝ち判定 パイプを使用すると例外に通されるのでこうする
            case "グー" if E == "チョキ":
                print("== Your won ==")
                won += 1
                H = "won"
            case "チョキ" if E == "パー":
                print("== Your won ==")
                won += 1
                H = "won"
            case "パー" if E == "グー":
                print("== Your won ==")
                won += 1
                H = "won"
            
            # 負け判定 パイプを使用すると例外に通されるのでこうする
            case "グー" if E == "パー":
                print("== Enemy won ==")
                lose += 1
                H = "lose"
            case "チョキ" if E == "グー":
                print("== Enemy won ==")
                lose += 1
                H = "lose"
            case "パー" if E == "チョキ":
                print("== Enemy won ==")
                lose += 1
                H = "lose"

            # 例外
            case _:
                print("Exception Occurrence")
                continue
    
    print(
        " Your  - ", Y, "\n",
        " Enemy - ", E, "\n",
        "\n",
        "== Your match history ==", "\n",
        " won   - ", won, "\n",
        " lose  - ", lose, "\n",
        " draw  - ", draw, "\n",
        sep=""
    )
    time.sleep(1.5)
