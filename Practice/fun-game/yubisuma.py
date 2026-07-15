import questionary, random, time

npc_list = ["cancel", "npc1", "npc2", "npc3", "npc4", "npc5"]

exit = 0
Start = 0
user_hands = 2
Npc1_hands = 2
Npc2_hands = 2
Npc3_hands = 2
Npc4_hands = 2
Npc5_hands = 2

while True:
    npc = questionary.select(
        "対戦NPC数を決定してください。", choices=npc_list
    ).ask()

    if (npc == "cancel") or (npc == None):
        print("キャンセルされました")
        break
    else:
        Start = 1
    
    while True:
        npc_str = npc.removeprefix("npc")
        A = ((int(npc_str) * 2) + 2)
        #B = "random.randrange(0, (A+1)-B)を使うようにしたい"
        total_hand = 0
        
        for i in range(int(npc_str)+1):
            if i == 0:
                time.sleep(0.5)
                print(
                    "あなたのターンです。"
                )
                user = int(input())
            else:
                time.sleep(0.5)
                print(
                    npc_list[i] + "のターンです。"
                )
                
            NpcT1 = NpcT2 = NpcT3 = NpcT4 = NpcT5 = random.randrange(0, (A+1))
            NpcHand1 = random.randrange(0, (Npc1_hands+1))
            NpcHand2 = random.randrange(0, (Npc2_hands+1))
            NpcHand3 = random.randrange(0, (Npc3_hands+1))
            NpcHand4 = random.randrange(0, (Npc4_hands+1))
            NpcHand5 = random.randrange(0, (Npc5_hands+1))
            time.sleep(1.5)
            
            print(
            )
            if total_hand == user:
                user_hands -= 1
