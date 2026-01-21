label toiletparty:
    if isabelle_date_done == True and toiletemilie_done == False:
        scene gettingoutoftoilet
        
        "Someone is getting out."
        scene gettingoutoftoiletblur with dissolve
        show emiliepose100 with dissolve
        emi "oh..."
        emi "jeez what you guys were doing in here?"
        name "huh? nothing."
        emi "I mean it's ok, I don't judge."
        emi "Maybe next time do it in a proper room."
        name "yeah, sure."
        show emiliepose101 with dissolve
        hide emiliepose100 with dissolve
        emi "Hmmm, I mean.."
        emi "It's kinda wild."
        name "I guess."
        emi "Do you think you could do it again?"
        name "what?"
        emi "I mean you know.. don't you want to..."
       
        name "Huh?"
        emi "You just met this girl right?"
        name "Yes but we talked and all..."
        emi "Yeah but you know, it's not like you know her."
        name "I don't know"
        emi "If you did it with her, you could potentially do it with someone else right?"
        $ toiletemilie_done = True
        menu:
            "yeah that's true":
                name "I guess.."
                emi "great!"
                emi "Come on hurry up."
                emi "Someone might come in."
                hide emiliepose101 with dissolve
                scene black with dissolve
                jump emiliescene
            "It doesn't work like that":
                emi "pff you are weird.."
                "She leaves abruptly"
                hide emiliepose101 with dissolve
                scene ericpeeing
                "I enter the toilet and sit on the toilet seat."
                "I take a moment to relax and gather myself."
                "Jeez this feel nice."
                
                jump upstairs

    elif drink_count >= 5:
        jump toiletscene
    
    else:
        jump toiletscene
    label toiletscene:   
        
        if renpy.random.randint(1, 2) == 1:
            scene toiletscene
            "I enter the toilet."
            "I don't really feel like peeing, but at least I know where it is."
            "It's a bit cramped, but at least it's clean."
            "I take a moment to gather myself before heading back to the party."
        elif renpy.random.randint(1, 2) == 2:
            scene ericpeeing
            "I enter the toilet and sit on the toilet seat."
            "I take a moment to relax and gather myself."
            "Jeez this feel nice."

        jump upstairs
    

label partybathroom:
    if sebastianjen_date_started == True and sebastianjen_date_done == False:
        scene corridorscreenarrow
        "It looks like there are people inside."
        menu:
            "Open the door":
                jump sebjendate

            "Stay outside":
                jump upstairs
    elif isabelle_date_done == True and sabrinaconv_done == False:

        scene corridorscreenfloutracy with dissolve
        "Someone is getting out.."
        show sabrinaview with dissolve
        $ sabrinaconv_done = True
        
        sab "Oh it's you.."
        "She looks at me with a mischievous gaze..."
        sab "You still have some left on your face.."
        sab "And your tee-shirt.."
        sab "Better clean it up before going back to the party."
    
        jump upstairs
    elif drink_count >= 5:
        scene drinkingpartybathroom
        "I enter the bathroom, feeling a bit dizzy from all the drinks."
        "Maybe I should slow down a bit."
        "I take a moment to splash some water on my face and gather myself."
        $ drink_count = 2
        jump upstairs
    else:
        scene bathroompartyscene
        "I enter the bathroom."
        "Cool, I could come here to freshen up if I need to."
    jump upstairs




    label sebjendate:
        if jenpeak_count == 0: 
            scene jenniferseb
            seb "Fuck my cock feels so nice in your mouth"
            scene jenniferseb2
            seb "Take it"
            scene jenniferseb3
            seb "Yes..."
            scene jenniferseb4
            jen "Mmmhgh"
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            $ jenpeak_count += 1
            jump upstairs
        elif jenpeak_count == 1:
            scene jenniferseb
            seb "Fuck my cock feels so nice in your mouth"
            scene jenniferseb2
            seb "Take it"
            scene jenniferseb3
            seb "Yes..."
            scene jenniferseb4
            jen "Mmmhgh"
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            $ jenpeak_count += 1
            jump upstairs
        elif jenpeak_count == 2:
            scene jenniferseb
            seb "Fuck my cock feels so nice in your mouth"
            scene jenniferseb2
            seb "Take it"
            scene jenniferseb3
            seb "Yes..."
            scene jenniferseb4
            jen "Mmmhgh"
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            $ jenpeak_count += 1
            jump upstairs
        elif jenpeak_count == 3:
            scene jenniferseb
            seb "Fuckk i am gonna cum..."
            scene jenniferseb2
            window hide
            pause
            scene jenniferseb3
            seb "Yes..."
            scene jenniferseb4
            jen "Mmmhgh"
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            scene jenniferseb
            window hide 
            pause
            scene jenniferseb2
            window hide 
            pause
            scene jenniferseb3
            window hide 
            pause
            scene jenniferseb4
            window hide 
            pause
            $ jenpeak_count += 1
            jump upstairs
        elif jenpeak_count == 4:
            scene jennifersebend
            jeni "Oops.."
            jeni "Hey..."
            "Jennifer walks past me"
            $ jenpeak_count += 1
            $ sebastianjen_date_done = True
            jump upstairs

    label emiliescene:
        
        scene black
        "The girl grabs me by the shoulder and pulls me into the bathroom."
        "I kneel obediently as she lowers her pants."
        "Her already hardened cock appears before me."
        scene firstpose1 with fade
        "A strange mix of excitement and embarrassment washes over me, but I decide to let go."
        emi "Fuck... You're really doing it..."
        scene firstpose2 with dissolve
        "I wrap my lips around her warm flesh."
        "A musky taste, a mix of precum and piss, fills my mouth."
        emi "Oooh yesss..."
        scene firstpose1 with dissolve
        emi "Just like that..."
        scene firstpose3 with dissolve
        window hide
        pause
        scene firstpose2 with dissolve
        window hide
        pause
        scene firstpose3 with dissolve
        window hide
        pause
        scene firstpose2 with dissolve
        window hide
        pause

        scene emilieface2 with dissolve
        emi "Oh God... That's amazing..."
        scene emilieface2 with dissolve
        emi "You know how do handle dick don't you?"
        scene secondpose2v23
        "Feeling more at ease, she takes matters into her own hands and grabs my head."

        emi "Yes.. take my dick"
        scene secondpose2v24
        window hide
        pause
        scene secondpose2v23
        window hide
        pause
        scene secondpose2v24
        window hide
        pause
        scene secondpose2v23
        window hide
        pause
        scene secondpose2v24
        emi "fuuck.."
        scene emilieface2 with dissolve
        window hide 
        pause
        scene emilieface4 with dissolve
        window hide 
        pause
        scene emilieface3 with dissolve
        window hide
        pause 
        scene emilieface4 with dissolve
        window hide 
        pause
        scene emilieface3 with dissolve
        emi "You're... really good at this..."
        "I take more of her length, matching my movements to her rhythm."
        scene secondpose2v26 with dissolve
        "Her grip tightens on my head as she guides my movements."
        scene secondpose2v25 with dissolve
        "I can feel her breathing getting heavier above me."
        scene secondpose2v26 with dissolve
        "She pulls me deeper, her hips moving in rhythm."
        scene secondpose2v25 with dissolve
        "The taste becomes more intense as she gets more excited."
        scene secondpose2v26 with dissolve
        "Her moans become more frequent and urgent."
        scene secondpose2v25 with dissolve
        "I try to match her pace, following her lead."
        scene secondpose2v23 with dissolve
        "She changes angles, seeking the perfect sensation."
        scene secondpose2v26 with dissolve
        "Her body language tells me she's getting close to the edge."
        scene secondpose2v24 with dissolve
        "The intensity builds as her movements become more desperate."
        scene secondpose2v26 with dissolve
        "I can sense her losing control, completely absorbed in the moment."
        scene secondpose2v23 with dissolve
        "Her breathing becomes ragged and uneven."
        scene secondpose2v24 with dissolve
        "The rhythm becomes more frantic as pleasure overtakes her."
        emi "Fuck yes... just like that..."
        scene finalburst1b with dissolve
        window hide
        pause
        scene finalburst3b with dissolve
        emi "Fuck.. yes..."
        emi "You like this don't you."
        emi "You like when i fucked your mouth."
        name "mhmmh"
        emi "I knew it.."
        scene finalburst1b with dissolve
        window hide
        pause
        scene finalburst3b with dissolve
        window hide
        pause
        scene finalburst1b with dissolve
        window hide
        pause
        scene finalburst3b with dissolve
        window hide
        pause
        scene finalburst1b with dissolve
        window hide
        pause
        scene backangle with dissolve
        emi "oh god.."
        emi "I am so glad i asked you."
        scene backangle2 with dissolve
        emi "My shrink is right, i need to talk about my feelings."
        scene backangle with dissolve
        emi "That's what she was refering to."
        scene backangle2 with dissolve
        emi "Yeah, that's right."
        scene backangle with dissolve
        emi "I need to be more open about these kind of thought"
        scene backangle2 with dissolve
        
        scene backangle with dissolve
        emi "You agree right?"
        scene backangle2 with dissolve
        emi "It's important to express ourselves."
        scene backangle with dissolve
        emi "you probably feel the same way."
        scene backangle2 with dissolve
        emi "You must have sucked a lot of dicks in your life."
        scene backangle with dissolve
        emi "I mean, you look like the type of guy who would do that."
        emi "No offense.."
        scene backangle2 with dissolve
        "I feel a bit akward about this conversation."
        "But I nod, not wanting to break the mood."
        scene finalburst3b with dissolve
        window hide
        pause
        scene finalburst1b with dissolve
        window hide
        pause
        scene finalburst3b with dissolve
        window hide
        pause
        scene finalburst1b with dissolve
        window hide
        pause
        scene backangle3 with dissolve
        emi "Shit... it's coming already..."
        
        scene backangle4 with dissolve
        emi "I am gonna cum in your mouth.."
        scene backangle3 with dissolve
        emi "I can feel it building up..."
        
        scene backangle4 with dissolve
        
        emi "Don't stop now..."
        scene backangle3 with dissolve
        emi "Yes... just like that..."
        
        scene backangle4 with dissolve
        emi "Keep going..."
        scene backangle3 with dissolve
        window hide
        pause
        scene backangle4 with dissolve
        window hide
        pause
        
        scene finalburst3b with dissolve
        emi "Fuck... yes..."
        emi "I'm about to explode..."
        scene finalburst2b with dissolve
        window hide
        pause
        scene finalburst3b with dissolve
        window hide
        pause
        scene finalburst1b with dissolve
        emi "Oh shit... it's happening..."
        
        scene finalburst3b with dissolve
        window hide
        pause
        
        scene finalburst2b with dissolve
        emi "Get ready..."
        scene backangle4 with dissolve
        emi "I'm... I'm gonna..."
        emi "Yes... yes... YES..."
        scene backangle3 with dissolve
        window hide
        pause
        scene finalburst2b with dissolve
        window hide
        pause
        scene finalburst3b with dissolve
        window hide
        pause
        scene finalburst2b with dissolve
        window hide
        pause
        scene finalburst3b with dissolve
        window hide
        pause
        scene backangle3 with dissolve
       
        "Her body tenses as orgasm overtakes her."
        scene finalburst2b with dissolve
        window hide
        pause
        scene finalburst1 with dissolve
        "A jet of sperm fills my mouth, hot and salty."
        
        scene finalburst2 with dissolve
        emi "oouuh yeees... "
        "Followed by a second one"
        scene finalburst3 
        "Then a third one"
        scene finalburst1
        emi "drink it.."
        scene finalburst3
        window hide
        pause
        scene finalburst1
        window hide
        pause
        scene finalemilieeric
        emi "That was amazing..."
        emi "Fuck, i hope no one is waiting.."
        emi "I should probably get going."
        emi "Thanks a lot for that."
        emi "See you."

        "She quickly slips out of the toilet, leaving me to collect myself."
        scene corridorscreenarrow with dissolve

        
        jump upstairs