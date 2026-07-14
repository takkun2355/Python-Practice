while True:
    print(
        "japanise janken - python script",
        "Select a number from the options below",
        "1 - gu",
        "2 - tyoki",
        "3 - pa",
        sep="\n"
    )

    E = 0
    Y = 0

    try:
        Y = int(input("Enter 3817 to exit >"))
    except ValueError:
        print("無効な数です。\n")
        continue
        
    if Y == 3817:
        break
    
    def pon():
        if Y == E:
            print("== draw ==")
            draw += 1
            H = "draw"
        if Y == 1 and E == 2 or Y == 2 and E == 3 or Y == 3 and E == 1:
            print("== Your won ==")
            won += 1
            H = "won"
        else:
            print("== Enemy won ==")
            lose += 1
            H = "lose"
            
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
            "Your  -", Y, "\n",
            "Enemy -", E, "\n",
            "\n",
            "== Your match history ==",
            "won   -", won, "\n",
            "lose  -", lose, "\n",
            "draw  -", draw, "\n",
            sep=" "
        )

    def yourwon():
        if Y == 1:
            E = 2
        elif Y == 2:
            E = 3
        elif Y == 3:
            E = 1
        pon()

    def yourlose():
        if Y == 1:
            E = 3
        elif Y == 2:
            E = 1
        elif Y == 3:
            E = 2
        pon()

    def yourdraw():
        E = Y
        pon()

    def random():
        print()
        pon()

    if __name__ == "__main__":
        yourwon()
        #yourlose()
        #yourdraw()
        #random()
