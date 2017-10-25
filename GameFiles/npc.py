import dialogues

#- - - - - - - - - - - - -  POLICE STATION - - - - - - - - - - - |

chief_kirill = {
    "id": "chief",
    "name": "Chief Kirill is",
    "dialogue": dialogues.d_chief_kirill_1
}

#- - - - - - - - - - - - -  HOSPITAL - - - - - - - - - - - - - - |


hospital_receptionist = {
    "id": "nurse",
    "name": "A nurse sitting at the reception desk is",
    "dialogue": dialogues.d_hospital_receptionist_1 #replace me
    
}

joe_branson = {
    "id": "joe",
    "name": "Joe Branson is",
    "dialogue": {
        "a": ["Hey buddy, how you doin'?", "...", "end_convo"],
        "b": ["Does it hurt anywhere?", "...", "end_convo"],
        "c": ["Bye.", "...", "end_convo"]
    }
}

doctor_kim = {
	"id": "doctor",
	"name": "Dr. Kim is",
	"dialogue": dialogues.d_doctor_kim_1
}

killer = {
	"id": "killer",
	"name": "The Killer is",
	"dialogue": None #replace me
}
#- - - - - - - - - - - - -  SHIPPING COMPANY - - - - - - - - - - - - - - |

shipping_ceo = {
	"id": "ceo",
	"name": "the Shipping CEO is",
	"dialogue": None	 #replace me
}

#- - - - - - - - - - - - -  JOE'S HOUSE - - - - - - - - - - - - - - |

joe_wife = {
	"id": "mrs branson",
	"name": "Mrs Branson is",
	"dialogue": None #replace me
}
"""Kirill

Doctor
Joe
Receptionist
Killer

Shipping Company CEO

Wife
"""

def get_npc():
    return {"joe_wife": joe_wife,
    "shipping_ceo": shipping_ceo,
    "killer": killer,
    "doctor_kim": doctor_kim,
    "joe_branson": joe_branson,
    "hospital_receptionist": hospital_receptionist,
    "chief_kirill": chief_kirill}

def restore_npc(arr):
    joe_wife = arr["joe_wife"]
    shipping_ceo = arr["shipping_ceo"]
    killer = arr["killer"]
    doctor_kim = arr["doctor_kim"]
    joe_branson = arr["joe_branson"]
    hospital_receptionist = arr["hospital_receptionist"]
    chief_kirill = arr["chief_kirill"]

npc_dict = {
    "mrs branson": joe_wife,
    "ceo": shipping_ceo,
    "killer": killer,
    "doctor": doctor_kim,
    "joe": joe_branson,
    "nurse": hospital_receptionist,
    "chief": chief_kirill
}