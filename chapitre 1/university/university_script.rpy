label gardenuni: 
    stop music fadeout 2.0
    scene garden1
    "I'm in the garden of the university."
    jump gardenuni_start

label gardenuni_start:
    scene garden1
    if linda_1st_conv_done == True and marion_1st_conv_done == True:
        "I am getting tired. I should go home and sleep."
    if classe == False:
        menu:
            "Go to the classroom":
                jump class1sttime
            
            "Go to the library":
                if classe == True and linda_1st_conv_done == False:
                    show screen uniscreen
                    call screen uniscreen
                elif classe == False: 
                    show screen uniscreenempty
                    call screen uniscreenempty
                elif linda_1st_conv_done == True:
                    show screen uniscreenlindaout
                    call screen uniscreenlindaout

            "Walk around the university":
                scene corrridor13
                "There aren't many people around. I should go to class first."
                jump gardenuni_start

            "Return to the street":
                show screen minicarte2
                call screen minicarte2
    else:
        menu:
            "Go to the classroom":
                "I already had classes."
                jump gardenuni_start

            "Walk around the university":
                if marion_1st_conv_done == False:
                    jump HugandZoeyStart
                elif marion_1st_conv_done == True:
                    "I have nothing to do here."
                    jump gardenuni_start

            "Go to the library":
                if classe == True and linda_1st_conv_done == False:
                    show screen uniscreen
                    call screen uniscreen
                elif classe == False: 
                    show screen uniscreenempty
                    call screen uniscreenempty
                elif linda_1st_conv_done == True:
                    show screen uniscreenlindaout
                    call screen uniscreenlindaout

            "Return to the street":
                show screen minicarte2
                call screen minicarte2

label class1sttime: 
    menu:
        "skip the intro":
            jump introskip
        "continue":
            pass

    scene unistairs
    "I climb the stairs to the first floor."
    "Many students are walking around the corridors."
    "I struggle to find the right classroom in this maze."
    "After a few minutes of going back and forth, I finally find the right room."
    "Students gather in front of the entrance. A slight buzz rises from the various groups. We finally enter the amphitheater."
    scene studentarrive2
    "I don't really feel like sitting in the front row, so I head a bit higher up in the room."
    
    name "Can I sit here?"

    scene studentarriveflou with dissolve
    show hugopose11 at left:
        xalign 0.3
    hug "Yeah, go ahead. My friend probably won't come."

    name "Thanks."
    hide hugopose11
    scene amphi with dissolve
    "The professor arrives shortly after everyone is settled and begins to introduce the course."
    "It's about the history of romantic iconography. It sounds exciting."
    "I take notes on my small laptop, trying my best to grasp the key points of her presentation. As I write, I remember that I need to find a professor to supervise my thesis."

    name "Is this professor good? I'm new here and don't know anyone."
    scene amphiflou with dissolve
    show hugopose09 at left:
        xalign 0.3
    hug "I had her once in my third year. Her classes are decent, but she's a bit of a bitch with her students."

    name "Ah, that's a shame. I'm looking for a professor to supervise my thesis. I'm not sure if I should choose her then."
    
    hug "Yeah, I wouldn't recommend her. But you should ask Linda; she knows the professors here well. She's a goldmine of information."

    name "Okay, thanks. I'll ask her."
    hide hugopose09
    show hugopose12 at left:
        xalign 0.3
    
    hug "No problem."

    name "Hm, who is Linda, by the way?"
    hide hugopose12
    show hugopose11 at left:
        xalign 0.3
    hug "Oh yeah, sorry. She's the brunette with the black sweater in the third row."

    name "Okay, got it. Thanks."
    hide hugopose11
    show hugopose07 at left:
        xalign 0.3
    hug "No worries. What's your name?"

    name "My name's [name], and yours?"

    hug "I'm Hugo."

    name "Any advice for a new student?"

    hug "Advice? Don't believe everything the professors say. Some of them are full of shit."

    name "Okay, that's counterintuitive, but I'll remember it."
    hide hugopose07
    scene amphi with dissolve
    "The class ends after an hour and a half. The students leave in a disorganized fashion and scatter in the hallways."
    "I try to catch Linda, but she rushed out of the classroom."
    "Shit... I need to find her."
    
    $ classe = True
    jump gardenuni_start


    label introskip:
        $ marion_1st_conv_done = True
        $ linda_1st_conv_done = True
        $ classe = True
        $ zoey_first_conv_done = True
        jump map2