import questionary, random, time

npc_list = ["cancel", "npc1", "npc2", "npc3", "npc4", "npc5"]

user_hands = 2
Npc_hands = ["NPC1": 2,"NPC2": 2,"NPC3": 2,"NPC4": 2,"NPC5": 2]

while True:
    select = questionary.select(
        "対戦NPC数を決定してください。", choices=npc_list
    ).ask()

    if (select == "cancel") or (select == None):
        print("キャンセルされました")
        break
    
    while True:
        npc_str = select.removeprefix("npc")

        A = ((int(npc_str) * 2) + 2)
        #B = "random.randrange(0, (A+1)-B)を使うようにしたい"
        total_hand = 0
        
        for i in range(int(npc_str)+1):
            if i == 0:
                time.sleep(0.5)
                print(
                    "あなたのターンです。",
                    "数を指定して"
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
