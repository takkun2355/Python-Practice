try:
    Y = int(input())
except ValueError:
    print("無効な数です。")

print(
    "japanise janken - python script",
    "Select a number from the options below",
    "1 - gu",
    "2 - tyoki",
    "3 - pa",
    sep="\n"
)

def yourwin():
    if Y == 1:
        E = 2
    elif Y == 2:
        E = 3
    elif Y == 3:
        E = 1

def yourlose():
    print()

def yourdraw():
    print()

def random():
    print()
    
def pon():
    if Y == 1:
        if E == 1:
            
        elif E == 2:
            
        elif E == 3:
            
    elif Y == 2:
        if E == 1:
            
        elif E == 2:
            
        elif E == 3:
            
    elif Y == 2:
        if E == 1:
            
        elif E == 2:
            
        elif E == 3:
            
    else:
        print("例外")

if __name__ == "__main__":
    yourwin()
    #yourlose()
    #yourdraw()
    #random()