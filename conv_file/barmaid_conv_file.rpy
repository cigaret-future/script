label BarmaidSarah:
    scene cafesarah
    show barmaidneutral

    lau "Hey, I might not look like it, but I'm actually working right now, so just tell me what you want."
    menu: 
        "I'd like a coffee.": 
            lau "I'll bring it to you."
        
            scene smallcoffe
            show text "-3$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) with dissolve
            hide text with dissolve
            $ money -= 3 
            "Always nice to kick back and enjoy a coffee." 
            "It's something we tend to overlook these days."
            jump cafedirection

        "I'm just looking around.": 

            hide barmaidneutral
            show barmaidpissed
            lau "Don't do anything stupid, alright? I'm watching you."
            hide barmaidpissed with dissolve
            ""
            jump cafedirection 
        "I'm looking for a job." if jobaskedlaura_done == False:
            name "Hey, I just arrived and I'm a bit short on money."
            name "I'd like to work alongside my studies."
            name "Do you need someone extra here?"
            
            lau "Good for you, but we don't need any staff at the moment."
            name "Damn, I would have loved to work here."
            name "It seems chill."
            lau "What, you think I just sit around doing nothing?"
            name "No, no, I didn't mean that."
            lau "That's what you said."
            lau "Anyway, we don't need anyone here, but I can ask my boss."
            lau "She owns several bars and is probably looking for people."
            name "Oh really? That would be great."
            lau "Yeah, 'great,' as you say..."
            lau "I can give her your number."
            name "Yes, that works."
            name "Thank you so much!"
            lau "You're welcome."
            lau "She'll contact you soon."
            $ jobaskedlaura_done = True
            jump cafedirection

label Barmaid3:
    scene slep
    name "Hello? Is the coffee shop closed?"
    
    lau "rrrrrh..."

    name "The door was open so I came in."

    lau "Mh huh??... Oh shit... Yeah yeah we are open... Give me a minute."
    show screen cafescreen_sleepylaura
    call screen cafescreen_sleepylaura

label Barmaid4: 
    scene slep2
    lau "What do you want?"

    name "Coffee please."

    lau "Sure."
    show text "-3$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) with dissolve
    hide text with dissolve
    $ money -= 3 

    name "Were you... sleeping?"

    lau "Me? No, I wouldn't do that."

    name "Oh, okay, cool."
    scene smallcoffe
    
    "Always nice to kick back and enjoy a coffee."
    
    "It's something we tend to overlook these days."

    $ laura_count += 1

    show screen cafescreen_sleepylaura
    call screen cafescreen_sleepylaura

label Barmaid5: 
    if laura_count >= 2:
        scene slep3
        name "She is still sleeping..."
      
        name "Doesn't she worry about someone coming in and stealing something?"
        
        show screen cafescreen_laura_backtobed
        call screen cafescreen_laura_backtobed
    else: 
        scene slep3
        name "..."
        name "You... went back to sleep?"
    
        lau "rrrh"

        name "I'll come back later, I guess..."
        $ laura_count += 1
        show screen cafescreen_laura_backtobed
        call screen cafescreen_laura_backtobed

label Barmaid2:
    if laura_repeat == True:
        if elise_cafe == True and elise_cafe_conv_done == False:
            scene cafeelisefinal
        elif sarah_cafe == True and sarahcafe_conv2_done == False:
            scene cafesarah2
        elif sarah_elise_cafe == True and sarah_elise_cafedate_done == False:
            scene elisesarahcafe
        else:
            scene cafe2
            
        show barmaidneutral with dissolve

        lau "Hey, I might not look like it, but I'm actually working right now, so just tell me what you want."
        menu: 
            "I'd like a coffee.": 
                lau "I'll bring it to you."

                scene smallcoffe
                show text "-3$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) with dissolve
                hide text with dissolve
                $ money -= 3 
                "Always nice to kick back and enjoy a coffee."
                
                "It's something we tend to overlook these days."
                
                "Maybe I could text someone."
                menu: 
                    "Elise" if elise_sdate_done == True and elise_sagain_done == False:
                        "Maybe I should text Elise."
                        n_nvl "Hey, I'm at the coffee shop, can I come to your place?"
                        el_nvl "Sure, come over."
                        el_nvl "I was wondering when you'd ask."
                        nvl clear
                        scene black
                        "I leave the coffee shop and head toward Elise's place." 
                        jump elise_sdate
                    "Sarah" if sarah_sdate_done == True and sarah_sagain_done == False:
                        "Maybe I should text Sarah."
                        n_nvl "Hey, can I visit you tonight?"
                        s_nvl "Of course."
                        s_nvl "I can't wait to see you."
                        nvl clear
                        $ sarah_sagain_done = True
                        $ sarah_conv_done = True

                        jump map3
                    "Just drink my coffee.":
                        ""
                jump cafedirection

            "I'm just looking around.": 
                hide barmaidneutral
                show barmaidpissed
                lau "Don't do anything stupid, alright? I'm watching you."
                hide barmaidpissed with dissolve
                jump cafedirection
            "I'm looking for a job." if jobaskedlaura_done == False:
                
                    name "Hey, I just arrived and I'm a bit short on money."
                    name "I'd like to work alongside my studies."
                    name "Do you need someone extra here?"
                    
                    lau "Good for you, but we don't need any staff at the moment."
                    name "Damn, I would have loved to work here."
                    name "It seems chill."
                    lau "What, you think I just sit around doing nothing?"
                    name "No, no, I didn't mean that."
                    lau "That's what you said."
                    lau "Anyway, we don't need anyone here, but I can ask my boss."
                    lau "She owns several bars and is probably looking for people."
                    name "Oh really? That would be great."
                    lau "Yeah, 'great,' as you say..."
                    lau "I can give her your number."
                    name "Yes, that works."
                    name "Thank you so much!"
                    lau "You're welcome."
                    lau "She'll contact you soon."
                    $ quickbed_disabled = True
                    $ jobaskedlaura_done = True
                    jump cafedirection
               
    else:
        if elise_cafe == True and elise_cafe_conv_done == False:
            scene cafeelisefinal
        elif sarah_cafe == True and sarahcafe_conv2_done == False:
            scene cafesarah2
        elif sarah_elise_cafe == True and sarah_elise_cafedate_done == False:
            scene elisesarahcafe
        else:
            scene cafe2

        show barmaidneutral with dissolve
        
        "The waitress looks tired, like she's about to fall asleep." 
        "She's pretty though."

    lau "Hi, what can I get for you?"

    name "Hello, I just moved into the neighborhood, I live right nearby. Do you serve anything special here?"

    lau "Not really, mostly just coffee and alcohol in the evenings."

    name "Ah, too bad. I'll just have a coffee then."

    lau "Sure."

    name "Do you have any special coffees?"

    hide barmaidneutral 

    show barmaidpissed

    lau "...?"

    lau "Special coffee?"

    name "You know, something that ends with the letter 'o'? Or with some expensive milk?"

    lau "You want milk in your coffee?"

    name "Oh yes, great."

    hide barmaidpissed 

    show barmaidsleep

    lau "(sigh)"

    lau "Alright, have a seat."

    hide barmaidsleep 

    "I take a seat at an empty table."
    "She doesn't seem too thrilled to be working here. But she seems nice." 
    "There are several young people in the coffee shop, probably students or young professionals." 
    "I'm excited to be a young professional too. These holidays have refreshed me;" 
    "I hope this year goes well."
 
    show barmaidneutral with dissolve

    lau "One latte."
    show text "-3$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) with dissolve
    hide text with dissolve
    $ money -= 3 
    "She casually places the cup on the table."

    name "Thanks. How long have you been working here?"

    hide barmaidneutral

    show barmaidtired3

    lau "Too long. I do this alongside my studies."

    name "Oh, you're also in college? Cool! What are you studying?"

    lau "Geography."

    name "Nice! I'm studying art history. Maybe we'll bump into each other."

    hide barmaidtired3

    show barmaidsmug

    lau "I doubt it."

    name "Ah, you're probably in a different part of the building."

    lau "Yeah, that's it, I'm in a different building."

    lau "Plus, I mostly work from home, and I gotta be here for my shift."

    name "Alright, I'll see you around here then."

    lau "Sure."

    lau "If you've bought something, feel free to hang out in the coffee shop."

    hide barmaidsmug

    "She returns behind the bar to wash some glasses. I think she kinda likes me."

    $ laura_repeat = True
    jump cafedirection
