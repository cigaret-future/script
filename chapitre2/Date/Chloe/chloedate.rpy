define jul = Character('Julia', color="#ff7f7f")
define ros = Character('Rose', color="#d1c5c5")
label raver_date_0:
    "Chloe probably won't be available tonight, i should try another time"
    jump gotobed

label raver_date_1:

    "Perhaps I should send Chloe a message."
    "She might have something planned for tonight."
    "We don’t know each other that well, but she did seem nice."

    "Alright, let's go for it."

    n_nvl "Hi, it's [name]. We met at the coffee shop recently. Not sure if you recall."

    n_nvl "I wanted to ask if you were free tonight."

    n_nvl "I just need to clear my head a bit."

    c_nvl "Oh, hi! Yeah, I remember, and funnily enough, I do have plans tonight."

    n_nvl "Oh, for real? That’s great!"

    c_nvl "I’ll text you the address. See you in 30 minutes."

    n_nvl "Alright, see you shortly."

    "Well, that was quick. Looks like I’m going out."
    if gender == "fem" and characterdesign_done == False:
        scene characterdesign2
        window hide
        pause
        menu:
            "continue":
                pass
            "Don't show me that message again":
                $ characterdesign_done = True
                pass
    scene outbuilding eric
    "I get dressed and head outside."

    "It's a bit far, so I'll have to take the metro."

    "I’m feeling a bit anxious."

    "I suppose that’s to be expected."

    scene subway
    "What’s the worst that could happen?"

    "Worst case, I’ll wake up tomorrow with a hangover at the coffee shop next door."

    "After changing subway lines a few times, I finally arrive at the spot."
    scene subwayouteric
    "The neighborhood is pretty quiet, with only the noise of a crowd in front of an alley bringing life to the street."

    n_nvl "Hey, where are you? I’ve arrived."

    c_nvl "Head to the front, you’ll see me."

    "I spot Chloe emerging from the alley."

    scene clubviewericpigine
    "She waves at me."

    rav "Hey, how’s it going?"

    name "Good, thanks!"

    rav "Follow me, my friend’s already inside."

    name "Where are you taking me?"

    rav "Don’t worry, it’s actually a pretty popular place."
    scene clubview5
    rav "I didn’t want to scare you off right away."

    name "Thanks, haha. Honestly, I’m not really used to this."

    rav "It’s not as underground as it seems."

    rav "A lot of software engineers and CEOs come here, but it’s a good place to dance without worrying too much."
    scene clubview2
    rav "Wow, there weren’t this many people when I stepped out earlier."

    name "There aren't that many people. It shouldn’t take too long."

    rav "Nah, come on."

    "Chloe moves past the crowd toward the bouncer."

    "He sees her and seems fine with letting her cut in front of everyone."

    name "Wow, he let us through just like that?"

    rav "We’re in the same yoga class."

    name "Haha, looks like you’re not just anyone."
    scene goingdownstairs
    "Loud music blares from the club, making the floor vibrate."

    "I catch sight of a crowd dancing frenetically on the dance floor."

    "A mix of sweat and plastic immediately fills my head."

    "We head downstairs and walk toward a sofa where a girl is sitting."
    scene talking2
    jul "Hey! Finally, where have you two been?"

    if gender == "male":
        jul "So, are you the guy trying to lose his innocence tonight?"
    elif gender == "fem":
        jul "So, are you the girl trying to lose her innocence tonight?"

    name "Uh, I guess so?"

    rav "No, no, we’re just helping him get familiar with the city, haha. You’ve got it all wrong."

    if gender == "male":
        rav "Don’t go corrupting him!"
    elif gender == "fem":
        rav "Don't go corrupting her!"

    jul "Then why did you bring him here?"

    jul "Want something to drink? I’m heading to the bar."

    name "Sure."

    jul "What’ll it be?"

    name "Whatever you're having."

    jul "Got it."

    scene talkingeric

    "I sit down on the sofa with Chloe."

    rav "Watch out for Julia, she’s a bit of a party animal."

    rav "I feel like I have to tell you."

    rav "She is horny as hell."

    name "Oh ok, thanks for the heads up."

    name "She is pretty."

    name "I wouldn't mind."

    rav "She will be glad to hear that."

    name "Hey, don't tell her I said that!"

    rav "I won't have to, ahah."

    rav "She will know."

    rav "Maybe try not to drink too much."

    name "Coming from you, an expert in that domain."

    rav "Yeah... I will try to keep it low tonight."

    name "I won't be available to pick up what's left of you tomorrow."

    name "So yeah, it's probably for the best."

    rav "Don't get too cocky."

    rav "I'll probably be the one paying for your hangover coffee tomorrow."

    name "Ahah."
    name "Maybe that's what I wanted."

    name "When I saw you dying at the coffee shop, I was like: I want to feel that."

    rav "Don't worry, I'll make sure you get your money's worth."

    rav "By the way, I am gonna look for Julia. She has probably forgotten about us."
    name "Hey, don't leave me hanging there."

    rav "I'll be back in a sec."
    "Chloe gets up and heads to the bar."

    scene eric alone
    "I sit alone on the banquette, the vibrant energy of the club enveloping me."
    "The rhythmic beats resonate within my body, matching the rapid pace of my heart."   

    scene sitting kate
    "In the throbbing heartbeat of the club, a sultry voice cuts through the din."
    ros "Can I sit here?"
    "She asks, her tone melodic and inviting." 
    name "Yeah, sure."
    "She puts two drinks on the table and sits down next to me."
    "Though her features remain partially hidden in the shadows, there's an undeniable allure about her." 
    "A raw sensuality that seems to emanate from every pore."

    scene ericwithkate
    ros "I am waiting for a friend."

    ros "You seem a little lost. Did you come here alone?"
    name "No, I am with a friend too."
    name "She went to the bar."

    ros "Oh ok."
    ros "Do you want a drink?"
    ros "I have two."
    name "I don't want to take your friend's drink."
    ros "Don't worry, just drink it."
    "She pushes one of the glasses towards me."
    name "Ok, thanks."
    "I take the glass and take a sip."
    "The liquid burns my throat."
    "The drink has a strange taste, a mix of sweet and spicy."
    "Suddenly, the liquor hits me, making me cough."
    "The tall girl laughs."
    ros "You don't seem to be used to it."
    "I can't quite place it, but it's not unpleasant."
    "I take another sip, feeling the warmth of the alcohol spread through my body."
    ros "Is it good?"
    name "Yeah, it's good."
    "The music seems to grow louder, the lights brighter."
    ros "You seem a little nervous."
    ros "Do you want to dance?"
    name "I'm not really a dancer."
    ros "Come on, it's easy."
    ros "Finish your drink and follow me."

    scene kate take eric
    "She takes my hand and pulls me to the dance floor."
    scene dancing2
    "I follow her lead, my body moving in time with the music."
    scene dancingtwo
    "As we sway to the rhythm of the music, she draws closer, her body almost touching mine." 
    "I can feel the warmth of her body drawing nearer. I catch a whiff of her sweat." 
    scene handonhip eric
    "Without warning, her hand finds my hip, guiding it to move in sync with hers."

    scene closeup
    "I feel her breath on my neck, her body pressing against mine."
    scene blurtotal
    "My head is spinning, the music and lights blending into a blur of color and sound."
    scene black
    pause
    scene katecar
    "I come to my senses, my head pounding."
    ros "Hey, are you okay?"
    ros "Do you want to have a little fun?"
    menu : 
        "Yes (i know where is this going)":
            jump rosefun

        "I'd rather go home":
            jump rosegohome
    label rosegohome:
        scene black
        "I shake my head and mumble something about needing to go home."
        ros "alright, let's drive you home"
        scene black
        "As she drives my senses slowly return to me."
        name "It's here!"
        scene endkatecar with dissolve
        "She stops the car in front of my building."
        "I get out and make my way inside."
        jump gotobed
    label rosefun:
        scene black
        "Slowly, I come to my senses. I blink several times, trying to clear my vision."    

        scene firstperson2 with dissolve
        play music "audio/music/suck+fast+v1.wav"
        "As my senses return to me, I become aware of the strange, musky scent surrounding me."
        scene firstperson1 with dissolve
        "Something large and hard is pressing against my lips."
        scene mouthangle000 with dissolve
        "I think I'm sucking a dick."
        scene mouthangle001 with dissolve
        "I feel her precum on my tongue, the salty taste invades my taste buds."
        scene mouthangle002 with dissolve

        scene mouthangle003 with dissolve
        pause
        scene anglelarge000 with dissolve
        "This isn't what I expected tonight, but here I am, my mouth filled with a throbbing cock."
        scene anglelarge001 with dissolve
        "I struggle to regain my senses, trying to comprehend how I ended up here." 
        scene anglelarge002 with dissolve 
        "But the taste of her precum overwhelms my mouth, clouding my thoughts."
        scene anglelarge003 with dissolve
        "My lips obediently suckle on her penis."
        scene anglelarge002 with dissolve
        pause
        window hide
        scene anglelarge001 with dissolve

        scene anglelarge000 with dissolve
        pause
        "I am completely under her control."
        scene angletight003 with dissolve
        "I attempt to speak, but only a garbled sound comes out."
        name "Mmggh"
        scene angletight002 with dissolve
        ros "Shht, just suck it."
        scene angletight001 with dissolve
        pause
        scene angletight000 with dissolve
        ros "That's it."
        scene shoulderangle003 with dissolve
        ros "Hm, your mouth feels so good."
        scene shoulderangle002 with dissolve
        "Her voice dripping with lust."
        # SHOULER
        scene shoulderangle001 with dissolve
        "As I suck her dick, the realization dawns on me that she brought me here in her car."
        scene shoulderangle000 with dissolve
        ros "You like that?"
        scene shoulderangle001 with dissolve
        ros "I knew you would suck like a pro."
        scene shoulderangle002 with dissolve
        pause
        window hide
        scene shoulderangle001 with dissolve
        pause
        scene shoulderangle002 with dissolve
        pause
        scene shoulderangle001 with dissolve

        "I recall that Chloe might be searching for me at the club."
        # MOUTH WET
        scene mouthanglewet001 with dissolve
        "The thought crosses my mind, adding a touch of anxiety to the already intense situation."

        scene mouthanglewet002 with dissolve
        pause
        scene mouthanglewet001 with dissolve
        "Yet, I find myself unable to do anything other than suck her dick, as if possessed by her."
        scene mouthanglewet002 with dissolve
        ros "That's it, baby."
        scene mouthanglewet001 with dissolve
        ros "You are such an obedient little slut."
        scene mouthanglewet002 with dissolve
        "Her desire to fuck my mouth is palpable, evident in the firm grip she maintains on my head, guiding my motions."

        scene mouthanglewet001 with dissolve
        "Seeing my compliance, she pushes her massive member deeper into my mouth."
        scene feetangle003 with dissolve
        "Making me gag on it."

        scene feetangle005 with dissolve
        ros "Oh fuck."
        scene feetangle004 with dissolve
        "She forces my head down onto her cock, disregarding my gag reflex entirely."
        scene feetangle005 with dissolve
        scene feetangle004 with dissolve
        scene feetangle005 with dissolve
        scene feetangle004 with dissolve
        scene feetangle005 with dissolve

        "I attempt to regain control, slowing her aggressive pace."
        stop music 
        play music "audio/music/suck+fast+v2.wav"
        pause
        scene feetangle004 with dissolve
        pause
        scene deepthroat003 with dissolve
        pause
        scene deepthroat004 with dissolve
        "Slowly, my mouth accommodates her large length."
        scene deepthroat003 with dissolve
        pause
        scene deepthroat004 with dissolve
        pause
        window hide

        scene deepthroat003 with dissolve

        pause
        scene deepthroat004 with dissolve
        "Sensing her growing frustration, she presses harder, causing me to gag in a slutty manner."
        scene deepthroat005 with dissolve
        pause
        scene deepthroat004 with dissolve
        ros "I am gonna fill your mouth so bad."
        scene deepthroat005 with dissolve

        scene deepthroat004 with dissolve

        scene sideangle003 with dissolve
        ros "I can tell that's what you need."
        scene sideangle004 with dissolve
        pause
        scene sideangle003 with dissolve
        pause
        scene sideangle005 with dissolve
        ros "I hope you like cum."
        scene sideangle003 with dissolve
        ros "Either way, I'm going to teach you to love it."
        scene sideangle005 with dissolve
        pause
        scene sideangle003 with dissolve
        "As she ravishes my mouth, I begin to accept my role, growing accustomed to her thick shaft occupying my mouth."
        scene deepthroatbis003 with dissolve
        pause
        scene deepthroatbis004 with dissolve
        pause
            
        
        scene deepthroatbis003 with dissolve
        ros "That's it, take it like the whore you are" 

        scene deepthroatbis005 with dissolve
        pause
        scene deepthroatbis003 with dissolve
        ros "oh fuck, I am gonna cum"
        scene deepthroatbis005 with dissolve
        pause
        scene deepthroatbis003 with dissolve
        scene deepthroatbis005 with dissolve
        pause
        scene deepthroatbis003 with dissolve
        ros "fuuuck"
        stop music    
        
        scene cs007 with dissolve
        "With a final, forceful thrust, she buries herself deep in my throat." 
        
        scene cs005 with dissolve
        play sound "audio/music/swallow1.wav"
        "A flood of warm, salty liquid fills my mouth and my throat ,"
        scene cs008 with dissolve
        play sound "audio/music/swallow2.wav"
        "the taste of her essence coating my tongue."
        play sound "audio/music/swallows1.mp3"
        play sound "audio/music/slurpswallow.mp3"
        scene cs005 with dissolve
        pause 
        scene cs008 with dissolve
        pause 
        scene cleaning with dissolve
        "As she finally pulls away,  a thick string of cum stretches taut between us."
        "it feels as if I'm not truly free from her dick"
        ros "Thanks baby"
        ros "Now clean my dick"
        scene cleaning2 with dissolve
        pause
        scene endkate with dissolve
        "Once I've finished cleaning her dick, I settle back into the passenger seat"
        "The cool leather of the seat contrasts sharply with the heat radiating from my body."
        
        ros "Come on, let's get you home safe"
        scene black 
        
        "As she navigates the familiar streets towards my home, I lean against the window, my mind reeling from the evening's events." 
        "The car comes to a stop outside my apartment building, and Kate turns to face me, her expression unreadable."
        scene endkatecar with dissolve
        ros "We'll continue this another time"
        "her tone leaving no room for argument."
        "With a final, lingering look, she watches as I exit the vehicle and make my way inside."
        $ raver_date_done = True
        jump gotobedKate