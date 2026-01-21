label clubalone:
    scene black
    "I’m getting ready to go out. "
    "Let’s see what happens."

    scene streetcut2 with fade
    "The city hums. Neon light scatters across the street. The air smells like rain and fried food."

    scene rosedate-arriving with dissolve
    play music clubmusicambiance volume 1 loop fadein 0.5
    $ renpy.music.set_volume(0.3, delay=0.5, channel="music")

    "The club’s entrance glows red. Bass leaks through the walls like a heartbeat."
   
 

    scene black with dissolve
    "Ten minutes later, I’m in."

    
    scene chloedate2enteringclub with dissolve
    $ renpy.music.set_volume(1, delay=0.5, channel="music")

 
    "I head to the bar."

    scene black with dissolve
    "One gin and tonic."

    scene rosedate-sittingwaiting2 with dissolve


    $ clubalone_drink_count = 0
    $ clubalone_talk_count = 0
    $ clubalone_bathroom_count = 0
    $ clubalone_dance_count = 0

    
    label clubalone_loop:
        scene rosedate-sittingwaiting with dissolve
        menu:
            "Get another drink":
                $ clubalone_drink_count += 1
                scene black with dissolve
                "I finish my glass and slide back to the bar."

                if clubalone_drink_count == 1:
                    scene nightdate_barmanscene with dissolve
                    name "Gin and tonic. No ice."
                    "The bartender nods — same guy as last time."
                    "A girl next to me leans in, voice cutting through the noise."
                    club "No ice?"
                    name "Less watering down the good stuff."
                    "She smiles, turns back to her friend."

                elif clubalone_drink_count == 2:
                    scene nightdate_barmanscene with dissolve
                    name "Same again."
                    "Two guys in matching black shirts are arguing about the DJ."
                    club "—told you, it’s not the original mix!"
                    club "Nah, that drop’s been rinsed since 2019."
                    "I laugh under my breath."
                    name "You guys always this passionate about transitions?"
                    "They both turn."
                    club "Ha! See? Even random people notice!"
                    club "You DJ?"
                    name "Nah, just like to dance. But that transition was rough."
                    club "Finally, someone with taste."
                    "One of them offers me a fist bump."
                    club "You should hear the original mix though."
                    name "Maybe next time."
                    "They go back to debating."
                    scene black with dissolve
                    "As I weave through the crowd to reclaim my stool, a strong hand clamps my shoulder — warm, deliberate, fingers pressing just enough to send a shiver down my spine."

                    "A low, gravel-rough voice purrs against my ear."

                    club "Hey… remember me?"

                    "I turn. She towers over me—the same bouncer from last time. Black tank hugging every curve of muscle, buzz-cut glistening with sweat, eyes dark and hungry under the strobes."

                    name "Hey… yeah."

                    club "You good tonight, sweetheart?"

                    name "Doing great. You?"

                    "She exhales, a tired smirk curling her lips."

                    club "Rough shift. Dragged three drunk assholes out by their collars. and my manager’s been on my ass all night."

                    "Her hand slides down my arm, fingers curling around my wrist — firm, possessive."

                    club "Need to blow off some steam."

                    "She leans in, lips grazing my ear, breath hot and smoky."

                    club "Think that pretty mouth of yours can help me unwind?"
                        
                    menu:
                        "Follow her right now":
                          
                            if gender == "male":
                                club "Atta boy."
                            else:
                                club "Atta girl."
                            scene black with dissolve
                            "She tugs me by the wrist toward the emergency-exit hallway."
                            jump bouncer_round2


                        "Decline (for now)":
                            name "Not tonight."
                            "She shrugs, but her eyes linger."
                            club "Sure, maybe next time.."
                            "She walks off, the crowd parting for her like water."
                            jump clubalone_loop





                elif clubalone_drink_count == 3:
                    scene nightdate_barmanscene with dissolve
                    name "One more."
                    "The bartender raises an eyebrow."
                    club "Slow night?"
                    name "Slow start. I wait for someone."
                    club "It gets better after midnight."
                    "He slides the drink over."
                elif clubalone_drink_count >= 4:
                    scene nightdate_barmanscene with dissolve
                    "I think I should pace myself."
    
                scene black with dissolve
                jump clubalone_loop


            "Go to the bathroom":
                $ clubalone_bathroom_count += 1
                scene chloedate_bathroom with dissolve
                "I slip through the crowd. The hallway’s cooler. Quieter."
                "Mirror. Water. Deep breath."
                "I fix my hair. Loosen my collar."
            
                "I splash water on my neck."
                "I wait a beat. Then head back."

                jump clubalone_loop


            "Talk to someone nearby":
                $ clubalone_talk_count += 1

                if clubalone_talk_count == 1:
                    "I turn to the girl sitting alone two stools down."
                    "She’s sketching on a napkin with a pen she definitely stole."
                    name "That the DJ?"
                    "She looks up. Smiles."
                    club "Nah. Just doodling. Helps me think."
                    name "Looks like a dragon wearing headphones."
                    club "Exactly. He’s dropping fire tonight."
                    "She laughs. Goes back to drawing."
                    "I don’t push."

                elif clubalone_talk_count == 2:
                    "A guy in a leather jacket leans against the wall, smoking an e-cig."
                    name "Mind if I stand here? Need a break from the bass."
                    club "All yours. Best spot for people watching."
                    name "And avoiding the dance floor?"
                    club "Got it in one. Need better music first."
                   
                    club "You here with someone?"
                    name "Just me tonight."
                    club "Wow that's brave... or stupid."
                    name "I am not sure yet"

                elif clubalone_talk_count == 3:
                    "Three friends are taking selfies near the mirror wall."
                    "One of them catches my eye in the reflection."
                    club "Hey, you look familiar. Been here before?"
                    name "Yeah, last week. I was with a girl named Rose."
                    club "Wait, tall, black hair, moves like she owns the place?"
                    name "That's her."
                    club "Oh my god, I totally know who you mean!"
                    club "Watch out, she is wild.."
                    name "Yeah, I know."
                    "The three friends exchange knowing looks."
                    club "Want to join our photo?"
                    name "Thanks, but I'll pass. Still recovering from last time."
                    "They laugh. One raises her glass in a mock salute."
                    "I smile, but my mind drifts to Rose. Is she here tonight?"

                else:
                    "I glance around. No one new to talk to."
                    "Maybe it’s time to move."

                jump clubalone_loop


            "Go dance" if clubalone_drink_count >= 2 and clubalone_dance_count == 0:
                $ clubalone_dance_count += 1
                scene black with dissolve
                "I down the rest of my drink."
                "The beat shifts. It's slower now, heavier."
                "I step onto the floor."
                "Lights pulse. Bodies move all around me."
                "I close my eyes. I let the rhythm take over."
                "No one’s watching. No one cares."
                "Just motion. Heat. Sound."
               

                "I dance until my shirt sticks to my back."
                

                jump dancingandmeettingrose

            "Leave the club" if clubalone_drink_count >= 1:
                "I finish my drink."
                "The night’s not what I expected."
                "But it wasn’t bad."
               
                scene black with dissolve
                "I step outside. The air feels clean."
                "I walk home under streetlights."
                "Smiling."
                jump quickgotobed


        jump clubalone_loop


    label bouncer_round2:
                                    
                                    club "On your knees."
                                    scene black with dissolve
                                    window hide 
                                    pause
                                    play sound pantdown volume 1 noloop
                                    scene nightdate_bouncersscene4 with dissolve
                                    "I drop. The floor is cold."
                                    "She unzips — she's half-hard and raring to go."
                                    "She holds the phone up like a trophy, speaker on."
                                    
                                  
                                    play background suckslowv1 volume 1 loop
                                    "She slides into my mouth, slow, deliberate."
                                    scene nightdate_bouncersscene5 with dissolve
                                    "I take her in, salty, warm, tasting of leather and smoke."
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    "The bouncer grips my hair, guiding."
                                   
                                    
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    club "Fuuck... you really like that don't you?"
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause

                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    "She groans low, hips rocking slow and steady against my mouth."
                                    scene nightdate_bouncersscene4 with dissolve

                                    if gender == "male":
                                        club "Fuck… good boy."
                                    else:
                                        club "Fuck… good girl."
                                    scene nightdate_bouncersscene7 with dissolve
                                    "Her hand tightens in my hair. One last deep thrust."
                                    "She comes with a low grunt, hot and thick across my tongue."
                                    scene nightdate_bouncersscenefinal with dissolve
                                    "I swallow instinctively, throat working, eyes watering."
                                
                                    "Her smirk is lazy, satisfied."
                                
                                    club "Wow.. thanks love..."
                                    club "See you around."
                                   
                                    "I stand on shaky legs, wipe my mouth with the back of my hand."
                                    "The taste of her lingers—salt, smoke, and something darkly addictive."
                                    scene black with dissolve
                                    "I slip back into the club, lips swollen, pulse racing, head spinning."
                                    jump clubalone_loop