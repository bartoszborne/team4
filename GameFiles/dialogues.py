import items
#Kirill Dialogues-------------------------------------------------------

d_chief_kirill_1 = {
    "a": ["I'm here about my first assignment.", "Yes, that's right. Have a seat.", 
        {
        "a": ["So what is it Chief?", "There was an attempt on the life of Joe Branson while he was on a case, one of our detectives at this branch. He's currently in a coma at a nearby hospital. I want you to find out who exactly did this to him and arrest the perpetrator", 
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


d_chief_kirill_ending = {
    "a": ["So Chief, mind explaining why you're here?", "I'm just here to investigate.", 
        {
        "a": ["Yeah, I dont buy it, just tell me the truth or I'll shoot you. -- aims the gun at Kirill --", "- Kirill's workers aims at you - Alright, I'll tell you. - Kirill tells his men to  not shoot - Joe Branson got his nose too close to finding out about my \"business\". And the only way I can make him stop is by killing him. However, that stupid worker of mine was meant to make it look like Joe died in a hit and run, you know, so that his death doesn't raise any suspicions. But surprise, surprise, he's alive. Which is why I blackmailed him to finish the job and kill him. And the rest you know.",
            {
            "a": ["As the Chief of the Police, why did you assign me to take on this job? Didn't think I'd get this far?", "Honestly, yes. And the fact that this is your first assignment, if you were to ever find out it's me, it's a lot less trouble to deny accusations from a newbie. So I'll give you a choice. I'll let you live if you put your gun down keep your mouth shut or I'll let my goons shoot you.", 
                {
                "a": ["-Shoot Kirill-", "-Kirill's workers shoots you-", "win_game"],
                "b": ["-Put your gun down-", "Shoot him boys -Kirill's workers shoots you-", "end_game"] # NOTE
                }
                ]
            }
            ],
        "b": ["Ah ok, that's good. Two investigators should solve this case much faster.", "-shoots you-", "end_game"]
        }
        ]
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
            "a": ["Please explain.", "We believe that he was hit by a car. So hard that it put him into comatose state.",
                {
                "a": ["Do you know exactly when he'll be up and mobile enough to talk?", "Honestly, it's a mirccle he even survived. Only time can tell when he'll wake up. It may take days or even months.",
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

#------------------------------------KILLER DIALOGUES-------------------------------------------------------

"""
NOTE: Ignore this. this is just to keep my head sane.
d_killer_1_agressive = {
    "a": ["Well, If it comes to this - shoot in a knee – Now tell me who you are working if you still want to walk!", "Aaaa! What the f*ck are you doing?!...All right, Jesus, I will talk. … I got an email from an encrypted email address. It had the name of the target and my reward for my job.*ugh* There was also a name, “Nickname”, so I knew that I better take the job. Was that really necessary?!", 
        {
        "a": ["So who is “nickname”? and have you ever seen this man?", "Everyone knows his name. People call him that because all drug deals go though him, every dealer in town work for him, because he is their dealer. And if you go against him, you don’t live long. And no, no one knows how he looks like. Only that he has power and drugs, so much people are scared to get to know who he is.", 
            {
            "a": ["Don’t make me shoot your other leg. Jail is even worse in a wheelchair.", "WOW, wow, no need for that! I am going to regret this… People talk about a shipping company operating at the docks. There are three ships, one leaves every day and a different ship replaces it, so it looks like nothing changes. It happens during the night, so no one can see ships change. That must be the place.", "end_convo"]
            }
            ]
        }
        ]
    }

d_killer_1_compromise = 
        {
        "a": ["So who is “nickname”? and have you ever seen this man?", "Everyone knows his name. People call him that because all drug deals go though him, every dealer in town work for him, because he is their dealer. And if you go against him, you don’t live long. And no, no one knows how he looks like. Only that he has power and drugs, so much people are scared to get to know who he is.", 
            {
            "a": ["Remember the deal: you talk and I`ll make sure that you end up spending your jail time alive. You will be safe.", "I am going to regret this… People talk about a shipping company operating at the docks. There are three ships, one leaves every day and a different ship replaces it, so it looks like nothing changes. It happens during the night, so no one can see ships change. That must be the place.", "end_convo"]
            }
            ]
        }
"""
d_killer_1 = {
    "a": ["Put the knife down!", "-drops knife-", [items.knife]],
    "b": ["-Charge at him-", "-stabs you-", "end_game"]
}


d_killer_2 = {
    "a": ["Why did you kill Joe Branson?", "Detective. Not all can run around town thinking they can do whatever they want just because they have a badge…", 
        {
        "a": ["Cut the crap, You are nothing but a cheap thug doing dirty work for small cash! You are not gaining anything from this but another jail time. Now tell me the reason you killed him!", "And what do I get from telling you anything?! I am going to jail anyway, like you said. What can you offer me for that info?", 
            {
            "a": ["Well, If it comes to this -shoot in a knee– Now tell me who you are working if you still want to walk!", "Aaaa! What the f*ck are you doing?!...All right, Jesus, I will talk. … I got an email from an encrypted email address. It had the name of the target and my reward for my job.*ugh* There was also a name, “Nickname”, so I knew that I better take the job. Was that really necessary?!", 
                {
                "a": ["So who is “nickname”? and have you ever seen this man?", "Everyone knows his name. People call him that because all drug deals go though him, every dealer in town work for him, because he is their dealer. And if you go against him, you don’t live long. And no, no one knows how he looks like. Only that he has power and drugs, so much people are scared to get to know who he is.", 
                    {
                    "a": ["Don’t make me shoot your other leg. Jail is even worse in a wheelchair.", "WOW, wow, no need for that! I am going to regret this… I work inside a warehouse... Inside the warehouse contains crates full of toys. But don't be decieved by them, if you break the toys into half, a pack of cocaine and other drugs can be found inside.", 
                        {
                        "a": ["So how do I get in without getting caught?.", "Well, security is tight. All I can give you now is the code that will give you access into the warehouse. That's all I know. So please no more.", [items.warehouse_passcode]]
                        }
                        ]
                    }
                    ]
                }
                ]
            }
            ],
        "b": ["You are clearly just a hired muscle. Tell me who hired you and I might move you to a better prison, one where you won`t get shanked after your second night.", "Okey, you got a deal… I got an email from an encrypted email address. It had the name of the target and my reward for my job. There was also a name, “Nickname”, so I knew that I better take the job.", 
            {
            "a": ["So who is “nickname”? and have you ever seen this man?", "Everyone knows his name. People call him that because all drug deals go though him, every dealer in town work for him, because he is their dealer. And if you go against him, you don’t live long. And no, no one knows how he looks like. Only that he has power and drugs, so much people are scared to get to know who he is.", 
                {
                "a": ["Remember the deal: you talk and I`ll make sure that you end up spending your jail time alive. You will be safe.", "I am going to regret this… Inside the warehouse contains crates full of toys. But don't be decieved by them, if you break the toys into half, a pack of cocaine and other drugs can be found inside.", 
                    {
                    "a": ["So how do I get in without getting caught?.", "Well, security is tight. All I can give you now is the code that will give you access into the warehouse. That's all I know. So please no more.", [items.warehouse_passcode]]
                    }
                    ]
                }
                ]
            }
            ]
        }
        ],
    "b": ["Who are you working for?", "You are not getting anything from me. I was a prisoner once, you have nothing what would scare me now.", 
        {
        "a": ["You think that you are so tough, excon, nothing can scare you, think of an isolation room. Four blank walls, no windows and nobody around. Drives people insane… Because this is how you can spend the rest of your jail time, or you can talk and give me what I want.", "Ugh…F*ck…Okey… I got an email from an encrypted email address. It had the name of the target and my reward for my job. There was also a name, “Nickname”, so I knew that I better take the job.",
            {
            "a": ["So who is “nickname”? and have you ever seen this man?", "Everyone knows his name. People call him that because all drug deals go though him, every dealer in town work for him, because he is their dealer. And if you go against him, you don’t live long. And no, no one knows how he looks like. Only that he has power and drugs, so much people are scared to get to know who he is.", 
                {
                "a": ["Remember the deal: you talk and I`ll make sure that you end up spending your jail time alive. You will be safe.", "I am going to regret this… Inside the warehouse contains crates full of toys. But don't be decieved by them, if you break the toys into half, a pack of cocaine and other drugs can be found inside.", 
                    {
                    "a": ["So how do I get in without getting caught?.", "Well, security is tight. All I can give you now is the code that will give you access into the warehouse. That's all I know. So please no more.", [items.warehouse_passcode]]
                    }
                    ]
                }
                ]
            }
            ],
        "b": ["You are going to prison anyway, so if you give me the information about your employer I will try my best to put him in the same place as you are, so you can have your revenge.", "No, boss. It doesn’t work this way. I don’t even know his face. This is an empty deal.", 
            {
            "a": ["Well, If it comes to this -shoot in a knee– Now tell me who you are working if you still want to walk!", "Aaaa! What the f*ck are you doing?!...All right, Jesus, I will talk. … I got an email from an encrypted email address. It had the name of the target and my reward for my job.*ugh* There was also a name, “Nickname”, so I knew that I better take the job. Was that really necessary?!", 
                {
                "a": ["So who is “nickname”? and have you ever seen this man?", "Everyone knows his name. People call him that because all drug deals go though him, every dealer in town work for him, because he is their dealer. And if you go against him, you don’t live long. And no, no one knows how he looks like. Only that he has power and drugs, so much people are scared to get to know who he is.", 
                    {
                    "a": ["Don’t make me shoot your other leg. Jail is even worse in a wheelchair.", "WOW, wow, no need for that! I am going to regret this… Inside the warehouse contains crates full of toys. But don't be decieved by them, if you break the toys into half, a pack of cocaine and other drugs can be found inside.", 
                        {
                        "a": ["So how do I get in without getting caught?.", "Well, security is tight. All I can give you now is the code that will give you access into the warehouse. That's all I know. So please no more.", [items.warehouse_passcode]]
                        }
                        ]
                    }
                    ]
                }
                ]
            }
            ]
        }
        ]
}

d_killer_3 = {
    "a": ["- stare - ", "What do you want? I've told ye everythin'!", "end_convo"]
}

#-------------------- DIALOGUE DICTIONARY --------------------------------|
dialswap = {
    "chief": [d_chief_kirill_2],
    "nurse": [d_hospital_receptionist_2, d_hospital_receptionist_3],
    "doctor": [d_doctor_kim_2],
    "mrs branson": [d_joe_wife_2],
    "killer": [d_killer_2, d_killer_3] #check me
}
