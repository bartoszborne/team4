import items
#Initial Dialogues-------------------------------------------------------

d_chief_kirill_1 = {
    "a": ["I'm here about the new assignment.", "Yes, that's right. Have a seat.", 
        {
        "a": ["So what is it Chief?", """
        There was an attempt on the life of Joe Branson, one of our detectives at this branch. He's currently in a coma at a nearby hospital. 
        I want you to find out who exactly did this to him and arrest the perpetrator.
        """, 
            {
            "a": ["Ok, got it.", "Here's your assignment file. I expect to see you when you find out who the perpetrator is.", [items.assignment]]
            }
            ]
        }
        ]
}

d_chief_kirill_2 = {
    "a": ["I like your red jeans", "... Get back to your work.", "end_convo"]
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
    "a": ["Hi again. Can I get your number this time? please.", "... Please go away!", "inc_convo"]
}

d_hospital_receptionist_3 = {
    "a": ["PLEEASE Can I get your number this time!?", "Fine! dial 999 and i'll accept it ;)", "end_convo"]
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
                    "a": ["Ok, Thanks.", "No problem.", "inc_convo"]
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

d_doctor_kim_2 = {
    "a": ["Are you related to Kim Jong Un, the dictator in North Korea?", "...", "end_convo"]
}

#-------------------- DIALOGUE DICTIONARY --------------------------------|
dialswap = {
    "nurse": [d_hospital_receptionist_2, d_hospital_receptionist_3],
    "doctor": [d_doctor_kim_2]
}

