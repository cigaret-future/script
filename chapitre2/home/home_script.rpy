

label backhome:
    stop music fadeout 2.0
    play music "music/doorhome.mp3" volume 0.5 noloop 
    
    show screen homescreen4
    call screen homescreen4


label newdaystart:
    if groceries <= 0:
        show closetempty
        "I have nothing to eat, maybe I should go buy some groceries."
        show screen homescreen4
        call screen homescreen4
    else: 
        scene beforebedphone
        "I eat dinner then I lay on my bed. Doomscrolling for an hour or two."
        
        jump textdirection

label gotobedKate:
     
            scene sleeping3e with dissolve
            "I lay on my bed with the taste of her still fresh on my tongue." 
            "Despite the exhaustion weighing heavily upon me, sleep eludes me."
            "Instead, I find myself imagining scenarios, fantasies of being taken by her again, of submitting fully to her desires."
            
            $ class_done = False
            $ groceries -= 1
            $ sarah_conv_done = False
            $ lisa_conv_done = False
            $ sacha_conv_done = False
            $ mila_conv_done = False
            $ linda_conv_done = False
            $ elise_sagain_done = False
            if emma_date_started:
                $ emma_date_done = True
            $ day_not_over = False
            $ raver_not_over = False
            $ day += 1
            if day_until_new_date : 
                $ day_until_new_date -= 1
            if sarah_homedate_done == True:
                $ elise_cafe = True
            if sarah_tvdate_done == True:
                $ sarah_cafe = True
            if sarahcafe_conv2_done == True:
                $ sarah_elise_cafe = True
            scene black with dissolve
            pause
            scene home00 with dissolve
            "The next day, I wake up with a bitter taste in my mouth and a bit of a headache."
            if day % 7 == 0:
                jump rentdue
            show screen homescreen4
            call screen homescreen4

label gotobed: 
            scene brushingteeth5
            "I undress and brush my teeth."
            
            scene sleeping3e
            "I lay on my bed, and fall asleep almost instantly."


            
            $ class_done = False
            $ groceries -= 1
            $ sarah_conv_done = False
            $ lisa_conv_done = False
            $ sacha_conv_done = False
            $ mila_conv_done = False
            $ linda_conv_done = False
            $ elise_sagain_done = False

            # //////////////////////Emma variables////////////
            if emma_date_started:
                $ emma_date_started = False
                
            if emma_date_done == True:
                $ emma_relation_status_text = "I think she likes me, I should go talk to her during class."
            $ day_not_over = False
            $ raver_not_over = False
            $ day += 1
            # ///////////////////// Sarah Variable//////////////
            if day >= 4 and sarah_count >= 1 and sarahcafe_conv1_done == False:
                $ sarah_relation_status_text = "I should go for a walk to the cafe, just to clear my mind"
            if sarahcafe_conv1_done == True and sacha_sarah_date_done == False:
                $ sarah_relation_status_text = "Maybe I'll see Sarah tonight while I hang out"
            if day_until_new_date : 
                $ day_until_new_date -= 1
            if sarah_homedate_done == True:
                $ elise_cafe = True
            if sarah_tvdate_done == True:
                $ sarah_cafe = True
            if sarahcafe_conv2_done == True:
                $ sarah_elise_cafe = True
            
            # /////////quick bed direction///////////
            if quickbed == True:
                pause 1.0
                scene black 
                $ quickbed = False
                jump map3
            #  /////////////////////////////////
            
            scene black with dissolve
            pause
            scene home00 with dissolve
            "The next day, I wake up feeling refreshed."
            if day % 7 == 0:
                jump rentdue
            elif jobaskedlaura_done == True and boss_textconv_done == False:
                jump bosstexting
            show screen homescreen4
           
            call screen homescreen4



screen homescreen4:
    frame:
        imagemap:
            ground "home00.jpg"
            hover "home00hover.jpg"
            hotspot (0, 1029, 1055, 408) action Jump("cantsleep2")
            hotspot (2191, 248, 362, 1047) action Jump("map4")


label cantsleep2:
    
    # if class_done == True or linda_conv_done == True :
        scene sleeping3e
        jump newdaystart   

     
    # # elif class_done == False:
    # #     scene home00
    # #     "I can't sleep right now, i should go to class first or something."
    # #     show screen homescreen4

    #     call screen homescreen4
        if groceries == 0:
            scene home00
            "I have nothing to eat, I should go buy some groceries."
            show screen homescreen4
            call screen homescreen4
label map4: 
    $ number = renpy.random.randint(1, 3)
    if number == 2 or number == 3:
        jump stairsencounter

    else:
        scene stairshome
        "I close my door, making sure it's locked, and head downstairs."
        jump map3