

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
    Y = int(input())
except ValueError:
    print("無効な数です。")


def yourwin():
    if Y == 1:
        E = 2
    elif Y == 2:
        E = 3
    elif Y == 3:
        E = 1

def yourlose():
    if Y == 1:
        E = 3
    elif Y == 2:
        E = 1
    elif Y == 3:
        E = 2

def yourdraw():
    E = Y

def random():
    print()
    
def pon():
    if Y == 1:
        if E == 1:
            print(
                "",
                "",
                "",
                sep="\n"
            )
        elif E == 2:
            print(
                
                
            )
        elif E == 3:
            print(
                
                
            )
        else:
            print("例外")
    elif Y == 2:
        if E == 1:
            print(
                
                
            )
        elif E == 2:
            print(
                
                
            )
        elif E == 3:
            print(
                
                
            )
        else:
            print("例外")
    elif Y == 2:
        if E == 1:
            print(
                
                
            )
        elif E == 2:
            print(
                
                
            )
        elif E == 3:
            print(
                
                
            )
        else:
            print("例外")
    else:
        print("例外")

if __name__ == "__main__":
    yourwin()
    #yourlose()
    #yourdraw()
    #random()