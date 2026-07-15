import questionary, random

npc_list = ["cancel", "npc1", "npc2", "npc3", "npc4", "npc5"]

while True:
    npc = questionary.select(
        "対戦NPC数を決定してください。", choices=npc_list
    ).ask()

    if (npc == "cancel") or (npc == None):
        print("キャンセルされました")
        break
    
    while True:
        npc_str = npc.removeprefix("npc")
        A = ((int(npc_str) * 2) + 2)
        #B = "random.randrange(0, (A+1)-B)を使うようにしたい"
        C = 0
        
        npc1 = npc2 = npc3 = npc4 = npc5 = random.randrange(0, (A+1))
        
        