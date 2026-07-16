import random, time

# 代入
E = 0
won = 0
lose = 0
draw = 0

while True:
    print(
        "japanese janken - python script",
        "Select a number from the options below",
        "1 - gu",
        "2 - tyoki",
        "3 - pa",
        sep="\n"
    )

    # input
    Y = input("Enter 'exit' to exit >")
    if (Y == str) and (Y == "exit"):
        break
    else:
        Y = int(Y)
    
    # randomでのenemyの出し手を作成
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
        print("Exception Occurrence")
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
