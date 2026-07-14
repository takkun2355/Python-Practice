import random, time

won = 0
lose = 0
draw = 0

while True:
    print(
        "japanise janken - python script",
        "Select a number from the options below",
        "1 - gu",
        "2 - tyoki",
        "3 - pa",
        sep="\n"
    )

    # 定義
    E = 0
    Y = 0

    # input
    try:
        Y = int(input("Enter 3817 to exit >"))
    except ValueError:
        print("無効な数です。\n")
        continue
        
    # 終了かどうかを調べる
    if Y == 3817:
        break
    
    # random
    E = random.randrange(1, 4)
    
    # 判定
    if 1 <= Y <= 3:
        if Y == E:
            print("== draw ==")
            draw += 1
            H = "draw"
        elif Y == 1 and E == 2 or Y == 2 and E == 3 or Y == 3 and E == 1:
            print("== Your won ==")
            won += 1
            H = "won"
        else:
            print("== Enemy won ==")
            lose += 1
            H = "lose"
    else:
        print("例外")
        continue
        
    if Y == 1:
        Y = "gu"
    elif Y == 2:
        Y = "tyoki"
    else:
        Y = "pa"
    
    if E == 3:
        E = "pa"
    elif E == 2:
        E = "tyoki"
    else:
        E = "gu"
    
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
