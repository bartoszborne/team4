import items
import dialogues

#- - - - - - - - - - - - -  POLICE STATION - - - - - - - - - - - |

chief_kirill = {
    "id": "chief",
    "name": "Chief Kirill is",
    "dialogue": dialogues.d_chief_kirill_1,    
}




hospital_receptionist = {
    "id": "nurse",
    "name": "A nurse is at the reception desk",
    "dialogue": {
        "a": ["Hi do u wanna have some tea", "NPC response A.", [items.victim_belongings]],
        "b": ["do u wanna f**k?", "NPC response B.",
        
            {"a": ["optiona 2", "NPC response a2.", "end_convo"],
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


"""Kirill

Doctor
Joe
Receptionist
Killer

Shipping Company CEO

Wife
"""