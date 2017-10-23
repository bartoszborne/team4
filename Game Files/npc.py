import items



hospital_receptionist = {
    "name": "A hospital receptionist",
    "dialogue": {
        "a": ["A: Hi do u wanna have some tea", "NPC response A.", [items.victim_belongings]],
        "b": ["B: do u wanna f**k?", "NPC response B.",
        
        {"a": ["option a2", "NPC response a2.", "end_convo"],
        "b": ["option b2", "NPC response b2.", {"a": ["option a3", "NPC response a3.", "end_convo"],
        "b": ["option b3", "NPC response b3.", ""],
        "c": ["option c3", "NPC response c3.", "end_convo"]}],
        "c": ["option c2", "NPC response c2.", "end_convo"]}],
        
        "c": ["C: bye.", "NPC response C.", "end_convo"]
    }
}

npcs = {
	"hospitalreceptionist": hospital_receptionist
}