import questionary

npc_list = ["npc1", "npc2", "npc3", "npc4", "npc5", "cancel"]

while True:
    npc = questionary.select(
        "対戦NPC数を決定してください。", choices=npc_list
    ).ask()

    if npc == "cancel":
        print("キャンセルされました")
        break