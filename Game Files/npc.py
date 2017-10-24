import items



hospital_receptionist = {
    "id": "nurse",
    "name": "A nurse is at the reception desk",
    "dialogue": {
        "a": ["Hi do u wanna have some tea", "NPC response A.", [items.victim_belongings]],
        "b": ["do u wanna f**k?", "NPC response B.",
        
            {"a": ["option a2", "NPC response a2.", "end_convo"],
            "b": ["option b2", "NPC response b2.", 
                {"a": ["option a3", "NPC response a3.", "end_convo"],
                "b": ["option b3", "NPC response b3.", ""],
                "c": ["option c3", "NPC response c3.", "end_convo"]}],
            "c": ["option c2", "NPC response c2.", "end_convo"]}],
        
        "c": ["bye.", "NPC response C.", "end_convo"]
    }
}

joe_branson = {
    "id": "joe",
    "name": "Joe Branson",
    "dialogue": {
        "a": ["A: Hey buddy, how you doin'?", "...", "end_convo"],
        "b": ["B: Does it hurt anywhere?", "...", "end_convo"],
        "c": ["C: Bye.", "...", "end_convo"]
    }
}


"""
FORMAT BELOW
----------------------------------------------------------
change_me = {
    "id": "EMPTY",
    "name": "EMPTY",
    "dialogue": {
        "a": ["A: OPTION", "NPC RESPONCE", "end_convo"],
        "b": ["B: OPTION", "NPC RESPONCE", "end_convo"],
        "c": ["C: OPTION", "NPC RESPONCE", "end_convo"]
    }
}"""

"""npcs = {
    "nurse": hospital_receptionist,
    "receptionist": hospital_receptionist,
    "joe":
}"""