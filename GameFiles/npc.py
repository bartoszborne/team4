import items
import dialogues

#- - - - - - - - - - - - -  POLICE STATION - - - - - - - - - - - |

chief_kirill = {
    "id": "chief",
    "name": "Chief Kirill is",
    "dialogue": dialogues.d_chief_kirill_1,    
}

#- - - - - - - - - - - - -  HOSPITAL - - - - - - - - - - - - - - |


hospital_receptionist = {
    "id": "nurse",
    "name": "A nurse sitting at the reception desk is",
    "dialogue": None, #replace me
    
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
	"dialogue": None, #replace me
}

killer = {
	"id": "killer",
	"name": "The Killer is",
	"dialogue": None, #replace me
}
#- - - - - - - - - - - - -  SHIPPING COMPANY - - - - - - - - - - - - - - |

shipping_ceo = {
	"id": "CEO",
	"name": "the Shipping CEO is",
	"dialogue": None,	 #replace me
}

#- - - - - - - - - - - - -  JOE'S HOUSE - - - - - - - - - - - - - - |

joe_wife = {
	"id": "mrs branson",
	"name": "Mrs Branson ",
	"dialogue": None, #replace me
}
"""Kirill

Doctor
Joe
Receptionist
Killer

Shipping Company CEO

Wife
"""