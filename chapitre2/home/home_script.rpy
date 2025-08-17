

label backhome:
    stop music fadeout 2.0
    stop sound fadeout 2.0
    
    play music "music/doorhome.mp3" volume 0.5 noloop
    label homeambiance:
        
        play background homeambianceneutral volume 1.4 loop
        show screen minicarte3
        show screen homescreen4 with dissolve
        hide screen minicarte3
        call screen homescreen4


label newdaystart:
    if groceries <= 0:
        show closetempty
        "I have nothing to eat, I should probably go buy some groceries."
        show screen homescreen4
        call screen homescreen4
    elif party_started == True:
        jump partydate
        
    else: 
        scene beforebedphone
        "I eat dinner then lay on my bed. Doomscrolling for an hour or two."
        
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
            $ corridorconv_done = False
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
            jump homeambiance

label gotobed: 
            scene brushingteeth5
            play sound toothbrushing volume 0.3 noloop
            "I undress and brush my teeth."
            label justbed:
                scene sleeping3e
                play sound gotobedsound volume 1 noloop
                "I lay on my bed and fall asleep almost instantly."
                
                $ class_done = False
                $ groceries -= 1
                $ sarah_conv_done = False
                $ lisa_conv_done = False
                $ sacha_conv_done = False
                $ corridorconv_done = False
                $ mila_conv_done = False
                $ linda_conv_done = False
                $ elise_sagain_done = False
                $ workday_done = False

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
                    $ sarah_relation_status_text = "I should walk down to the cafe, just to clear my mind."
                if sarahcafe_conv1_done == True and sacha_sarah_date_done == False:
                    $ sarah_relation_status_text = "Maybe I'll see Sarah tonight while I hang out."
                if day_until_new_date : 
                    $ day_until_new_date -= 1
                if sarah_homedate_done == True:
                    $ elise_cafe = True
                if sarah_tvdate_done == True:
                    $ sarah_cafe = True
                if sarahcafe_conv2_done == True:
                    $ sarah_elise_cafe = True
                
                # /////////quick bed direction///////////
                if quickbed == True and quickbed_disabled == False and day % 7 != 0:
                
                    pause 1.0
                    scene black 
                    $ quickbed = False
                    jump map3
                #  /////////////////////////////////
                $ quickbed_disabled = False
                scene black with dissolve
                pause
                scene home00 with dissolve
                
                "The next day, I wake up feeling refreshed."
                if day % 7 == 0:
                    jump rentdue
                elif (jobaskedlaura_done == True and boss_textconv_done == False) or work_count == 1:
                    jump bosstexting
                jump homeambiance



screen homescreen4:
    $ number = renpy.random.randint(1, 2)
    if number == 2:     
        timer 1 action Function(
        renpy.music.play,
        "music/home/homemusic.mp3",
        channel="music",
        loop=False,
        fadein=2.0
        
    )
    elif number == 1:
        
        on "show" action Function(
        renpy.music.play,
        "music/home/footstep.mp3",
        channel="music",
        loop=False,
        fadein=2.0)
       

        

    
    # elif number == 4:
    #     timer 1 action Play("music", "music/home/ambient.mp3")
    
    frame:
        imagemap:
            ground "home00.jpg"
            hover "home00hover.jpg"
            hotspot (0, 1029, 1055, 408) action Jump("cantsleep2")
            hotspot (2153, 1152, 374, 274) action Jump("map4")


label cantsleep2:
        stop music 
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
    stop music fadeout 0.5
    stop background fadeout 0.5
    $ number = renpy.random.randint(1, 3)
    if number == 2 or number == 3:
        jump stairsencounter

    else:
        scene stairshome
        "I close my door, making sure it's locked, and head downstairs."
        jump map3