label lindadate_casual:
    if linda_workday_count == 1:
        jump lindadate_casual1
    elif linda_workday_count == 2:
        jump lindadate_casual2
    elif linda_workday_count == 3:
        jump lindadate_casual3
    elif linda_workday_count == 4:
        jump lindadate_casual4
    

label lindadate_casual1:
    scene livingroomanais5 with fade
    "I walk into the living room; Anaïs is sitting on the couch, scrolling through her phone."
    ana "Hey! Taking a break?"
    name "Yeah, my eyes need a rest."
    scene livingroomanais-kitchen with fade
    "The fridge hums as I refill my water bottle."

    "I take my time, clearing my head and breathing slowly."

    "I hear Anaïs get up and move toward me."
    scene livingroomanais-kitchenblur with dissolve
    "She stands close behind me, her presence warm."
    show anaisneutral with dissolve

    ana "How's it going?"
    name "Hey, Just grabbing water."
    ana "You guys ate yet?"
    name "Just coffee."
    ana "Criminal. Here takes this.."
    "She hands me a peach from a paper bag on the counter."
    show anaisneutralbis with dissolve
    hide anaisneutral with dissolve
    ana "Local market. Saturday only. Sweetest ones all summer."
    "Her fingers brush mine as I take it."

    ana "Go slowly. The juice tends to run."
    "She leans against the counter, watching me bite. A bead of juice escapes."
    show anaislaugh with dissolve
    hide anaisneutralbis with dissolve
    ana "Told you."
    "She laughs, her eyes crinkling as she hands me a paper towel."
    hide anaislaugh with dissolve
    show anaisneutral with dissolve
    "She opens the fridge and takes out a yogurt drink."
    "I wipe my mouth a little clumsily, trying not to make a mess."
    
    ana "So… how’s the thesis treating you?"
    name "Better since Linda’s been helping."
    ana "I saw... you guys seem serious."
    ana "Linda showed me some of your notes earlier."
    ana "color-coded and all. Very cute."
    name "It’s… organized."
    ana "Mhm yeah i see that."
    "She says it lightly, peeling her yogurt lid."
    
    show anaislookleft with dissolve
    hide anaisneutral with dissolve
    ana "You notice the cops more lately? Two patrol cars on the corner every night now."
    name "Yeah, it's a bit unsettling."
    ana "Some dealer got busted two blocks over."
    ana "Makes the walk home feel… watched."
    "She glances out the window, then back at me."
    ana "You walk alone?"
    name "Usually."
    ana "Careful. Pretty face like yours stands out after dark."
    ana "Especially if Linda makes you come home late."
    show anaisneutral with dissolve
    hide anaislookleft with dissolve
    ana "I wouldn't want anything to happen to you.."
    "She smiles, I'm not sure how to take that."
    hide anaisneutral with dissolve
    scene livingroomanais4 with dissolve
    lin "Finally off that call."
    "She sees the peach in my hand, Anaïs leaning close."
    lin "You feeding my assistant now?"
    if gender == "fem":
        ana "Someone has to. She was starving."
    elif gender == "male":
        ana "Someone has to. He was starving."
   
    lin "I’ve got snacks in my room."
    "She grabs my wrist, light but firm, and pulls me toward the hallway."
    lin "Come on. Work to do."
    ana "Enjoy the peach, cutie."

    $ anais_flirtcount += 1
    jump linda_work_end


label lindadate_casual2:
    scene livingroomanais3 with dissolve
    "I’m waiting on the couch. Anais waters a huge monstera near the window."
    show anais neutral with dissolve
    ana "This one’s dramatic. Drops a leaf if you look at it wrong."
    name "You seem to take good care of it."
    ana "Yeah. I do what I can."
    "Anais keeps watering them, glancing at me from time to time."
    "She starts talking to them softly."
    ana "Yeah, I talk to my plants, haha."
    ana "I know it may seem strange."
    ana "But it really works."
    menu:
        "Ask her about it.":
            name "You really talk to them?"
            ana "Of course! They respond better that way."
            name "I’ve never heard of that."
            ana "Try it sometime. You’ll see."
            ana "It keeps their spirits up."
            name "Plants have moods?"
            ana "Everything does. You just have to listen."
            "She turns the pot, then glances at me."
            ana "You ever talk to your plants?"
            name "No… should I?"
            ana "Try it. They like deep voices. Or soft ones. Depends."
            "She smirks, then crouches to snip a yellow leaf."
            ana "See this? Stress. Too much sun, not enough love."
            "Her tone is light, but her eyes flick up to mine—quick, curious."
            ana "Some things just need the right kind of attention."
            $ anais_flirtcount += 1
        "Stay quiet.":
            pass
    name "Okay, well, I'll get back to it. I haven't worked nearly enough today.."
    ana "Alright, don't burn yourself out."
    ana "And don't hesitate to call me if you need anything."
    jump linda_work_end




label lindadate_casual3:
    scene Livingroomanais4 with dissolve
    "I walk into the living room, hoping to relax a little."
    "I don’t see Anaïs."
    "Maybe she went out."
    "I have to admit… I was kind of hoping to talk to her."
    "Suddenly, I hear her coming out of a small room behind me."
    "She folds tiny lace tops into a basket."
    ana "Hey you.."
    ana "You do laundry separately or all in one go?"
    name "Uh… one go. Saves time."
    ana "Brave. I separate delicates."
    "She holds up a black silk camisole, inspects it."
    ana "This one shrank last week. C'est à mon Boyfriend mais didn’t notice."
    name "He didn’t?"
    ana ""
    "She folds it slowly, then looks at me."
    ana "You’d notice, though. You seem… observant."
    jump linda_work_end


    scene lindadate_casual4 
    "It’s hot. A small desk fan oscillates on the coffee table. Anaïs lies on the couch, one arm over her eyes."

    ana "This heat is criminal."
    name "Tell me about it."
    ana "Fan’s useless. Just moves hot air."
    "She lifts her shirt to fan her stomach—pale skin, tiny silver belly ring glints."
    ana "You ever sleep with ice cubes on your chest?"
    name "No…"
    ana "Game-changer. Melts slow. Feels like a cold hand."
    "She says it lazily, eyes still closed."

    ana "How’s work with Linda?"
    name "She’s making me read 300 pages by tomorrow."
    ana "Classic. She used to time me with a stopwatch."
    ana "You keep up?"
    name "Trying."
    ana "Good. She likes effort."
    "She opens one eye, looks at me."
    ana "You drink enough water in this heat?"
    name "Probably not."
    ana "Here—"
    "She hands me her water bottle—condensation cold, her lip print faint on the rim."
    ana "Drink. Doctor’s orders."

    # — Linda returns —
    scene couch_linda_enter with dissolve
    lin "Shower’s free."
    "She walks in, towel around her neck, sees the water bottle in my hand."
    lin "Sharing germs now?"
    ana "He/She was dehydrated. I’m a hero."
    lin "Heroes don’t leave lip prints."
    "She takes the bottle, wipes the rim with her towel, hands it back to me."
    lin "Come on. My room’s cooler."

    $ anais_banal_flirt += 1