import questionary, random

npc_list = ["npc1", "npc2", "npc3", "npc4", "npc5", "cancel"]

while True:
    npc = questionary.select(
        "対戦NPC数を決定してください。", choices=npc_list
    ).ask()

    if (npc == "cancel") or (npc == None):
        print("キャンセルされました")
        break
    
    while True:
        npc_str = npc - "npc"
        npc_int = int(npc_str)
        A = 
        B = 
        C = 
        
        npc1 = random.randrange(A, (B+1)-C)
        npc2 = 
        npc3 = 
        npc4 = 
        npc5 = 