import items
#Kirill Dialogues-------------------------------------------------------

d_chief_kirill_1 = {
    "a": ["I'm here about the new assignment.", "Yes, that's right. Have a seat.", 
        {
        "a": ["So what is it Chief?", """
        There was an attempt on the life of Joe Branson while he was on a case, one of our detectives at this branch. He's currently in a coma at a nearby hospital. 
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

#------------------------------------HOSPITAL RECEPITIONIST DIALOGUES-------------------------------------------------------

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

#------------------------------------DOCTOR DIALOGUES-------------------------------------------------------

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
    "a": ["Are you related to Kim Jong Un, the dictator of North Korea?", "...", "end_convo"]
}

#------------------------------------JOE WIFE DIALOGUES-------------------------------------------------------

d_joe_wife_1 = {
    "a": ["I know this is a difficult time, but could I ask you a few questions?", "Of course. Anything that can help catch whoever did this.",
        {
        "a": ["Did you know anything about the case your husband was working on?", "Not really. He was really private in that regard. He'd keep his work life separate from home.", 
            {
            "a": ["Was there anything suspicious leading up to the attack?", "Hmmm. I did notice in the past few weeks that Joe was out of the house more often. I thought he was working really hard for this case.",
                {
                "a": ["Ok thanks.", "Anytime.", "end_convo"]
                }
                ]
            }
            ]
        }
        ],
    "b": ["Do you know of any place he kept his work? Documents or anything?", "From what I remember, he kept a lot of his work online. He preferred it to keeping physical copies.", 
        {
        "a": ["Do you know where exactly he kept this?", "Well, he enjoyed working in his home office. He spent countless hours in there. Perhaps you could start there?", 
            {
            "a": ["Ok thanks", "No problem.", "inc_convo"]
            }
            ]
        }
        ]
}

d_joe_wife_2 = {
    "a": ["...", "Have you checked his office yet?", "end_convo"]
}

#------------------------------------ DIALOGUES-------------------------------------------------------

d_joe_wife_1 = {
    "a": ["I know this is a difficult time, but could I ask you a few questions?", "Of course. Anything that can help catch whoever did this.",
        {
        "a": ["Did you know anything about the case your husband was working on?", "Not really. He was really private in that regard. He'd keep his work life separate from home.", 
            {
            "a": ["Was there anything suspicious leading up to the attack?", "Hmmm. I did notice in the past few weeks that Joe was out of the house more often. I thought he was working really hard for this case.",
                {
                "a": ["Ok thanks.", "Anytime.", "end_convo"]
                }
                ]
            }
            ]
        }
        ],
    "b": ["Do you know of any place he kept his work? Documents or anything?", "From what I remember, he kept a lot of his work online. He preferred it to keeping physical copies.", 
        {
        "a": ["Do you know where exactly he kept this?", "Well, he enjoyed working in his home office. He spent countless hours in there. Perhaps you could start there?", 
            {
            "a": ["Ok thanks", "No problem.", "inc_convo"]
            }
            ]
        }
        ]
}

d_joe_wife_2 = {
    "a": ["...", "Have you checked his office yet?", "end_convo"]
}

#-------------------- DIALOGUE DICTIONARY --------------------------------|
dialswap = {
    "nurse": [d_hospital_receptionist_2, d_hospital_receptionist_3],
    "doctor": [d_doctor_kim_2],
    "mrs branson": [d_joe_wife_2]
}

