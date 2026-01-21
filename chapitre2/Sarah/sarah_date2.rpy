define sal = Character('Salomon', color="#7b9ce2")
define cat = Character('Cat', color="#7b9ce2")
define elise = Character('Elise', color="#1b2b50")
define jay = Character('Jay', color="#00e8f8")

label sarahdate2:
    
    scene stairssarah
    "I close my door, making sure it's locked, and head downstairs."
    "A person is coming down the stairs."
    
    show sarahneutral
    sar "Hi, it's my day off and I have a few friends over. Do you want to join us?"

    menu: 
        "Sure, why not?": 
            sar "Great, see you there."
            hide sarahneutral
            
            jump afternoon_party
        "I'm not sure, I'm a bit tired.": 
            sar "No worries, maybe next time."
            hide sarahneutral
            $ day_until_new_date = 4
            jump map3

label afternoon_party:
    name "Oh, nice. Is it some kind of afternoon party?"

    sar "Yeah, that's the spirit. It's a tea party."

    name "Sounds fun. Give me a minute, I'm coming."

    sar "Great, see you there."
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
    scene climbing2

    "The door is open, letting a cat out."

    cat "Meow."
    scene miaow3
    name "Hi, kitty. That's a nice chonk."
    cat "Mew."
    scene miaow4
    elise "His name is Salomon."

    name "Salomon, that's nice. Hi, Salomon."

    sal "Mrlh?"

    scene headshotelise2
    elise "Come in. I'm Elise."

    name "[name], nice to meet you."

    scene 1test2

    elise "We were talking about you."

    name "What?"

    elise "Sarah told us you were coming."
    
    scene enteringsarahelise
    elise "So we were talking about friendly neighborhoods and how it's rare to have a good one."
    elise "I am changing the track, guys. This is getting boring."
    
    scene e4sarahsayinghi2
    sar "That's Jay and Elise, they are friends from work."
    sar "And that's Salomon, the cat."
    name "Hi, everyone."
    name "I'm [name], nice to meet you."
    jay "Hey, nice to meet you too."
    scene ericlookforaseat
    elise "We were talking about dates."
    
    scene everyone sit eric
    "I sit with them on the couch and try to catch up with the discussion."

    elise "Do you remember last Tuesday when Sacha vomited on the laptop? He just threw up, went to sleep, and then came back like nothing happened. He didn’t even remember that he threw up."

    sar "And he was like, who the fuck threw up on the computer? He didn't even remember."

    elise "And Marion was like, aren’t you tired? It's 10 p.m."

    sar "It's late."

    sar "Honestly, I can’t blame her. I'm getting more tired earlier and earlier."

    jay "You're getting old. What are you, like 30?"

    scene everyonesit2
    sar "Shut the fuck up. I'm 28."

    jay "It's the turning point before 30."

    sar "Yeah, that's what everyone says."

    elise "How original."

    name "As long as you realize your dreams, you stay young."

    elise "Are you competing for the most cliché phrase?"

    name "I'm just saying."

    scene laughing elise
    elise "Live as if you were to die tomorrow."

    jay "The worst mistake you can make is constantly being afraid of making a mistake."

    name "That's a good one."

    elise "I'll write it on my Facebook wall."

    sar "Next to the pro-Palestinian posts, it'll be engraved in stone. Everyone will think you've lost it."

    scene everyone sit eric
    elise "Anyway, how’s your team handling the new project, Sarah?"

    sar "Uh... Not great, honestly."

    sar "It seems like they've completely lost interest in it."

    elise "Really? They can't be that disengaged!"

    sar "Oh, they are. Just last Wednesday, James asked if we were supposed to be designing a video game."

    elise "Why would he think that?"

    sar "I have no idea. I just stared at him in disbelief."

    scene laughing elise
    elise "Haha, that's ridiculous."

    elise "Hopefully, they’ll get back on track soon."

    sar "If they don't, you might have to take charge."

    elise "Yeah, maybe."

    jay "Maybe Elise's secretly sabotaging your team to take your place!"

    jay "It's like Game of Thrones, but with less blood."

    jay "Who knows, maybe she's already poisoned the coffee machine."

    sar "I wouldn't put it past her."

    elise "I'm not that evil."

    sar "Honestly, I am too drained to start thinking about what my coworker could do to me."

    "The conversation continues for a while, and I start to feel more comfortable with them."

    scene looking elise2

    "As we talk, I notice that Elise is trying to catch my glance. She's kinda pretty."

    "I'm not sure if she's interested in me or if I have something weird on my face."

    "I decide to ignore it and keep talking with the group."

    sar "I'm going to make some tea. Does anyone want some?"

    jay "One for me."

    name "Me!"

    scene gettingteae

    sar "What sort of tea do you want, [name]?"

    name "I'll take red tea."

    sar "Got it."

    scene sarcastic
    elise "Red tea? Isn't that a bit strong?"

    name "What do you mean?"

    elise "You remind me of my little sister."
    if gender == "male":
        "I am not sure how I feel about that..."
    name "What's her name?"
    elise "Joanna."
    name "It's pretty."
    jay "Where is she now?"
    elise "She's in Paris for her studies."
    elise "Living the bohemian life."
    elise "A bit like you."
    elise "You remind me of her."
    name "I am not sure how to take it."
    elise "She's kinda cute, so I guess it's a compliment."
    elise "But she is a bit of a brat."
    elise "She sometimes needs to be put back in her place."
    name "I have no doubt that you take care of it very well."
    scene servingtea
    "Sarah is coming back with tea."
    sar "Here you go."
    name "Thanks."
    scene lookingatsarah

    sar "It's cool to see you here."
    name "Yeah, it's nice to meet new people."
    name "Your friends are cool."
    sar "When they are sober, they are, yeah."
    "Sarah keeps looking at me insistently."
    "She seems genuinely happy to see me here."
    jay "Hey, I am also nice when I am drunk."
    sar "Yeah, you are a real sweetheart."
    name "I am sure you are, Jay."
    jay "Thanks."
    sar "You should come to the next party, so you can judge for yourself."
    sar "I am sure you will have a good time."
    name "I'm always up for a party."
    sar "Cool, I'll let you know."
    scene elisestanding
    sar "But you can come by whenever you want, if you want to hang out."
    name "Mh, ok... cool, thanks."
    "Elise gets up and stretches."
    elise "I think I'm going to go. I have some stuff to do."
    jay "I'm going to leave soon too. I need to rest before tomorrow."
    
    name "I should probably go too."
    sar "You can stay if you want."
    "I'm not sure I want to stay alone with Sarah while her friends are leaving..."
    name "I have stuff to do as well, but it was nice to hang out with you guys."
    scene leaving

    sar "Alright, see you around, guys."
    jay "And we'll touch base again about this party, right?"
    sar "Of course, Jay."
    name "See you around."
    
    "We leave the apartment, and after saying goodbye to Jay and Elise, I head home."
    scene home00
    "It's cool to have Sarah as a neighbor. Her friends seem nice too."
    "It reminds me a bit of my friends from my hometown."
    "Ok, where was I?"

    $ sarah_relation_status_text = "I should hang out to the cafe (you will meet Elise there)"
    $ sarah_homedate_done = True
    $ sarah_conv_done = True
    show screen homescreen4
    call screen homescreen4
    
