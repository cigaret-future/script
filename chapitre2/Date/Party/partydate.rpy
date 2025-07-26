label partydate:
    
        scene black with dissolve
        "I eat dinner thinking about the party ahead."
        z_nvl "Hey I have sent you the address"
        z_nvl "See you there!"
        nvl clear
        scene black with dissolve
        pause 1.0
        "I quickly get dressed and prepare myself for the party."
        "I check my appearance in the mirror one last time before heading out."
        "I grab my phone and wallet, then head out the door."
        scene ericgoingout with dissolve
        pause 0.5
        "the night is warm and the streets are lively."
        scene entryparty with dissolve
        "After a short walk through the city streets, I arrive at the party location."
        "The music is already pumping from inside, and I can see people entering the building."
        scene black with dissolve
        "I take a deep breath and ring the doorbell."
        scene entry4 with dissolve
        "The door opens and I'm greeted by the warm glow of lights and the sound of laughter."
        "I step inside and am immediately hit by the energy of the party."
        "People are chatting, dancing, and having a good time all around me."
        "I look around to see if I can spot any familiar faces."
        show screen vestibulescreen
        call screen vestibulescreen

label partyending:
        scene black with dissolve
        $ party_started = False
        "The party is coming to an end..."
        "Everyone is starting to leave little by little."
        "A few people who are too drunk have fallen asleep on the couch."
        "I should go."
        scene endpartydoor with dissolve
        "I walk towards the door, but I hear a voice behind me."
        if zoey_date_done == True and isabelle_date_done == False:
                jump zoeypartyend
        elif isabelle_date_done == True and zoey_date_done == False:
                jump isabelleend
        elif isabelle_date_done == True and zoey_date_done == True:
                jump isabellezoeyend
        

label zoeypartyend:
        scene endpartydoor with dissolve
        show zoeysmile with dissolve
        "As I step through the door, Zoey grabs my arm firmly, her warm fingers tightening around my skin."
        zoey "Come on, I'm taking you home..."
        zoey "No way I'm letting you go back alone in this state."  

        name "I haven’t drunk that much..."  
        show zoeysurprise with dissolve
        hide zoeysmile with dissolve
        zoey "Oh really?"  
        zoey "You can barely walk straight."  
        zoey "You look like you’re about to collapse any second now." 
        show zoeysmile with dissolve
        hide zoeysurprise with dissolve
        "she whispers in my ear"  
        zoey "Probably because you were too busy greedily taking my cock earlier.."  
        zoey "Nope, you’re definitely coming with me."
        jump zoeycominghomeafterparty 
    
    

label isabelleend:
        scene endpartydoor with dissolve
        show isav21 with dissolve 
        "As I start to leave, Isabelle catches up with me at the door."

        isa"Hey, wait up!"
        isa "You're not seriously thinking of walking home alone this late, are you?"

        name "I'll be fine, really..."
        isa "Look at you, you can barely stand upright."
        isa "Plus it's really late and the streets aren't safe."

        isa "Come on, let get you home."
        name "Are you sure? I don't want to be a bother..."

        isa "Don't be silly, it's no trouble at all."
        isa "I would be an asshole not to help you."
        scene leavingpartywithisa
        "Isabelle takes me by the arm and leads me down the stairs to the street."
        "We walk slowly through the quiet streets, Isabelle's arm wrapped around me for support."
        "The cool night air feels refreshing after the stuffy atmosphere of the party."
        "Our footsteps echo softly on the empty sidewalk."
        scene isabelleerichome
        "After walking through the streets for a while, we finally arrive at my place."
        isa "Here we are."
        name "Thanks for walking me home, Isabelle."
        isa "No problem.."
        isa "It was fun tonight, I hope you had a good time."
        name "Yeah, it was great."
        isa "Good night, see you around."
        name "Good night, Isabelle."
        scene black
        scene sleeping3e with dissolve
        "I lay on my bed and fall asleep instantly" 
        
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
        "The next day, I wake up a headache"
        if day % 7 == 0:
                jump rentdue
        show screen homescreen4
        call screen homescreen4


label isabellezoeyend:
        scene endpartydoor with dissolve
        show zoeysmile at Position(xalign=0.8, yalign=0.99) with dissolve
        show isav21 at Position(xalign=0.8, yalign=0.99) with dissolve
            
        "As I reach for the door handle, both Zoey and Isabelle appear on either side of me."

        zoey "Where do you think you're going?"
        isa "You're not walking home alone in this condition."

        name "I'm fine, really. You don't need to worry about me."

        zoey "Fine? You can barely keep your eyes open."
        isa "Zoey's right. You need someone to make sure you get home safely."
        show zoeylookingleft at Position(xalign=0.8, yalign=0.99) with dissolve
        hide zoeysmile with dissolve
        show isalookright at Position(xalign=0.8, yalign=0.99) with dissolve
        hide isav21 with dissolve
        "The two girls exchange a look over my head."

        zoey "I'll take him home."
        isa "Actually, we were about to leave together."
        show zoeyangry at Position(xalign=0.8, yalign=0.99) with dissolve
        hide zoeylookingleft with dissolve
        zoey "Back off.. I am the one who brought him here, so I will take him back."
        zoey "I know him better, and I care about his well-being."
        isa "I know him too, Zoey."
        zoey "Just because he sucked your dick in the toilet doesn't mean you know him.."
        "I blush a little, people around start looking at us.."
        zoey "You should just let me handle this."
        hide isalookright with dissolve
        show isalookleft at Position(xalign=0.8, yalign=0.99) with dissolve
        
        isa "Yeah whatever.. I am not gonna make a drama about this"
        "Isabelle rolls her eyes, clearly annoyed by Zoey's assertiveness."
        isa "See you later then."
        name "Bye Isabelle."
        zoey "Yeah, see you later."
        jump zoeycominghomeafterparty



label zoeycominghomeafterparty:
        scene black with dissolve
        "Zoey takes my arm and leads me out of the apartment, her grip firm but gentle."
        
        scene leavingpartywithzoey with dissolve
        "As we step into the cool night air, I feel a mix of gratitude and confusion."
        if isabelle_date_done == True:
                "The fact that she knows I went down on Isabelle makes me a bit nervous."
        "But she seems convinced that I belong to her."
        "We walk slowly through the quiet streets, Zoey's arm wrapped around me for support."
        "The cool night air feels refreshing after the stuffy atmosphere of the party."
        "Our footsteps echo softly on the empty sidewalk."
        scene black with dissolve
        "After walking through the streets for a while, we finally arrive at my place."
        "Zoey climbs the stairs with me and helps me into the apartment."
        "I sit heavily on the bed, exhausted."
        scene zoeyerichome
        zoey "There you go, home sweet home."
        zoey "It was a fun night"
        zoey "I hope we'll do it again sometime."
        name "Yeah me too."
        zoey "I'll let you rest."
        zoey "See you later."
        name "alright."
        zoey "good night babe"
        name "good night.."
        scene sleeping3e with dissolve
        "I lay on my bed and fall asleep instantly" 
        
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
        "The next day, I wake up a headache"
        if day % 7 == 0:
                jump rentdue
        show screen homescreen4
        call screen homescreen4


label endpartydrink10:
        scene black with dissolve
        "Suddenly everything becomes blurry..."
        "I feel myself losing consciousness as the alcohol takes over."
        "The last thing I remember is someone helping me to a quiet room..."
        
        scene black
        pause 2.0
        
        "My head is pounding..."
        "Where am I?"
        
        scene unknownbedroom with dissolve
        "I slowly open my eyes and find myself in an unfamiliar bedroom."
        "The sunlight filters through curtains I don't recognize."
        scene unknownbedroom2 with dissolve
        "This isn't my room..."
        "I try to piece together what happened last night, but my memory is fuzzy."
        
        "I hear footsteps approaching."
        
        scene unknownbedroom3 with dissolve

        jeni "Oh! You're awake!"
        jeni "Good morning..."
        scene jennsayhi2 with dissolve
        name "What... where am I?"
        "I sit up slowly, still feeling a bit dizzy."
        "I take a moment to look around the room - it's cozy and well-organized."
        "Jennifer looks at me with concern, her eyes soft and caring."
        jeni "You're in my room. You were really drunk last night and I..."
        jeni "I couldn't just leave you there, so I brought you here."
        name "Oh ok... thanks.."
        
       
        
        jeni "I just wanted to make sure you were ok."
        
    
        
        name "Thank you. That's really kind of you."
        
        jeni "I... I hope you don't mind. I know we don't know each other that well."
        jeni "But I saw you struggling so I thought I could help."
        name "I really appreciate it."
        "It seems a bit strange to me that Zoey or Hugo didn't help me..."

        jeni "How are you feeling?"
        name "A bit better, I think."
        name "I should probably get going..."
        jeni "Oh, are you sure?"
        name "Yeaah.."
        scene jennsayhi3 with dissolve
        name "Thanks for the help!"
        name "See you..."
        jeni "Oh ok.. bye then.."
        "I get up and gather my things, still feeling a bit disoriented."
        $ zoey_relation_status_text = "I think I missed my chance with Zoey"
        $ party_started = False
        $ Jenny_end_done = True
        scene black with dissolve
        window hide 
        pause
        jump map3
        
        # menu:
        #     "Accept the coffee":
        #         name "That sounds perfect, thank you."
        #         jenny "I'll be right back!"
        #         hide jennifer_smile with dissolve
        #         "She hurries out of the room, and I can hear her moving around in what I assume is the kitchen."
        #         "I take a moment to look around the room - it's cozy and well-organized."
        #         "There are books scattered around and some plants by the window."
        #         show jennifer_coffee with dissolve
        #         jenny "Here you go."
        #         "She hands me a steaming mug, our fingers brushing briefly."
        #         name "This is really good, thank you."
        #         jenny "I'm glad you like it."
                
        #     "Politely decline":
        #         name "That's very sweet, but I should really head home."
        #         show jennifer_disappointed with dissolve
        #         hide jennifer_smile
        #         jenny "Oh... okay, I understand."
        #         jenny "Let me at least call you a taxi."
        #         name "You don't have to do that."
        #         jenny "I insist. It's the least I can do."
        
        # jenny "Last night was... interesting."
        # jenny "I mean, taking care of you. I don't usually do things like that."
        
        # name "Well, I'm grateful you did."
        
        # jenny "Maybe... maybe we could hang out sometime? When you're not drunk, I mean."
        # "She laughs nervously, fidgeting with her hands."
        
        # name "I'd like that, Jennifer."
        
        # show jennifer_happy with dissolve
        # jenny "Really? That's... that's great!"
        
        # scene black with dissolve
        # "After finishing the coffee and getting my things together, I prepare to leave."
        # "Jennifer walks me to the door, still in her oversized t-shirt."
        
        # jenny "Take care of yourself, okay?"
        # name "I will. And thank you again for everything."
        # jenny "It was nothing... well, it was something to me."
        
        # "I head home, thinking about Jennifer's kindness and wondering what might develop between us."
        
        # $ jennifer_encountered = True
        # $ day += 1
        
        # scene home00 with dissolve
        # "I arrive home with a clearer head and a new perspective on the night."
        show screen homescreen4
        call screen homescreen4