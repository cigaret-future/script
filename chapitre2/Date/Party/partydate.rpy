label partydate:
    scene entryparty
    
    
    "test"
    scene entry4
    "test"
    show screen vestibulescreen
    call screen vestibulescreen

label partyending:
    scene black with dissolve
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
    zoey "Probably because you were too busy greedily taking my cock earlier~"  
    zoey "Nope, you’re definitely staying with me tonight."  
    "je la laisse me racompagner."
    

label isabelleend:
    scene endpartydoor with dissolve
    show isav21 with dissolve 
    "As I start to leave, Isabelle catches up with me at the door."

    isa"Hey, wait up!"
    isa "You're not seriously thinking of walking home alone this late, are you?"

    name "I'll be fine, really..."
    isa "Look at you, you can barely stand upright."
    isa "Plus it's getting really late and the streets aren't safe."

    isa "Come on, let get you home."
    name "Are you sure? I don't want to be a bother..."

    isa "Don't be silly, it's no trouble at all."
    isa "I would be an asshole not to help you."
    scene black
    "Isabelle takes me by the arm and leads me down the stairs to the street."
    "We walk slowly through the quiet streets, Isabelle's arm wrapped around me for support."
    "The cool night air feels refreshing after the stuffy atmosphere of the party."
    "Our footsteps echo softly on the empty sidewalk."
    scene black


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
    scene black with dissolve
    "Zoey takes my arm and leads me out of the apartment, her grip firm but gentle."
    scene leavingpartywithzoey with dissolve
    "As we step into the cool night air, I feel a mix of gratitude and confusion."
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
    zoey "Je te laisse te reposer."
    zoey "On se voit plus tard."
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