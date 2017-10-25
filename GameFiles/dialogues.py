import items
#Initial Dialogues-------------------------------------------------------

d_chief_kirill_1 = {
        "a": ["OPTION A", "NPC RESPONCE A", "end_convo"],
        "b": ["OPTION B", "NPC RESPONCE B", "end_convo"],
        "c": ["OPTION C", "NPC RESPONCE C", "end_convo"]
}

d_hospital_receptionist_1 = {
    "a": ["Do you know in which room I can find Joe Branson?", "May I ask what's your relation with the patient?",
        {
        "a": ["I am investigating his case.", "Oh ok. Just go left and follow the corridor to the last room.",
            {
            "a": ["Ok Thanks.", "No problem", "end_convo"],
            "b": ["Do you happen to know who's the doctor assigned to this patient?", "Yes. It is Dr. Kim.",
                {
                "a": ["Ok Thanks.", "No problem", "end_convo"]
                }
                ],
            "c": ["Did the patient have any valuables on him at the time of being admitted to hospital?", "Yes. He had some keys.",
                {"a": ["Ok Thanks.", "No problem", "end_convo"],
                "b": ["Can I take them please?", "Yes. No problem", [items.joe_keys]]
                }
                ]
            }
            ],
        "b": ["We do kinky sh!t together.", "Security!", "end_game"]
        }
        ],


    
    "b": ["Hi, I seem to have lost my number, can I have yours?", "Excuse me? I have a boyfriend.", "end_convo"]
}

d_hospital_receptionist_2 = {
    "a": ["OPTION A", "NPC RESPONCE A", "end_convo"],
    "b": ["OPTION B", "NPC RESPONCE B", "end_convo"],
    "c": ["OPTION C", "NPC RESPONCE C", "end_convo"]
}


d_doctor_kim_1 = {
    "a": ["Hi. I'm the investigor assigned to Mr. Branson's case.", "Oh Hello. I am Dr. Kim. I have been expecting you.", 
        {
        "a": ["So how is his condition?", "At the moment. He's in a state of coma.",
            {
            "a": ["Please explain.", "He was hit with a blunt instrument. So hard that it put him into comatose state.",
                {
                "a": ["Do you know exactly when he'll be up and mobile enough to talk?", "Given his conditions, only time can tell when he'll wake up. It may take days or even months.",
                    {
                    "a": ["Ok, Thanks.", "No problem.", "end_convo"]
                    }
                ]
                }
            ],
            "b": ["Do you know what weapon hit him that put him into this state", "He was most likely whipped with a pistol or some metallic object.", "end_convo"]
            }
        ]
        }
    ]
}

<<<<<<< HEAD

#-------------------- DIALOGUE DICTIONARY --------------------------------|
dialswap = {
    "nurse": d_hospital_receptionist_2
}
=======
d_doctor_1 = {
>>>>>>> ccfab89e20b832fde7d00988fd3c418a7379c3b0
