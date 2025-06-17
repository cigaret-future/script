
label stairsencounter:
    
    $ encounternum = renpy.random.randint(1, 2)
    if encounternum == 1:
        jump sacha
    elif encounternum == 2:
        jump sarah



label sacha:
    if sacha_conv_done == True:
        scene stairshome
        "I close my door, making sure it's locked, and head downstairs."
        jump map3
    else: 
        if sacha_count == 0: 
            jump sacha0
        if sacha_count == 1:
            jump sacha1
        if sacha_count >= 2:
            jump sacha2

label sacha0:
    $ sacha_count += 1
    scene stairs4   
    "I close my door, making sure it's locked, and head downstairs."
    "A person is coming down the stairs."
    show sasha
    sac "Hello, are you new here?" 

    name "Hi! Yeah, I just moved in this week." 

    sac "Welcome! What's your name?"

    name "[name], and you?" 

    sac "I’m Sacha, nice to meet you!" 

    name "Same here." 

    sac "See you around, neighbor!" 

    name "See you." 
    hide sasha
    $ sacha_conv_done = True
    
    jump map3

label sacha1:
    scene stairs4
    "I close my door, making sure it's locked, and head downstairs."
    "A person is coming down the stairs."
    show sasha
    sac "Hello, what's up? Doing anything interesting?"

    name "Hey, not really. And you?"

    sac "Going to work... I have to open the store in 30 minutes. Ugh..."

    name "Sounds like a pain."

    sac "It is."

    sac "Hey, we should go out one evening, grab a drink or go to a party."

    name "Yeah, why not? Sounds good."

    sac "Alright, see you later then!"
    hide sasha
    name "Bye."
    $ sacha_count += 1
    $ sacha_conv_done = True

    jump map3

label sacha2:
    scene stairs4
    "I close my door, making sure it's locked, and head downstairs."
    "A person is coming down the stairs."
    show sasha
    sac "Hey, how are you doing?"
    name "Hey, good, you?"
    sac "Tired."
    name "Same here. Have a good day at work."
    sac "Thanks, see you later."
    hide sasha
    $ sacha_count += 1
    $ sacha_conv_done = True

    jump map3

label sarah: 
    if sarah_conv_done == True:
        scene stairshome
        "I close my door, making sure it's locked, and head downstairs."
        jump map3
    elif sarah_conv_done == False:
        if sarah_count == 0 and sarah_pissed == False:
            jump sarah0
        elif sarah_pissed == True:
            jump sarahexplain
        elif sarah_count >= 1 and sacha_sarah_date_done == True and day_until_new_date == 0 and sarah_homedate_done == False:
            jump sarahdate2
        elif sarah_count >= 1 and elise_cafe_conv_done == True and day_until_new_date == 0 and sarah_tvdate_done == False:
            jump texto_stairs
        # elif sarah_count >= 1 and sarah_homedate_done == True and day_until_new_date == 0: 
        #     jump 
        elif sarah_count >= 1 and sacha_sarah_date_done == True and day_until_new_date > 0:
            jump sarah1
        elif sarah_count >= 1 and sacha_sarah_date_done == False:
            jump sarah1
        else:
            jump sarah1

label sarah0:
    scene stairssarah
    "I close my door, making sure it's locked, and head downstairs."
    "A person is coming down the stairs."
    show greetting6
    name "Hello, you live here too?"

    sac "Yep, welcome to the building! I'm Sarah."

    name "I'm [name], nice to meet you."

    sac "Nice to meet you too! If you need anything, don't hesitate to ask."

    name "Thanks, I will."
    $ sarah_relation_status_text = "I hope to meet Sarah more often in the corridor in the coming days"
    $ sarah_count += 1
    $ sarah_conv_done = True
    hide greetting6
    scene stairshome

    "She seems nice. Maybe I'll see her around later."
    jump map3

label sarah1: 
    scene stairssarah
    "I close my door, making sure it's locked, and head downstairs."
    "Sarah is coming down the stairs."
    show sarah5
    sar "Hey, how's it going?"
    name "Hey, good, you?"
    sar "A bit tired, but we keep it rolling."
    name "Yeah, I am tired too, all the studying."
    sar "Gotta keep it up, right?"
    name "Yeah, I guess so."
    sar "Well, see you around!"
    hide sarah5
    $ sarah_conv_done = True
    jump map3

label texto_stairs:  
    scene stairshome
    "A notification pops up on my phone."
    s_nvl "Hey, what are you doing?"
    n_nvl "Hey, nothing much."
    s_nvl "Do you want to come watch a movie at my place with Elise?"
    menu:
        "Sure, I'm in.":
            n_nvl "I'm in."
            s_nvl "Great, see you at my place."
            nvl clear
            jump sarahdate3
        "I can't, I have stuff to do":
            n_nvl "I'm sorry, I can't. I have stuff to do."
            s_nvl "Oh, that's too bad. Maybe next time."
            $ day_until_new_date = 3
            nvl clear
            jump map3

label sarahexplain:
    scene stairssarah
    "I close my door, making sure it's locked, and head downstairs."
    "Someone is coming down the stairs."
    show sarahbothered
    sar "Hey, thanks for turning down the music the other night. Just so you know, I’m not a fan of loud music in the evenings."

    name "I'm sorry! I thought it wouldn't be too loud!"

    sar "It's okay. The previous neighbors used to blast their music, so I’d prefer if we’re clear on keeping it quiet."

    name "I get it, lousy neighbors can be a real pain. Just so you know, I'm not the type to throw big parties at my place. In fact, I'm pretty quiet myself."

    sar "Ok, ok."

    sar "Well, actually, I don’t mind if you play music occasionally. I’m just a bit stressed right now. I've got so much on my plate and deadlines approaching."

    name "Yeah, I understand perfectly. You don’t have to justify yourself. I will buy a pair of headphones."

    sar "I like to party too, just not right now."

    name "Yes, I understand. We can’t party all the time."

    sar "That's right."
    $ sarah_pissedconv_done = True

    if sarah_count == 0:
        $ sarah_relation_status_text = "I hope to meet Sarah more often in the corridor in the coming days"

        sar "By the way, what's your name?"

        name "I am [name], and you?"

        sar "I am Sarah."

        sar "Well, [name], I’m glad we talked. I’ll see you later. I have to go!"

    elif sarah_count >= 1:
        sar "Well, that’s cool. I’m glad we talked. I’ll see you later. I have to go!"

    name "Ok, see you later then."

    sar "Have a good day."

    name "You too."

    hide sarahbothered
    "That went pretty well."
    $ sarah_count += 1
    $ sarah_conv_done = True
    $ sarah_pissed = False
    
    jump map3