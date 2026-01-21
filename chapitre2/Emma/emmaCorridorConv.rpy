

label emma_corridor_sequence:

    # Fond dynamique
    if day % 2 == 0 and Jenny_end_done == False and zoey_uni_conv_done == False:
        scene zoeycorridorblur with dissolve
    else:
        scene corridorrealistblur with dissolve

    # ===================================================================
    # 1. Déjà fait la vraie scène toilettes → phase repeat + teasing
    # ===================================================================
    if emma_date_done:
        if emma_corridor_progress < 5:
            $ emma_corridor_progress = 5

        if emma_corridor_progress == 5:           # première fois après la date
            $ emma_corridor_progress = 6
            jump emma_postdate_first_tease
        else:
            jump emma_toilet_repeat               # toutes les suivantes

    # ===================================================================
    # 2. CONDITION FINALE : proposition toilettes (4 classes OU 4 couloirs)
    # ===================================================================
    elif (classdateemma_count >= 4) or (emma_corridor_progress >= 4):
        $ emma_corridor_progress = max(emma_corridor_progress, 5)
        jump emma_toilet_invitation_first

    # ===================================================================
    # 3. Flirt chaud (après au moins 2-3 interactions en classe)
    # ===================================================================
    elif classdateemma_count >= 2:
        $ emma_corridor_progress = max(emma_corridor_progress, 4)
        jump emma_corridor_flirty

    # ===================================================================
    # 4. Deuxième rencontre soft dans les couloirs
    # ===================================================================
    elif emma_corridor_progress == 3:
        $ emma_corridor_progress = 4
        jump emma_corridor_soft3

    # ===================================================================
    # 5. Première rencontre soft avancée (déjà vu plusieurs fois)
    # ===================================================================
    elif emma_corridor_progress == 2:
        $ emma_corridor_progress = 3
        jump emma_corridor_soft2

    # ===================================================================
    # 6. Première rencontre soft basique (déjà vu au moins une fois en cours)
    # ===================================================================
    elif emma_corridor_progress == 1 or classdate_count >= 1:
        $ emma_corridor_progress = 2
        jump emma_corridor_soft1

    # ===================================================================
    # 7. Toute première fois dans les couloirs (même avant le premier cours)
    # ===================================================================
    else:  # emma_corridor_progress == 0
        $ emma_corridor_progress = 1
        jump emma_corridor_first_ever

    return


# ===========

# EMMA RANDOM CORRIDOR EVENTS – Final version (English + gardenuni_start2)
# ========================


label emma_corridor_first_ever:
    "A girl approaches."
    show emma00 with dissolve
    emm "Hey. You’re the new face I keep seeing around, right?"
    name "Uh… yeah?"
    show emma05 with dissolve
    hide emma00 with dissolve
    emm "Thought so. You have that lost-puppy look. It’s cute."
    emm "I’m Emma, by the way."
    name "…I’m [name]."
    show emma03 with dissolve
    hide emma05 with dissolve
    emm "Relax. I don’t bite…"
    "She flashes a quick, dangerous smile and steps aside."
    emm "Catch you later."
    hide emma03 with dissolve
    jump corridorscreen_redirection


label emma_corridor_soft1:
    "Emma appears out of nowhere and bumps your hip with hers."
    show emma02 with dissolve
    emm "Hey, you okay? Haven’t seen you all morning."

    menu:
        "Just trying to find a quiet corner to get some reading done…":
            show emma05 with dissolve
            hide emma02 with dissolve
            emm "Still the perfect little student, huh?"
            name "Trying to survive the semester."
            show emma03 with dissolve
            hide emma05 with dissolve
            emm "You’re way too serious. Doesn’t suit you."
            "She gives you a half-smirk, almost fond."
            emm "One day you’re gonna burn out if you keep taking everything so seriously."
            name "Maybe."
            show emma05 with dissolve
            hide emma03 with dissolve
            emm "When you finally need a break, let me know."
            "She walks past, throwing you a quick glance over her shoulder."

        "I’m good, you?":
            show emma05 with dissolve
            hide emma02 with dissolve
            emm "Better than you, apparently."
            "She leans against the wall beside you."
            emm "You look like you’ve been living on coffee and stress."
            name "Pretty accurate."
            show emma02 with dissolve
            hide emma05 with dissolve
            emm "Hey… I’m just teasing you. You’re doing great, you know that?"
            "She flashes you a quick, genuine smile before pushing off the wall."
            emm "But maybe grab a real meal at some point, yeah?"

        "Eh, too much to do…":
            show emma03 with dissolve
            hide emma02 with dissolve
            emm "Classic survival mode."
            name "Pretty much."
            show emma05 with dissolve
            hide emma03 with dissolve
            emm "You’re gonna crash hard if you keep going like this."
            "She shakes her head, amused."
            emm "Take care of yourself, okay? Would be a shame if you didn’t."

    hide emma05 with dissolve
    jump corridorscreen_redirection


label emma_corridor_soft3:     
    "A familiar hand snatches your earbud before you can react."
    show emma02 with dissolve
    emm "Hey, wait up."
    "She tugs one of your earbuds out before you can react."
    show emma00 with dissolve
    hide emma02 with dissolve
    emm "What are we listening to today, mister mystery?"
    name "Hey! Give it back!"
    show emma05 with dissolve
    hide emma00 with dissolve
    emm "Nope. Quality check first."
    "She pops it in her ear for three seconds, then raises an eyebrow."
    emm "…Lo-fi beats? Really? I had you pegged for secret metalhead."

    menu:
        "It helps me focus.":
            emm "Sure, grandpa. Next you’ll tell me you fall asleep to whale sounds."
            "She laughs and hands the earbud back."
            emm "I’m messing with you. It’s kinda cute, actually."

        "What do you listen to, then?":
            show emma03 with dissolve
            hide emma05 with dissolve
            emm "Right now? Old-school punk when I’m mad, cheesy 2000s pop when I’m happy."
            show emma05 with dissolve
            hide emma03 with dissolve
            emm "Send me your playlist later. I need to know how deep the lo-fi rabbit hole goes."

        "Sometimes I just need silence.":
            emm "You’re such a cliché and I love it."
            "She flicks the earbud cord playfully."

    emm "Alright, I’ll let you return to your chill beats."
    "She slips the earbud back into your ear, fingers brushing your cheek just a little too long."
    emm "But next time you’ll come get it in my room."
    hide emma05 with dissolve
    jump corridorscreen_redirection


label emma_corridor_soft2:
    "Emma slides in front of you"
    show emma02 with dissolve
    emm "Hey, I was looking for you yesterday."
    name "I was in class all day."
    show emma03 with dissolve
    hide emma02 with dissolve
    emm "Too studious… it’s starting to become a flaw."
    "She steps closer and lowers her voice."
    show emma05 with dissolve
    hide emma03 with dissolve
    emm "You know, I really like your style."
    emm "But you often seem busy."
    emm "If you ever need to… unwind, just tell me. I know the perfect spot."

    menu:
        "Thanks, but I need to finish this book first.":
             
            
            show emma03 with dissolve
            hide emma05 with dissolve
            emm "You’re wound way too tight."
            "She steps closer..."
            show emma05 with dissolve
            hide emma03 with dissolve
            emm "Five minutes with me and you’d forget every single lecture."
            name "Five minutes?? where?"
            emm "Let's just say it'll be a change from those neat, tidy classrooms."
            "She holds your gaze two seconds too long, then shrugs with a tiny smirk."

            menu:
                "Sorry, I really have class right now… maybe later?":
                    emm "Boring. But I won’t let you escape forever."
                    hide emma05 with dissolve

                "Only five minutes, huh?":
                    
                    emm "Five is plenty when you know what you’re doing."
                    "She tilts her head, eyes gleaming."
                    emm "And I really, really need it right now."
                    name "Need what?"
                    "Instead of answering, she just grabs your hand and starts walking."
                    emm "You’ll see in ten seconds."
                    scene black with fade
                    "Door locked behind you."
                    jump emmadatequick

        "Huh? Where exactly?":
            
            emm "If I told you now, it would ruin the surprise."
            "She straightens your shirt collar with a finger."
            emm "Let's just say it'll be a change from those neat, tidy classrooms."
            
            hide emma05 with dissolve

        "That your standard pickup line?":
            show emma03 with dissolve
            hide emma05 with dissolve
            emm "Only when I spot someone trying so hard to look unfazed… and failing."
            name "I’m perfectly calm."
            show emma05 with dissolve
            hide emma03 with dissolve
            emm "Keep telling yourself that."
            "She lightly brushes your cheek with the back of her fingers."
            emm "You’re burning up."
            hide emma05 with dissolve
    
    jump corridorscreen_redirection









    label emma_corridor_flirty:
        "Someone blocks your path with a hip"
        show emma03 with dissolve                    
        emm "Still thinking about what happened last time?"
        name "Emma, not so loud…"
        show emma05 with dissolve
        hide emma03 with dissolve
        emm "Relax, nobody’s listening."
        "She leans in, almost whispering."
        emm "You were so cute trying not to make a sound."
        emm "Next time I won’t be so gentle."
        hide emma05 with dissolve
        jump corridorscreen_redirection


    label emma_toilet_repeat:
        "Emma appears out of nowhere and pulls you by the sleeve."
        show emma03 with dissolve                     
        emm "Come here… right now."
        show emma05 with dissolve
        hide emma03 with dissolve
        emm "Open up, baby. I need to feel that pretty mouth again."

        menu:
            "Yes, Emma.":
                scene black with fade
                "She drags you into the nearest toilet, locks the door."
                jump emmadatequick

            "Someone might see us…":
                show emma03 with dissolve
                hide emma05 with dissolve
                emm "Then you’d better be quiet."
                scene black with fade
                "You still follow her without hesitation."
                jump emmadatequick

            "Not today.":
                show emma00 with dissolve
                hide emma03 with dissolve
                emm "Pff… you’re no fun today."
                "She walks off, clearly annoyed."
                hide emma00 with dissolve
                jump corridorscreen_redirection

        hide emma05 with dissolve
        jump corridorscreen_redirection


    label emma_postdate_first_tease:                 
        "Someone blocks your path with a hip"
        show emma05 with dissolve                     
        emm "Hold on… you’ve got a little something right here."
        "She reaches out and slowly wipes the corner of your mouth with her thumb."
        name "Shut up…"
        emm "Make me."
        "She laughs softly and ruffles your hair."
        show emma03 with dissolve
        hide emma05 with dissolve
        emm "You’re adorable when you’re all flushed and embarrassed."
        emm "See you soon, baby."
        hide emma03 with dissolve
        jump corridorscreen_redirection

    label emma_toilet_invitation_first:
        "Emma suddenly appears in front of you, a mischievous glint in her eyes"
        show emma05 with dissolve
        emm "Hey you. I was thinking…"
        name "About what?"
        show emma03 with dissolve
        hide emma05 with dissolve
        emm "You looked like you could use a break."
        emm "How about you follow me to the toilets?"
        name "The toilets?"
        show emma05 with dissolve
        hide emma03 with dissolve
        emm "It'll be fun. I promise."
        menu:
            "Sure, why not.":
                
                scene black with fade
                "She grabs your hand and leads you to the nearest toilet."
                jump emmadatequick

            "I don’t think that’s a good idea.":
                
                show emma03 with dissolve
                hide emma05 with dissolve
                emm "Aw, come on. Live a little."
               
                "She walks off, a hint of disappointment in her eyes."
                hide emma03 with dissolve
                jump corridorscreen_redirection

