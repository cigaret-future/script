label Mila1_sarahscreen:
    scene cafesarah
    
    show mila00 with dissolve
    name "Hi, do you come here often?"
    mil "Shhh, I can't talk to you."
    mil "I'm in the middle of a sentence."
    mil "I'll lose my train of thought."
    name "Oh, sorry."
    name "I'll come back later."
    $ mila_conv_done = True
    hide mila00 with dissolve
    
    
    show screen cafescreen_sarah
    call screen cafescreen_sarah



label Mila1:
    
    if elise_cafe == True and elise_cafe_conv_done == False:
            scene cafeelisefinal
    
    elif sarah_cafe == True and sarahcafe_conv2_done == False:
            scene cafesarah2
    else: 
        scene cafe2

    if mila_conv_done == True:
        "I already talk to her today"
        jump cafedirection

    elif mila_count == 0:
        jump Mila1_0
    elif mila_count == 1:
        jump Mila1_1
    elif mila_count == 2:
        jump Mila1_2
    elif mila_count == 3:
        jump Mila1_3



label Mila1_0:
    show mila00 with dissolve
    mil "Can't you see I am busy?"
    name "oh sorry... "
    $ mila_count += 1
    $ mila_conv_done = True
    hide mila00 with dissolve
    jump cafedirection

label Mila1_1:
    show mila00 with dissolve
    name "Have we met before?"
    mil "I don't think so, sorry."
    name "I think I saw you at the university."
    name "Are you a student?"
    mil "In psychology."
    name "Ah, nice."
    mil "Yep."
    mil "And you?"
    name "Art history."
    name "I just arrived."
    mil "Cool."
    mil "Good luck."
    name "Thanks."
    $ mila_count += 1
    $ mila_conv_done = True
    hide mila00 with dissolve
    "She isn't very talkative."
    
    jump cafedirection

label Mila1_2:
    show mila02 with dissolve
    name "Heyy! What's up?"
    mil "Oh.. it's you."
    name "I'm just passing by."
    mil "Cool, do you come here often?"
    name "Yeah, I like this place."
    name "It's becoming a habit."
    name "Oh, by the way,"
    name "I'm [name]."
    show mila04 with dissolve
    hide mila02 with dissolve
    "She sighs."
    mil "I'm Mila."
    name "Nice to meet you."
    mil "I am going to work now."
    name "Alright, see you."
    $ mila_count += 1
    $ mila_conv_done = True
    hide mila04 with dissolve
    jump cafedirection

label Mila1_3:
    show mila00 with dissolve
    name "Hey, can I sit here?"
    mil "I'm waiting for someone."
    name "Oh, sorry."
    $ mila_count += 1
    $ mila_conv_done = True
    hide mila00 with dissolve
    jump cafedirection